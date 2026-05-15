import fitz  # PyMuPDF
import io
from PIL import Image

class DietAnalyzer:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)

    def get_plan_for_user(self, user_data):
        # User data se age ya category nikalna
        age = int(user_data.get('Age', 20)) 
        
        # Logic: Agar age 15 se kam hai toh bacchon wala plan (Page 1-2)
        # Warna adults wala plan (Page 3-10)
        if age < 15:
            plan_pages = [0, 1] # Hindi & English for kids
        else:
            plan_pages = [2, 3, 4, 5] # Normal plans
            
        return self.extract_images(plan_pages)

    def extract_images(self, page_numbers):
        images = []
        for p in page_numbers:
            page = self.doc.load_page(p)
            pix = page.get_pixmap()
            img_data = pix.tobytes("png")
            images.append(img_data)
        return images

# Usage example for the AI Assistant logic
# analyzer = DietAnalyzer('diet_plans.pdf')
# user_images = analyzer.get_plan_for_user(member_data)
