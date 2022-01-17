import torch
import os
import torch.utils.data as data
import torchvision.transforms as transforms
import random
from PIL import Image,ImageOps
import numpy as np
import os 
import os.path
def default_loader (path):
    return Image.open(path).convert('RGB')
def preprocess(image):
    pass 
class scene_flow_loader(data.Dataset):
    def __init__(self, file_list,training,loader=default_loader):
        super(scene_flow_loader,self).__init__()
        self.file_list=file_list
        self.loader=loader
        self.training=training
    
    def __getitem__(self,index):
        sample=self.file_list[index]
        image_path= sample["file_path"]
        bounding_box=sample["bb"]
        class_id=sample["id"]
        image=self.loader(image_path)
        image=preprocess(image)
        return image,bounding_box,class_id
    def __len__(self):
        return (len(self.file_list))