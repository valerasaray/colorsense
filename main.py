import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from sklearn.cluster import KMeans
from random import randint as r
from scipy.spatial.distance import cdist

from scan import image_to_rgb
from scan import rgb_to_hex

a = image_to_rgb('images/00000027.jpg')
print(a)

distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 20)

print('+++')

for k in K:
    # Building and fitting the model
    kmeanModel = KMeans(n_clusters=k).fit(a)
    kmeanModel.fit(a)
  
    distortions.append(sum(np.min(cdist(a, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / a.shape[0])
    inertias.append(kmeanModel.inertia_)
  
    mapping1[k] = sum(np.min(cdist(a, kmeanModel.cluster_centers_,
                                   'euclidean'), axis=1)) / a.shape[0]
    mapping2[k] = kmeanModel.inertia_


# for key, val in mapping1.items():
#     print(f'{key} : {val}')


# for key, val in mapping2.items():
#     print(f'{key} : {val}')

plt.figure(1)
plt.subplot (1, 2, 1)
plt.plot(K, distortions, c='tab:orange')
plt.xlabel('Количество кластеров K')
plt.ylabel('Искажение')
plt.title('Метод локтя для искажения')

plt.figure(1)
plt.subplot (1, 2, 2)
plt.plot(K, inertias, c='tab:green')
plt.xlabel('оличество кластеров K')
plt.ylabel('Инерция')
plt.title('Метод локтя для инерции')


print('+++')

kmeans = KMeans(n_clusters=10)

kmeans.fit(a)

print(kmeans.cluster_centers_)

print(rgb_to_hex(list(kmeans.cluster_centers_)))

hex_colors = rgb_to_hex(kmeans.cluster_centers_)
colors = matplotlib.colors.ListedColormap(hex_colors)
all_colors = matplotlib.colors.ListedColormap(rgb_to_hex(a))

plt.figure(2)
plt.axes(projection="3d").scatter(a[:,0],a[:,1], a[:,2], c=kmeans.labels_, cmap=colors)

plt.figure(3)
plt.axes(projection="3d").scatter(a[:,0],a[:,1], a[:,2], c=[range(len(a))], cmap=all_colors)

plt.show()

