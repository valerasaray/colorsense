import matplotlib.pyplot as plt
import cv2
import glob
import os

directory = 'C:/Users/vsu70/Desktop/images'

for filename in os.listdir(directory):
    print('+++')
    name = os.path.join(filename)
    if f'{name[-3:-1]}{name[-1]}' != 'jpg':
        print(f'{name[-3:-1]}{name[-1]}')
        continue
    print(name)
    filter = cv2.imread(name)
    filter = cv2.resize(filter, (300, 300), interpolation=cv2.INTER_CUBIC)
    filter = cv2.cvtColor(filter, cv2.COLOR_BGR2RGB)
    plt.imsave(name.split('.')[0] + '.jpg', filter)
