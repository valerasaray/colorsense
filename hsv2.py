import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
from colorsys import rgb_to_hsv, hsv_to_rgb
from PIL import Image
from scan import image_to_rgb
from scan import rgb_to_hex
from hue import hue, list_hue
import matplotlib.colors
from math import sqrt




def mode_hsv_to_rgb(hsv):
    rgb = np.array(hsv_to_rgb(hsv[0]/360, hsv[1]/100, hsv[2]/100))
    rgb = np.array(list(map(lambda x: int(x*250), rgb)))
    return rgb

def mode_rgb_to_hsv(rgb):
    hsv = list(rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255))
    hsv[0] *= 360
    hsv[1] *= 100
    hsv[2] *= 100
    hsv.append(hue(hsv[0])[0])
    hsv.append(hue(hsv[0])[1])
    hsv = np.array(list(map(lambda x: int(x), hsv)))
    return hsv

def image_to_rgb_hsv(image_path):
    rgb = image_to_rgb(image_path)
    hsv = []
    for i in rgb:
        hsv.append(mode_rgb_to_hsv(i))
    return [np.array(rgb), np.array(hsv)]



def hsv_centroids_to_rgb(kmeans):
    rgb_centroids = []
    for i in kmeans.cluster_centers_:
        print('=====')
        i = i.astype(int)
        print(i)
        flag = 0
        list_distance = []
        for j in list_hue:
            list_distance.append(sqrt((j[0]-i[2])**2+(j[1]-i[3])**2))
        dot = list_distance.index(min(list_distance)) 

        i[0], i[1], i[2] = dot, i[0], i[1]
        i = np.delete(i, 3)
        print(list_hue[dot])
        print(i[0])
        print('=====')
        rgb_centroids.append(mode_hsv_to_rgb(i))
    return np.array(rgb_centroids)


def hsv2_clustering(image_path, count_clusters):
    kmeans = KMeans(n_clusters=count_clusters)
    image = image_to_rgb_hsv(image_path)
    rgb = image[0]
    hsv = image[1]
    hsv = hsv[:,1:]
    kmeans.fit(hsv)

    hex_colors = rgb_to_hex(hsv_centroids_to_rgb(kmeans))
    colors = matplotlib.colors.ListedColormap(hex_colors)
    all_colors = matplotlib.colors.ListedColormap(rgb_to_hex(rgb))

    print(hex_colors)

    plt.figure(2)
    plt.axes(projection="3d").scatter(hsv[:,0],hsv[:,1], hsv[:,2], hsv[:,3],  c=kmeans.labels_, cmap=colors)

    plt.figure(3)
    plt.axes(projection="3d").scatter(hsv[:,0],hsv[:,1], hsv[:,2], hsv[:,3],  c=[range(len(hsv))], cmap=all_colors)

    plt.show()