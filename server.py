import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)

# Get allowed origin from environment variable
allowed_origin = os.environ.get("DEEPSEEK_KEY", "*")
CORS(app, origins=[allowed_origin])

@app.route('/')
def home():
    return "MedId backend is running!"

@app.route('/ask', methods=['POST'])


@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        symptoms = data.get('symptoms', '').lower()
        duration = data.get('duration', '').lower()

        # Prepare payload for DeepSeek
        deepseek_payload = {
            "symptoms": symptoms,
            "duration": duration
        }

        # Get DeepSeek API URL and KEY from environment variables
        deepseek_url = os.environ.get("DEEPSEEK_API_URL")
        deepseek_key = os.environ.get("DEEPSEEK_API_KEY")

        if not deepseek_url or not deepseek_key:
            return jsonify({"error": "DeepSeek API URL or KEY not set"}), 500

        headers = {
            "Authorization": f"Bearer {deepseek_key}",
            "Content-Type": "application/json"
        }

        # Send request to DeepSeek
        resp = requests.post(deepseek_url, json=deepseek_payload, headers=headers, timeout=15)
        if resp.status_code != 200:
            return jsonify({"error": "DeepSeek API error", "details": resp.text}), 500

        # Expect DeepSeek to return a list of results with the required fields
        deepseek_results = resp.json().get("results", [])

        # Remove duplicates if needed
        unique = []
        seen = set()
        for r in deepseek_results:
            key = (r.get("selected_case"), r.get("selected_case_details"))
            if key not in seen:
                unique.append(r)
                seen.add(key)

        if not unique:
            unique.append({
                "possible_cases": ["Unknown"],
                "selected_case": "Unknown",
                "selected_case_details": "Not enough information.",
                "emergency_advice": "Consult a healthcare professional."
            })

        return jsonify({"results": unique})

    except Exception as e:
        print("Error in /ask:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on port 5000...")
    app.run(port=5000, debug=True)
