import numpy as np
import pandas as pd
import rasterio
import rasterio.features
import rasterio.warp
from matplotlib import pyplot as plt
from configparser import ConfigParser

file =  'config.ini'
config = ConfigParser()
config.read(file)

file1 = config['ECE file path']['ECEpath']
file2 = config['Soil file path']['Soilpath']
file3 = config['Raw data file']['Rawpath']



dataset1 = rasterio.open(file1)
#dataset2 = rasterio.open(file2)


band1 = dataset1.read(1)
#band2 = dataset2.read(1)

def featureextract(x,y):
    xs = x
    ys = y
    with dataset1 as src:
        rows, cols = rasterio.transform.rowcol(src.transform, xs, ys)   
    
    feature = band1[rows, cols]
    
    return feature

fig = plt.figure(figsize= (10,10))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(band1, cmap = "pink")   

def mergingdata():
    df_data = pd.read_csv(file3)
    df_data['ECE'] = 0.5

    for i, row in df_data.iterrows():  
        x = df_data['long'][i]
        y = df_data['lag'][i]
        df_data['ECE'][i] = featureextract(x,y)
    
    df_data.to_excel("testpackage.xlsx",index=False)



