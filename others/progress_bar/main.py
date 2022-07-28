from tqdm.auto import tqdm #自動で判別
import time
import sys
import warnings

with warnings.catch_warnings():
    #warnings.simplefilter("ignore", category=TqdmExperimentalWarning)
    from tqdm.autonotebook import tqdm as notebook_tqdm
    from tqdm.autonotebook import trange as notebook_trange
from tqdm.std import tqdm as std_tqdm

print(std_tqdm, notebook_tqdm)


for i in tqdm(range(5), leave = False,  desc="test"):
    time.sleep(1)