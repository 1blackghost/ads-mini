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
'''
# Example usage:
distances = {
    'Joe Biden&Emma Watson': '525.4597986525706m',
    'Joe Biden&Taylor Swift': '800.7877371688455m',
    'Emma Watson&Joe Biden': '525.4597986525706m',
    'Emma Watson&Taylor Swift': '288.2585644868162m',
    'Taylor Swift&Joe Biden': '800.7877371688455m',
    'Taylor Swift&Emma Watson': '288.2585644868162m'
}

social_distance_filter = SocialDistanceFilter(distances)
filtered_distances = social_distance_filter.filter_social_distance(distance_threshold=500)
print(json.dumps(filtered_distances, indent=4))
'''