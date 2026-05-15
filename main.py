import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# Data fetching function ko import kar rahe hain
try:
    from sheets_handler import get_member_data
except ImportError:
    def get_member_data(member_id):
        return {"error": "sheets_handler.py file missing!"}

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        self.layout.add_widget(Label(text="HERBALIFE SMART WELLNESS", font_size='28sp', bold=True))
        self.layout.add_widget(Label(text="Enter Member ID to Start Analysis", font_size='16sp'))
        
        self.member_id_input = TextInput(
            multiline=False, 
            hint_text="Type Member ID here...",
            size_hint_y=None,
            height='50dp',
            padding_y=(10, 10)
        )
        self.layout.add_widget(self.member_id_input)
        
        self.btn_login = Button(
            text="VERIFY & ANALYZE", 
            size_hint_y=None, 
            height='60dp',
            background_color=(0.1, 0.7, 0.3, 1)
        )
        self.btn_login.bind(on_press=self.verify_id)
        self.layout.add_widget(self.btn_login)

        self.status_label = Label(text="", color=(1, 0, 0, 1), halign="center")
        self.layout.add_widget(self.status_label)
        
        self.add_widget(self.layout)

    def verify_id(self, instance):
        mid = self.member_id_input.text.strip()
        if not mid:
            self.status_label.text = "Error: Please enter a Member ID"
            return

        self.status_label.text = "Searching in Google Sheets..."
        self.status_label.color = (1, 1, 1, 1)
        
        # UI freeze na ho isliye halka sa delay ya threading zaroori hoti hai
        Clock.schedule_once(lambda dt: self.fetch_process(mid), 0.5)

    def fetch_process(self, mid):
        result = get_member_data(mid)
        
        if result and "error" in result:
            self.status_label.text = f"System Error: {result['error']}"
            self.status_label.color = (1, 0, 0, 1)
        elif result:
            name = result.get('Name', 'Member')
            self.status_label.text = f"Success! Welcome {name}.\nAnalyzing Diet Plans..."
            self.status_label.color = (0, 1, 0, 1)
            # Yahan se Dashboard screen par jayenge agli file mein
        else:
            self.status_label.text = "Member ID not found in records."
            self.status_label.color = (1, 0, 0, 1)

class HerbalifeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        return sm

if __name__ == '__main__':
    HerbalifeApp().run()
