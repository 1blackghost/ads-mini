import json

class SocialDistanceFilter:
    def __init__(self, distances):
        self.distances = distances

    def filter_social_distance(self, distance_threshold):
        filtered_distances = {}
        for key, distance in self.distances.items():
            
            name1, name2 = key.split('&')
            
            
            if float(self.distances[key])<= distance_threshold:
                filtered_distances[name1] = True
                filtered_distances[name2] = True
            else:
                if (name1  not in filtered_distances or name2 not in filtered_distances):
                    filtered_distances[name1] = False
                    filtered_distances[name2] = False
        return filtered_distances