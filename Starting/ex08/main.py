
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(300)):
    sleep(0.005)
print()

for elem in tqdm(range(300)):
    sleep(0.005)
print()
