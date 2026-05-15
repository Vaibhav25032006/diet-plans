import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def get_member_data(member_id):
    # Google Sheets setup
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Path check: Kya credentials file maujood hai?
    creds_file = 'credentials.json'
    
    if not os.path.exists(creds_file):
        return {"error": "credentials.json file not found in folder!"}

    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        client = gspread.authorize(creds)
        
        # Link se sheet open karna
        sheet_id = "1krG5NFJ2Uo2tP90fgh9ZeuIJRN80GRkcbik63KXX2Es"
        workbook = client.open_by_key(sheet_id)
        sheet = workbook.get_widget(gid=339189941) # Specific tab (gid) access

        # Saara data fetch karke search karna
        records = sheet.get_all_records()
        
        for row in records:
            # Sheet mein column ka naam 'Member ID' hona chahiye
            if str(row.get('Member ID', '')) == str(member_id):
                return row
        
        return None # Agar ID nahi mili

    except Exception as e:
        return {"error": str(e)}
