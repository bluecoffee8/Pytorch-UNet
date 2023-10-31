import os
import glob 
from PIL import Image 
import numpy as np


# img = img[:,:,0]
# img = (img > 128)
# print(np.unique(img))
# r = Image.fromarray(np.uint8(img)).convert('RGB')
# r.save('test.jpg')

# mask_files = glob.glob('../kvasir_seg/masks/*.jpg')
# thresh = 128 
# fn = lambda x : 255 if x > thresh else 0

# img = Image.open(mask_file)
# r = img.convert('L').point(fn, mode='1')
# z = np.asarray(r)
# print(z.shape)
# print(np.unique(z))

# for mask_file in mask_files:
#     img = Image.open(mask_file)
#     r = img.convert('L').point(fn, mode='1')
#     r.save('data/masks_01/' + mask_file[11:])

# mask_file = mask_files[0]
# img = np.asarray(Image.open(mask_file))
# print(np.unique(img))
