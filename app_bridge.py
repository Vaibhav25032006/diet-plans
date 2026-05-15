import datetime
from diet_analyzer import DietAnalyzer
from camera_tracker import ActivityScanner
from voice_assistant import HerbalifeVoiceAssistant

class AppBridge:
    def __init__(self, main_app_instance):
        self.main_app = main_app_instance
        self.voice = HerbalifeVoiceAssistant()
        self.scanner = ActivityScanner()
        self.current_user_data = None
        # Local state storage for tasks completed today
        self.completed_tasks_today = set()

    def set_user_context(self, user_data):
        """Google Sheet se aaya hua user data yahan save hota hai"""
        self.current_user_data = user_data
        
    def process_diet_request(self, pdf_path):
        """User ke age ke according correct routine image select karna"""
        if not self.current_user_data:
            return None
            
        analyzer = DietAnalyzer(pdf_path)
        # Returns raw image bytes list (Hindi/English)
        images = analyzer.get_plan_for_user(self.current_user_data)
        
        # Voice alert based on profile
        age = int(self.current_user_data.get('Age', 20))
        if age < 15:
            self.voice.speak("Aapke bache ke liye special daily routine plan taiyar hai.")
        else:
            self.voice.speak("Aapka personalized Herbalife diet plan ready hai.")
            
        return images

    def execute_live_task_scan(self, task_name, success_callback):
        """Camera open karke 10s analysis chalana aur verification handle karna"""
        self.voice.speak(f"Kripya live camera ke saamne apni activity dikhayein. Das second analysis shuru ho raha hai.")
        
        def internal_callback(is_valid):
            if is_valid:
                today_day = datetime.datetime.now().day
                self.completed_tasks_today.add(task_name)
                self.voice.speak("Task successfully verify ho gaya hai. Calendar par green tick mark add kar diya hai.")
                success_callback(True, today_day)
            else:
                self.voice.speak("Activity sahi se detect nahi hui. Kripya dobara koshish karein.")
                success_callback(False, None)
                
        self.scanner.start_10s_analysis(internal_callback)
