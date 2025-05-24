from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "MedId backend is running!"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        symptoms = data.get('symptoms', '')
        duration = data.get('duration', '')

        # Simulate AI logic based on the symptoms and duration
        possible_cases = ["Common Cold", "Flu", "COVID-19"]
        selected_case = possible_cases[1]  # For demo, pick "Flu"
        selected_case_details = "Flu: lasts 5-7 days, treat with rest and fluids."
        emergency_advice = "See a doctor if symptoms worsen or high fever persists."

        return jsonify({
            "possible_cases": possible_cases,
            "selected_case": selected_case,
            "selected_case_details": selected_case_details,
            "emergency_advice": emergency_advice
        })
    except Exception as e:
        print("Error in /ask:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on port 5000...")
    app.run(port=5000, debug=True)
