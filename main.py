import tkinter as tk
from view.main_window import MainWindow
from controller.face_controller import FaceController
import threading

def run_face_detection(face_controller):
    face_controller.start_detection()

if __name__ == "__main__":
    root = tk.Tk()
    main_window = MainWindow(root)
    face_controller = FaceController(main_window)

    # Iniciar a detecção facial em uma thread separada para não bloquear a interface gráfica
    detection_thread = threading.Thread(target=run_face_detection, args=(face_controller,))
    detection_thread.start()

    root.mainloop()

    # Garantir que a detecção pare quando a interface gráfica for fechada
    face_controller.stop_detection()
    detection_thread.join()

