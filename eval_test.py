# evalute dice score of model predictions

import os
import glob
from utils.dice_score import dice_coeff
import torch
from torch import Tensor
from PIL import Image 
import numpy as np
from torchvision import transforms

true_files = glob.glob('../kvasir_seg/masks_01/*')
pred_files = glob.glob('../kvasir_seg/pred/*')

dice_scores = []

for i in range(len(true_files)):
    true_img = np.asarray(Image.open(true_files[i]))
    pred_img = np.asarray(Image.open(pred_files[i]))
    pred_img = pred_img[:,:,0]
    true_img = (true_img > 128).astype(int)
    pred_img = (pred_img > 128).astype(int)
    dice_scores.append(2 * np.sum(true_img * pred_img) / (np.sum(true_img) + np.sum(pred_img)))

print(np.mean(np.array(dice_scores)))
print(dice_scores)
