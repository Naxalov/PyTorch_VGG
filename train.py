import torch
from torch.utils.data import DataLoader
from torch.utils.data import dataset
from utils.datasets import CatDogDataset,split_dataset,show_data,show_grid
from pathlib import Path

# Data Preperation
DATA_DIR = Path('data/PetImages')

dataset = CatDogDataset(DATA_DIR)

train_data,test_data = split_dataset(dataset=dataset,test_size=0.2)

# TO DO
# STATIC LABEL
print('number of dataset:',len(dataset))
print('Train:',len(train_data))

print('Val:',len(test_data))

# Visualizing the Dataset
# show_data(test_data[0])

#Iterate through the DataLoader

# show_grid(test_data,save=True)

# Preparing your data for training with DataLoader

train_dataloader = DataLoader(train_data, batch_size=16, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=16, shuffle=True)


train_features, train_labels  = next(iter(train_dataloader))
show_data((train_features[0], train_labels[0]))