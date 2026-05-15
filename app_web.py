from flask import Flask, render_template, request, jsonify
from sheets_handler import get_member_data
from web_launcher import get_app_metadata
import os

app = Flask(__name__)

# Main route: Jab user browser me website kholega
@app.route('/')
def home():
    metadata = get_app_metadata()
    return render_template('index.html', metadata=metadata)

# API Route: Jab user Member ID submit karega
@app.route('/api/verify', methods=['POST'])
def verify_member():
    data = request.json
    member_id = data.get('member_id', '').strip()
    
    if not member_id:
        return jsonify({"success": False, "error": "Kripya Member ID dalein."})
    
    # Pehle se bani sheets_handler file se data fetch karna
    user_records = get_member_data(member_id)
    
    if user_records and "error" in user_records:
        return jsonify({"success": False, "error": user_records["error"]})
    elif user_records:
        # User ka data successfully mil gaya
        return jsonify({
            "success": True, 
            "name": user_records.get('Name', 'Member'),
            "age": user_records.get('Age', '20')
        })
    else:
        return jsonify({"success": False, "error": "Member ID nahi mili."})

if __name__ == '__main__':
    print("Herbalife Web Engine starting on http://127.0.0.1:5000/ ...")
    app.run(debug=True)
