from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser

class DashboardScreen(Screen):
    def __init__(self, user_data=None, **kwargs):
        super().__init__(**kwargs)
        self.user_data = user_data or {"Name": "User", "Age": "20"}
        
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Professional Coach Welcome Header
        header_text = f"Coach Dashboard\nWelcome, {self.user_data.get('Name')}!"
        layout.add_widget(Label(text=header_text, font_size='24sp', bold=True, halign='center', size_hint_y=0.15))
        
        # Grid for Specific Feature Buttons
        grid = GridLayout(cols=2, spacing=15, size_hint_y=0.6)
        
        # Button 1: View Personalized Diet Plan
        btn_diet = Button(text="📋\nDiet Plan", font_size='18sp', halign='center', background_color=(0.2, 0.6, 1, 1))
        btn_diet.bind(on_press=self.open_diet_plan)
        grid.add_widget(btn_diet)
        
        # Button 2: Scan Live Activity (Camera)
        btn_scan = Button(text="📷\nScan Activity\n(10s AI Check)", font_size='18sp', halign='center', background_color=(0.1, 0.8, 0.3, 1))
        btn_scan.bind(on_press=self.start_camera_scan)
        grid.add_widget(btn_scan)
        
        # Button 3: Track Progress Calendar
        btn_cal = Button(text="📅\nView Calendar", font_size='18sp', halign='center', background_color=(0.9, 0.5, 0.1, 1))
        btn_cal.bind(on_press=self.go_to_calendar)
        grid.add_widget(btn_cal)
        
        # Button 4: Talk to AI Female Assistant
        btn_voice = Button(text="🎙️\nTalk to AI Coach\n(Female Voice)", font_size='18sp', halign='center', background_color=(0.6, 0.3, 0.8, 1))
        btn_voice.bind(on_press=self.trigger_voice_assistant)
        grid.add_widget(btn_voice)
        
        layout.add_widget(grid)
        
        # Button 5 (Bottom): Go To Main Website
        btn_website = Button(
            text="🌐 Go to Main Website", 
            size_hint_y=None, 
            height='60dp', 
            background_color=(0.8, 0.1, 0.2, 1),
            bold=True
        )
        btn_website.bind(on_press=self.open_canva_website)
        layout.add_widget(btn_website)
        
        self.add_widget(layout)

    def open_diet_plan(self, instance):
        print("Opening diet plans extracted from PDF...")
        # Yahan File 3 (DietAnalyzer) trigger hogi

    def start_camera_scan(self, instance):
        print("Starting 10-second live camera tracker...")
        # Yahan File 4 (ActivityScanner) trigger hoga

    def go_to_calendar(self, instance):
        self.manager.current = 'calendar'

    def trigger_voice_assistant(self, instance):
        print("AI Assistant is listening...")
        # Yahan File 6 (HerbalifeVoiceAssistant) trigger hoga

    def open_canva_website(self, instance):
        # File 8 ka use karke link open hoga
        from web_launcher import open_studio_link
        open_studio_link()
