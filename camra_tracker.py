import cv2
import time
from kivy.clock import Clock

class ActivityScanner:
    def __init__(self):
        self.cap = cv2.VideoCapture(0) # Camera open karega
        self.scanning = False
        self.start_time = 0

    def start_10s_analysis(self, callback):
        """10 second ka live analysis shuru karta hai"""
        self.scanning = True
        self.start_time = time.time()
        
        # Har frame check karne ke liye clock setup
        Clock.schedule_interval(lambda dt: self.analyze_frame(callback), 1.0/30.0)

    def analyze_frame(self, callback):
        ret, frame = self.cap.read()
        if not ret or not self.scanning:
            return False

        elapsed_time = time.time() - self.start_time
        
        # Screen par 'Analyzing...' text dikhana
        cv2.putText(frame, f"Analyzing Activity: {int(10 - elapsed_time)}s", 
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("AI Activity Scanner", frame)

        if elapsed_time >= 10:
            self.scanning = False
            cv2.destroyAllWindows()
            # Yahan logic aayega ki activity 'Sahi' thi ya nahi
            # Abhi ke liye hum ise 'True' maan rahe hain
            callback(True) 
            return False

    def stop(self):
        self.scanning = False
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()

# Callback function jo Task Tick karega
def on_task_verified(success):
    if success:
        print("Task Completed! Automatic Tick added to Calendar.")
