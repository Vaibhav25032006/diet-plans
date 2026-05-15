import os
import urllib.request
from bs4 import BeautifulSoup
from gtts import gTTS
import pygame
import speech_recognition as sr

class HerbalifeVoiceAssistant:
    def __init__(self):
        pygame.mixer.init()
        self.recognizer = sr.Recognizer()

    def speak(self, text_to_say):
        """Text ko female professional voice mein convert karke play karta hai"""
        try:
            # gTTS default voice natural female Hindi/English mix support karti hai
            tts = gTTS(text=text_to_say, lang='hi', slow=False)
            audio_file = "response.mp3"
            tts.save(audio_file)
            
            # Play Audio
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
                
            pygame.mixer.music.unload()
            os.remove(audio_file) # Temp file cleanup
        except Exception as e:
            print(f"Voice Error: {e}")

    def google_search_fallback(self, query):
        """Agar AI ko database mein answer nahi mila, toh web search karega"""
        try:
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            req = urllib.request.Request(search_url, headers=headers)
            html = urllib.request.urlopen(req).read()
            
            soup = BeautifulSoup(html, 'html.parser')
            # Pehla reliable description snippet nikalna
            snippet = soup.find('div', class_='BNeawe s3v9rd AP7Wnd')
            if snippet:
                return snippet.get_text()
            return "Mujhe iski jaankari Google par nahi mili."
        except Exception:
            return "Network issue ki wajah se main search nahi kar paayi."

    def listen_user(self):
        """User ki awaaz ko sunna"""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                user_text = self.recognizer.recognize_google(audio, language='hi-IN')
                return user_text
            except Exception:
                return None

# Quick Check Execution Logic
if __name__ == "__main__":
    assistant = HerbalifeVoiceAssistant()
    # Test Greeting
    assistant.speak("Namaste! Main aapki Herbalife smart coach hoon. Aap apna data analyze kar sakte hain.")
