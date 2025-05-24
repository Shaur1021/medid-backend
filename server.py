from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DEEPSEEK_API_KEY = "sk-91a312fb7ff044dba097c376f9950b44"  # Replace with your DeepSeek API key

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        prompt = data.get('prompt', '')

        # DeepSeek API endpoint and headers
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",  # Or another model name if needed
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        answer = response.json()['choices'][0]['message']['content']
        return jsonify({"answer": answer})
    except Exception as e:
        print("Error in /ask:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on port 5000...")
    app.run(port=5000, debug=True)