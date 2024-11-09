from sklearn.cluster import KMeans
import numpy as np
from reverseGeocoding import reverse_geocode
from Utils import read_driver_trips


def suggest_cluster_centers(data, n_clusters):
    # Prepare data for clustering: extract start and endpoint coordinates
    start_points = np.array([[entry["startpoint"]["latitude"], entry["startpoint"]["longitude"]] for entry in data])
    end_points = np.array([[entry["endpoint"]["latitude"], entry["endpoint"]["longitude"]] for entry in data])

    # Initialize KMeans for specified number of clusters for both start and end points
    kmeans_start = KMeans(n_clusters=n_clusters, random_state=0).fit(start_points)
    kmeans_end = KMeans(n_clusters=n_clusters, random_state=0).fit(end_points)

    # Get cluster centers for suggested start and end points
    start_centers = kmeans_start.cluster_centers_
    end_centers = kmeans_end.cluster_centers_

    result = {
        "startPoints": [{"latitude": lat, "longitude": lon} for lat, lon in start_centers],
        "endPoints": [{"latitude": lat, "longitude": lon} for lat, lon in end_centers]
    }

    return result

