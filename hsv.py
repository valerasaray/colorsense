import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

import numpy as np
from colorsys import rgb_to_hsv
from PIL import Image
from scan import image_to_rgb

image_path = 'image/pix2.jpg'

def mode_hsv_

def mode_rgb_to_hsv(rgb):
    hsv = np.array(rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255))
    hsv[0] = int(hsv[0] * 360)
    hsv[1] *= 100
    hsv[2] *= 100
    hsv = np.array(list(map(lambda x: int(x), hsv)))
    return hsv
print('+++')

def image_to_hsv(image_path):
    rgb = image_to_rgb(image_path)
    hsv = []
    for i in rgb:
        hsv.append(mode_rgb_to_hsv(i))
    return np.array(hsv)

hsv = image_to_hsv('images/uk.jpg')







kmeans = KMeans(n_clusters=4)

kmeans.fit(hsv)

print(kmeans.cluster_centers_)



plt.figure(1)
plt.axes(projection="3d").scatter(hsv[:,0],hsv[:,1], hsv[:,2], c=kmeans.labels_)
plt.show()