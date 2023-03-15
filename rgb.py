import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np
from sklearn.cluster import KMeans
from random import randint as r
from scipy.spatial.distance import cdist
from sklearn.metrics import silhouette_score

from scan import image_to_rgb
from scan import rgb_to_hex


def rgb_clustering(image_path, cluster_count):
    a = image_to_rgb(image_path)
    print(a)

    distortions = []
    inertias = []
    mapping1 = {}
    mapping2 = {}
    K = range(2, 10)

    print('+++')
    s_scores = []

    for k in K:
        # Building and fitting the model
        kmeans = KMeans(n_clusters=k).fit(a)
        kmeans.fit(a)
    
        distortions.append(sum(np.min(cdist(a, kmeans.cluster_centers_,
                                            'euclidean'), axis=1)) / a.shape[0])
        inertias.append(kmeans.inertia_)
    
        mapping1[k] = sum(np.min(cdist(a, kmeans.cluster_centers_,
                                    'euclidean'), axis=1)) / a.shape[0]
        mapping2[k] = kmeans.inertia_

        kmeans = KMeans(n_clusters=k)
        cluster_labels = kmeans.fit_predict(a)

        # if k > 2:
        #     score = silhouette_score(a, cluster_labels)
        #     s_scores.append(score)
        #     print(f'Количество кластеров: {k}, средний score: {score:.3f}')


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

    # cluster_count = s_scores.index(max(s_scores)) + 3
    kmeans = KMeans(n_clusters=cluster_count)

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