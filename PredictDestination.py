import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

from Utils import read_driver_trips
from reverseGeocoding import reverse_geocode


# Assuming the function read_driver_trips is defined elsewhere
def predictnextdestination(data):

    # Extract startpoints and endpoints
    startpoints = np.array([[entry['startpoint']['latitude'], entry['startpoint']['longitude']] for entry in data])
    endpoints = np.array([[entry['endpoint']['latitude'], entry['endpoint']['longitude']] for entry in data])

    # Combine startpoints and endpoints for clustering
    all_coordinates = np.vstack((startpoints, endpoints))

    # Apply KMeans clustering
    n_clusters = 1  # Adjust the number of clusters as needed
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(all_coordinates)

    # Predict clusters for each coordinate
    predicted_clusters = kmeans.predict(all_coordinates)

    # Count occurrences of coordinates in each cluster
    cluster_counts = Counter(predicted_clusters)

    # Find the most populated cluster
    most_populated_cluster = cluster_counts.most_common(1)[0][0]

    # Get indices of coordinates in the most populated cluster
    indices = np.where(predicted_clusters == most_populated_cluster)[0]

    # Separate startpoints and endpoints based on the indices
    most_common_startpoints = startpoints[np.isin(np.arange(len(startpoints)), indices)]
    most_common_endpoints = endpoints[np.isin(np.arange(len(endpoints)), indices - len(startpoints))]

    # Count occurrences of the most common startpoints and endpoints
    most_common_startpoint = Counter(map(tuple, most_common_startpoints)).most_common(1)[0]
    most_common_endpoint = Counter(map(tuple, most_common_endpoints)).most_common(1)[0]

    startpoint_address ={"startpoint_address":reverse_geocode(most_common_startpoint[0][0], most_common_startpoint[0][1]),"latitude": most_common_startpoint[0][0], "longitude": most_common_startpoint[0][1]}
    endpoint_address = {"endpoint_address":reverse_geocode(most_common_endpoint[0][0], most_common_endpoint[0][1]),"latitude": most_common_startpoint[0][1], "longitude": most_common_startpoint[0][1]}


    return startpoint_address,endpoint_address



