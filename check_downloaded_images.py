# some of the images in catalog.csv is a 1 channel image of a warning message
# we will need to remove them from our dataset

import pandas as pd
from skimage import io

df = pd.read_csv('catalog.csv')
df['has_valid_image'] = df['product'].apply(lambda x: io.imread(f'./images/{x}.jpg').shape[-1] == 3)
df.to_csv('catalog.csv', index=False)

