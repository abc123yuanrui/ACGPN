import os 
from os.path import isfile, join

path = 'D:/VirtualFitting/dataset/ACGPN_traindata/train_colormask'
onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
print(len(onlyfiles), 'files')