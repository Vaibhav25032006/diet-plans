from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import datetime

class CalendarScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        self.layout.add_widget(Label(text="YOUR WELLNESS CALENDAR", font_size='22sp', bold=True, size_hint_y=0.1))
        
        # Grid for Calendar Days (7 Columns for Mon-Sun)
        self.grid = GridLayout(cols=7, spacing=5, size_hint_y=0.7)
        self.generate_calendar()
        self.layout.add_widget(self.grid)
        
        # Bottom Navigation Info
        self.status_bar = Label(text="Green = Tasks Completed | Red = Missed Days", font_size='14sp', size_hint_y=0.1)
        self.layout.add_widget(self.status_bar)
        
        self.add_widget(self.layout)

    def generate_calendar(self):
        # Current month and year
        now = datetime.datetime.now()
        year, month = now.year, now.month
        
        # Days of the week headers
        days_headers = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for day in days_headers:
            self.grid.add_widget(Label(text=day, bold=True, color=(0.7, 0.7, 0.7, 1)))
            
        # Dummy performance data (1 = Completed, 0 = Missed, None = Future)
        # Real app mein ye data database ya local storage se aayega
        task_history = {1: 1, 2: 1, 3: 0, 4: 1, 5: 1, 14: 1, 15: 0} 
        
        # Month ke total 30/31 days generate karna
        for day in range(1, 32):
            if day in task_history:
                if task_history[day] == 1:
                    # Task completed - Green Button
                    btn = Button(text=str(day), background_color=(0, 1, 0, 1))
                else:
                    # Task missed - Red Button
                    btn = Button(text=str(day), background_color=(1, 0, 0, 1))
            else:
                # Default Days - Gray Button
                btn = Button(text=str(day), background_color=(0.5, 0.5, 0.5, 1))
                
            self.grid.add_widget(btn)
