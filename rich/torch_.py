import torch 
from torch import cuda
from torch import  optim

import os 
### my script

from rich.traceback import install

install()

import backtrace

backtrace.hook(
    reverse=True,         # 逆順
    strip_path=True    # ファイル名のみ
)

### TODO: config.yaml
is_cnn = False
seed = 2020
input_size, hidden_size ,output_size = 784, 784, 2
data_type = "mnist"

epochs = 10
batch_size = 100

optimizer_name = 'Adam'
lr = 0.001

cuda_name = 'cuda:0'

normal = True
dropout = False


### environment 
torch.manual_seed(seed)
device = cuda_name if cuda.is_available() else "cpu"
print(f"Using {device} device")
os.environ['CUDA_VISIBLE_DEVICES'] = cuda_name[-1]
os.environ['TF_DETERMINISTIC_OPS'] = '1'

### 
train_dataloader1, val_dataloader1 , test_dataloader1  = generate_dataloader(data_name = data_type , is_cnn = is_cnn, batch_size = batch_size, split_labels = [0,1] , permuted=False)
train_dataloader2, val_dataloader2 , test_dataloader2  = generate_dataloader(data_name = data_type , is_cnn = is_cnn, batch_size = batch_size, split_labels = [2,3], permuted=False)


model = ThreeFcNet(input_size = input_size, hidden_size = hidden_size ,output_size = output_size)
loss_fn = nn.CrossEntropyLoss()
exec('optimizer = optim.' + optimizer_name + '(model.parameters(), lr=lr)')


result = Result(data_type ,model.model_name , optimizer_name , lr, split = True)
trainer = Trainer()


### 重み保存
if normal:
    pre_model_path = f"torch_model/{data_type}_{model.model_name}_{optimizer_name}_normal_epoch0.pt"
else:
    pre_model_path = f"torch_model/{data_type}_{model.model_name}_{optimizer_name}_epoch0.pt"
torch.save(model.state_dict(),pre_model_path)

model.to(device)
analysis_model  = TorchModelAnalysis(tmp_model,pre_model_path, pro_model_path = None )
same_hub_percentage_list,hub_growth_rate_list, pro_input_output_hub_rate_list = [1.0],[1.0],[0.0] # TODO: 本当に0?

print('Part1 Start!!')
for epoch in range(1, epochs + 1):
    
    loss, acc = trainer.train(model, loss_fn, device, train_dataloader1, optimizer)
    result.set_result(loss, acc , key = 'train')
    loss, acc = trainer.test(model, loss_fn, device, val_dataloader1)
    result.set_result(loss, acc , key = 'val')
    
    print(f"epoch = {epoch}, {result.acc['val'][-1]}" )

    analysis_model.get_model_weight(model, add_method = True)

    _ = analysis_model.analysis_hub()
    same_hub_percentage, hub_growth_rate, pre_input_output_hub_rate, pro_input_output_hub_rate  = _
    same_hub_percentage_list.append(same_hub_percentage[1])
    hub_growth_rate_list.append(hub_growth_rate[1])
    pro_input_output_hub_rate_list.append(pro_input_output_hub_rate[0])

    print("Part1", same_hub_percentage_list,  hub_growth_rate_list)

analysis_model.set_task_weight(task_name = "task1", weight_list = None)
print('\nPart2 Start!!')
for epoch in range(1, epochs + 1):
    
    loss, acc = trainer.train(model, loss_fn, device, train_dataloader2, optimizer)
    result.set_result(loss, acc , key = 'train2')
    loss, acc = trainer.test(model, loss_fn, device, val_dataloader2)
    result.set_result(loss, acc , key = 'val2')
    
    loss, acc = trainer.test(model, loss_fn, device, val_dataloader1)
    result.set_result(loss, acc , key = 'val1')
    print(f"epoch = {epoch}, {result.acc['val2'][-1]}, {result.acc['val1'][-1]}" )

    analysis_model.get_model_weight(model, add_method = True)

    _ = analysis_model.analysis_hub(task_name = "task1")
    same_hub_percentage, hub_growth_rate, pre_input_output_hub_rate, pro_input_output_hub_rate  = _
    same_hub_percentage_list.append(same_hub_percentage[1])
    hub_growth_rate_list.append(hub_growth_rate[1])
    pro_input_output_hub_rate_list.append(pro_input_output_hub_rate[0])

    print("Part2", same_hub_percentage_list[epochs+1:],  hub_growth_rate_list[epochs+1:])
    

print(result.acc)
result.save_split_result()
result.write_log()
