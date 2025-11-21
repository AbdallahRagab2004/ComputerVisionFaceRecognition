import os
import cv2
import numpy as np
import torch
from facenet_pytorch import InceptionResnetV1, MTCNN

# Initialize MTCNN and InceptionResnetV1
mtcnn = MTCNN(keep_all=True)
resnet = InceptionResnetV1(pretrained='vggface2').eval()

# Function to detect and encode faces
def detect_and_encode(image):
    with torch.no_grad():
        boxes, _ = mtcnn.detect(image)
        if boxes is not None:
            faces = []
            for box in boxes:
                face = image[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
                if face.size == 0:
                    continue
                face = cv2.resize(face, (160, 160))
                face = np.transpose(face, (2, 0, 1)).astype(np.float32) / 255.0
                face_tensor = torch.tensor(face).unsqueeze(0)
                encoding = resnet(face_tensor).detach().numpy().flatten()
                faces.append(encoding)
            return faces
    return []

# Function to encode specific images with predefined names
def encode_known_faces(known_faces):
    known_face_encodings = []
    known_face_names = []

    for name, image_path in known_faces.items():
        known_image = cv2.imread(image_path)
        if known_image is not None:
            known_image_rgb = cv2.cvtColor(known_image, cv2.COLOR_BGR2RGB)
            encodings = detect_and_encode(known_image_rgb)
            if encodings:
                known_face_encodings.append(encodings[0])  # Assuming one face per image
                known_face_names.append(name)

    return known_face_encodings, known_face_names

# Known faces dictionary (Week 2)
known_faces = {
    "Abdallah": "images/Abdallah.jpg",
    "Mohamed": "images/Mohamed.jpg",
}
