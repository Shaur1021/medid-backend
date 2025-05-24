from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "MedId backend is running!"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        prompt = data.get('prompt', '')

        # Simulate AI logic based on the prompt
        if "possible cases" in prompt:
            answer = "Possible cases: Common Cold, Flu, COVID-19"
        elif "more information about case" in prompt:
            answer = "Flu: lasts 5-7 days, treat with rest and fluids."
        elif "How urgent" in prompt:
            answer = "See a doctor if symptoms worsen or high fever persists."
        else:
            answer = "No data."

        return jsonify({"answer": answer})
    except Exception as e:
        print("Error in /ask:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on port 5000...")
    app.run(port=5000, debug=True)
