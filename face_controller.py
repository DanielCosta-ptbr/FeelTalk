import cv2
from model.face_recognition import FaceRecognition
from view.main_window import MainWindow
import threading

class FaceController:
    def __init__(self, main_window):
        self.face_recognition = FaceRecognition()
        self.main_window = main_window
        self.running = True

    def start_detection(self):
        cap = cv2.VideoCapture(0)
        while self.running:
            ret, frame = cap.read()
            if not ret:
                break

            expression = self.face_recognition.detect_expression(frame)
            self.main_window.update_buttons(expression)
            
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break
        
        cap.release()
        cv2.destroyAllWindows()

    def stop_detection(self):
        self.running = False

