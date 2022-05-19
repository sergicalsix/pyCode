from natsort import natsorted
from PIL import Image
import glob
 
# GIFアニメーションを作成
def create_gif(path_list ,output_file = "all.gif"):
    """
    usage:
        create_gif(path_list = natsorted(glob.glob('img/all/*.png'))
    """
    imgs = []                                                 
 
    for path in path_list:
        img = Image.open(path)                   
        imgs.append(img)                                 
    
    #最後だけ少し長くする
    #for _ in range(30):
      #  imgs.append(img)  
        
    
    imgs[0].save(output_file,
                 save_all=True, append_images=imgs[1:], optimize=False, duration=10, loop=0)
    

create_gif(path_list = natsorted(glob.glob('img/all/*.png')))
