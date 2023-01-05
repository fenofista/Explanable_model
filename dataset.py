import os
import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from torch.utils.data import DataLoader
import cv2
import torchvision.transforms.functional as tx
from sklearn.utils import shuffle
import torch
class AL_Dataset():
    def __init__(self, mode):
        if(mode=="train"):
            self.AD_dir = np.array(os.listdir("D:/Project/data_crop/training_data/AD"))
            self.CN_dir = np.array(os.listdir("D:/Project/data_crop/training_data/CN"))
        else:
            self.AD_dir = np.array(os.listdir("D:/Project/data_crop/validation_data/AD"))
            self.CN_dir = np.array(os.listdir("D:/Project/data_crop/validation_data/CN"))
        self.AD = np.ones((len(self.AD_dir)))
        self.CN = np.zeros((len(self.CN_dir)))
        self.df = np.concatenate((self.AD_dir, self.CN_dir))
        self.label = np.concatenate((self.AD, self.CN))
        self.df, self.label = shuffle(self.df, self.label)
        self.mode = mode

    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, idx):
        if self.mode=="train":
            if self.label[idx]==1:
                image_path = "D:/Project/data_crop/training_data/AD/"+self.df[idx]
                label = 1
            else:
                image_path = "D:/Project/data_crop/training_data/CN/"+self.df[idx]
                label = 0
        else:
            if self.label[idx]==1:
                image_path = "D:/Project/data_crop/validation_data/AD/"+self.df[idx]
                label = 1
            else:
                image_path = "D:/Project/data_crop/validation_data/CN/"+self.df[idx]
                label = 0
        whole_image = nib.load(image_path)
        whole_image = np.array(whole_image.dataobj)
        image_arr = np.zeros((90, 256, 256, 3))
        for i in range((90)):            
            image = whole_image[i]
            image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)
            image = normalize(image)
            image = image.reshape(256, 256, 1)
            image = np.concatenate((image, image, image), 2)
            image_arr[i] = image
        return image_arr, label
    
def normalize(arr):
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    return (arr - arr_min) / (arr_max - arr_min)