import json

class SocialDistanceFilter:
    def __init__(self, distances):
        self.distances = distances

    def filter_social_distance(self, distance_threshold):
        filtered_distances = {}
        for key, distance in self.distances.items():
            name1, name2 = key.split('&')
            name1, name2 = sorted([name1, name2])
            if float(distance[:-1]) <= distance_threshold:
                filtered_distances[name1] = True
                filtered_distances[name2] = True
            else:
                filtered_distances[name1] = False
                filtered_distances[name2] = False
        return filtered_distances