import face_recognition
import itertools
import os

class SocialDistanceChecker:
    def __init__(self, main_image_path, faces):
        self.main_image_path = main_image_path
        self.main_image = face_recognition.load_image_file(main_image_path)
        self.main_face_locations = face_recognition.face_locations(self.main_image)
        self.faces = {name: face_recognition.load_image_file(path) for name, path in faces.items()}
        self.face_locations = {name: face_recognition.face_locations(image) for name, image in self.faces.items()}

    def calculate_distance(self, face1_loc, face2_loc):
        x_distance = abs(face1_loc[1] - face2_loc[1])
        y_distance = abs(face1_loc[0] - face2_loc[0])
        z_distance = abs((face1_loc[3] - face1_loc[1]) - (face2_loc[3] - face2_loc[1]))  
        distance = (x_distance**2 + y_distance**2 + z_distance**2)**0.5
        return distance

    def check_social_distance(self):
        result = {}
        for (face1_index, face1_loc), (face2_index, face2_loc) in itertools.product(enumerate(self.main_face_locations), enumerate(self.main_face_locations)):
            if face1_index == face2_index:
                continue
            
            face1_name = list(self.faces.keys())[face1_index]
            face2_name = list(self.faces.keys())[face2_index]
            distance = self.calculate_distance(face1_loc, face2_loc)
            result[f"{face1_name}&{face2_name}"] = f"{distance}m"
        return result


