from flask import Flask, request, jsonify
from flask_cors import CORS  # Isse aap apni kisi bhi website se isko connect kar sakte hain
from sheets_handler import get_member_data
from diet_analyzer import DietAnalyzer
import os

app = Flask(__name__)
CORS(app) # Cross-Origin Resource Sharing active kiya taaki aapki main website isse block na kare

@app.route('/api/v1/verify-member', methods=['POST'])
def verify_member_endpoint():
    data = request.json or {}
    member_id = data.get('member_id', '').strip()
    
    if not member_id:
        return jsonify({"success": False, "message": "Member ID missing!"}), 400
        
    # File 2 (sheets_handler.py) se data lana
    user_data = get_member_data(member_id)
    
    if user_data and "error" in user_data:
        return jsonify({"success": False, "message": user_data["error"]}), 500
    elif user_data:
        # Check if child or adult
        age = int(user_data.get('Age', 20))
        is_child = True if age < 15 else False
        
        return jsonify({
            "success": True,
            "data": {
                "name": user_data.get('Name', 'Member'),
                "age": age,
                "is_child": is_child,
                "status": "Active"
            }
        })
    else:
        return jsonify({"success": False, "message": "Member ID not found in Google Sheets."}), 404

if __name__ == '__main__':
    # Production ready cross-origin hosting configuration
    print("Herbalife API Gateway Online. Ready to connect with your website...")
    app.run(host='0.0.0.0', port=5000, debug=True)
