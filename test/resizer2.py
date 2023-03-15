import matplotlib.pyplot as plt
import cv2
import os

directory = 'C:\\Users\\vsu70\\Desktop\\colorsense2\\colorsense\\test'
name = f'{directory}\\{input()}'
image = cv2.imread(name)
image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_CUBIC)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imsave(name.split('.')[0] + '2.png', image)