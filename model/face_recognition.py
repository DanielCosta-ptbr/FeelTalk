import cv2
import dlib
import numpy as np

class FaceRecognition:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor('path/to/shape_predictor_68_face_landmarks.dat')

    def shape_to_np(self, shape, dtype="int"):
        coords = np.zeros((68, 2), dtype=dtype)
        for i in range(68):
            coords[i] = (shape.part(i).x, shape.part(i).y)
        return coords

    def mouth_aspect_ratio(self, mouth):
        A = np.linalg.norm(mouth[2] - mouth[10])
        B = np.linalg.norm(mouth[4] - mouth[8])
        C = np.linalg.norm(mouth[0] - mouth[6])
        mar = (A + B) / (2.0 * C)
        return mar

    def eye_aspect_ratio(self, eye):
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        C = np.linalg.norm(eye[0] - eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def detect_expression(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detector(gray, 0)

        for face in faces:
            shape = self.predictor(gray, face)
            shape = self.shape_to_np(shape)
            
            # Detectando sorriso
            mouth = shape[48:68]
            mar = self.mouth_aspect_ratio(mouth)
            if mar > 0.5:
                return "sorriso"
            
            # Detectando piscada de um olho
            left_eye = shape[42:48]
            right_eye = shape[36:42]
            ear_left = self.eye_aspect_ratio(left_eye)
            ear_right = self.eye_aspect_ratio(right_eye)
            if ear_left < 0.2 and ear_right > 0.2:
                return "piscando olho esquerdo"
            elif ear_right < 0.2 and ear_left > 0.2:
                return "piscando olho direito"

            # Detectando franzir testa
            brow_left = shape[21]
            brow_right = shape[22]
            if brow_left[1] < shape[19][1] and brow_right[1] < shape[24][1]:
                return "franzindo testa"

            # Detectando mostrar dentes
            mouth_open = shape[66][1] - shape[62][1]
            if mar > 0.5 and mouth_open > 15:
                return "mostrando dentes"
            
        return "neutro"  # Nenhuma expressão detectada

