# check defualt clustering size for kmeans

from sklearn.cluster import KMeans
import numpy as np

test_arr_k_need_more_samples = np.array([[1,2,3,4],[1,2,3,4]])

# need atleast 8 unique samples for default clustering of 8 clusters
test_arr_k = np.array([[51,2,3,4],[1,25,3,23], [1,24,53,4], [17,2,3,4], [1,28,53,4], [1,24,73,4], [1,2,3,84], [1,26,73,54],])

model = KMeans().fit(test_arr_k)