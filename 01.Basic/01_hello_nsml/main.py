""" 01: Hello NSML
=====================================

A simple example of how to connect to NSML and print a few values.

"""

import torch
import time
import os
from nsml import GPU_NUM, DATASET_PATH, DATASET_NAME


with open(os.path.join(DATASET_PATH, 'train/data.txt')) as f:
    print('read from dataset {0}'.format(DATASET_NAME), [line for line in f])

# print number of gpus
print('Number of gpus: {}'.format(GPU_NUM))

print('Hello NSML!')
for x in range(20):
    time.sleep(1)
    print('Hello timer', x)
print(torch)
