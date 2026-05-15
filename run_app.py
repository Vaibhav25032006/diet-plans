import os
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from main import LoginScreen
from dashboard import DashboardScreen
from calendar_view import CalendarScreen
from app_bridge import AppBridge

class MasterHerbalifeApp(App):
    def build(self):
        # Window configuration and styling setup
        self.title = "Herbalife Smart Wellness Studio"
        
        # Main Screen Manager initialization
        self.screen_manager = ScreenManager()
        
        # Bridge initiate karna jo state maintain karega
        self.bridge = AppBridge(self)

        # Screens setup aur loading
        self.login_screen = LoginScreen(name='login')
        self.calendar_screen = CalendarScreen(name='calendar')
        
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.calendar_screen)
        
        # Kivy check clock setup framework pipeline
        return self.screen_manager

    def transition_to_dashboard(self, verified_user_data):
        """Login pass hone ke baad dynamically dashboard create karna user data ke sath"""
        self.bridge.set_user_context(verified_user_data)
        
        # Naya dashboard user dynamic parameters ke sath inject karna
        dashboard_screen = DashboardScreen(user_data=verified_user_data, name='dashboard')
        self.screen_manager.add_widget(dashboard_screen)
        self.screen_manager.current = 'dashboard'

if __name__ == '__main__':
    # Environment Setup check to prevent crashes
    if not os.path.exists('credentials.json'):
        print("[WARNING]: 'credentials.json' missing! Google Sheets auto-sync offline rahega.")
        
    print("Herbalife Smart Wellness App Engine starting up...")
    MasterHerbalifeApp().run()
