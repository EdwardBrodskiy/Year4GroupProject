import pandas as pd
import numpy as np
np.random.seed(42)
import os

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

def load_everything(dataset_path): # you should use this function as it avoids storing duplicates of the image data hence saving ram
    dataset = get_data(dataset_path)
    
    x_train, x_test, y_train, y_test = extract_train_test_sets(dataset)
    
    dataset = dataset.drop(columns='image')
    
    return dataset, (x_train, x_test, y_train, y_test)
    

def get_data(dataset_path): # return shuffled dataset
    metadata = pd.read_csv(os.path.join(dataset_path, 'generated_metadata.csv'), index_col=0)
    
    metadata = metadata.sample(frac=1).reset_index(drop=True)
    
    images = []
    for path, dirnames, filenames in os.walk(os.path.join(dataset_path,'generated')):
        if not filenames: # skip empty directory
            continue
        for filename in filenames:
            full_path = os.path.join(path, filename)
            
            images.append((filename[:-4], get_img(full_path)))
    
    images = pd.DataFrame(images, columns=('img_name', 'image'))
    
    
    dataset = metadata.merge(images, on='img_name', how='inner')
    dataset = dataset.astype({
        'img_name': 'string',
        'img_source': 'category',
        'fire': 'bool',
        'pos_y': np.uint32,
        'pos_x': np.uint32,
        'wind_direction': np.float64,
        'wind_strength': np.float64,
    }, errors='ignore')
    
    return dataset

def get_img(path):
    img = plt.imread(path)
    if img.dtype == 'uint8':
        img = img.astype(np.float32) / 255
    return img

def extract_train_test_sets(data):
    y = np.array(data['fire'])
    x = np.concatenate(list(map(lambda x: x[np.newaxis, :, :, :], data['image'])), axis=0)
    return train_test_split(x, y, shuffle=False)