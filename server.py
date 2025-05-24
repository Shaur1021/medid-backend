from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=["chrome-extension://cemkbgmnnmnalagobjeiohcaldkjjemc"])


CORS(app)  # Enable CORS for extension use

@app.route('/')
def home():
    return "MedId backend is running!"

from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=["chrome-extension://cemkbgmnnmnalagobjeiohcaldkjjemc"])


CORS(app)  # Enable CORS for extension use

@app.route('/')
def home():
    return "MedId backend is running!"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        symptoms = data.get('symptoms', '').lower()
        duration = data.get('duration', '').lower()

        results = []

        # Each block checks for a symptom and appends a result if matched
        if "cough" in symptoms and "fever" in symptoms:
                results.append({
                "possible_cases": ["Flu", "COVID-19", "Common Cold"],
                "selected_case": "Flu",
                "selected_case_details": "Flu: lasts 5-7 days, treat with rest and fluids.",
                "emergency_advice": "See a doctor if symptoms worsen or high fever persists."
                })
        if "fever" in symptoms:
            results.append({
            "possible_cases": ["Flu", "COVID-19", "Infection"],
            "selected_case": "Flu",
            "selected_case_details": "Flu: lasts 5-7 days, treat with rest and fluids.",
            "emergency_advice": "See a doctor if fever is high or lasts more than 3 days."
            })
        if "runny nose" in symptoms or "sneezing" in symptoms:
            results.append({
                "possible_cases": ["Common Cold", "Allergy"],
                "selected_case": "Common Cold",
                "selected_case_details": "Common Cold: lasts 3-7 days, rest and fluids recommended.",
                "emergency_advice": "Usually not urgent, but see a doctor if symptoms persist."
            })
        if "headache" in symptoms and "nausea" in symptoms:
            results.append({
                "possible_cases": ["Migraine", "Flu"],
                "selected_case": "Migraine",
                "selected_case_details": "Migraine: can last hours to days, treat with rest and medication.",
                "emergency_advice": "See a doctor if headaches are severe or frequent."
            })
        if "chest pain" in symptoms:
            results.append({
                "possible_cases": ["Heart Attack", "Anxiety", "Muscle Strain"],
                "selected_case": "Heart Attack",
                "selected_case_details": "Heart Attack: chest pain, shortness of breath, call 911 immediately.",
                "emergency_advice": "Call 911 or emergency services immediately."
            })
        if "rash" in symptoms:
            results.append({
                "possible_cases": ["Allergy", "Chickenpox", "Measles"],
                "selected_case": "Allergy",
                "selected_case_details": "Allergy: treat with antihistamines, see a doctor if severe.",
                "emergency_advice": "See a doctor if rash is widespread or with other symptoms."
            })
        if "vomiting" in symptoms and "diarrhea" in symptoms:
            results.append({
                "possible_cases": ["Stomach Flu", "Food Poisoning"],
                "selected_case": "Stomach Flu",
                "selected_case_details": "Stomach Flu: lasts 1-3 days, stay hydrated.",
                "emergency_advice": "See a doctor if unable to keep fluids down."
            })
        if "shortness of breath" in symptoms:
            results.append({
                "possible_cases": ["Asthma", "COVID-19", "Pneumonia"],
                "selected_case": "Asthma",
                "selected_case_details": "Asthma: use inhaler, seek medical help if severe.",
                "emergency_advice": "Seek immediate help if breathing is difficult."
            })
        if "joint pain" in symptoms:
            results.append({
                "possible_cases": ["Arthritis", "Lyme Disease", "Injury"],
                "selected_case": "Arthritis",
                "selected_case_details": "Arthritis: chronic, managed with medication and therapy.",
                "emergency_advice": "See a doctor for persistent joint pain."
            })
        if "abdominal pain" in symptoms:
            results.append({
                "possible_cases": ["Appendicitis", "Indigestion", "Gallstones"],
                "selected_case": "Appendicitis",
                "selected_case_details": "Appendicitis: sudden pain, may require surgery.",
                "emergency_advice": "Seek emergency care if pain is severe or with fever."
            })
        if "dizziness" in symptoms:
            results.append({
                "possible_cases": ["Dehydration", "Low Blood Pressure", "Ear Infection"],
                "selected_case": "Dehydration",
                "selected_case_details": "Dehydration: drink fluids, rest.",
                "emergency_advice": "See a doctor if dizziness persists or is severe."
            })
        if "back pain" in symptoms:
            results.append({
                "possible_cases": ["Muscle Strain", "Kidney Infection", "Herniated Disc"],
                "selected_case": "Muscle Strain",
                "selected_case_details": "Muscle Strain: rest, gentle stretching, pain relief.",
                "emergency_advice": "See a doctor if pain is severe or with other symptoms."
            })
        if "sore throat" in symptoms:
            results.append({
                "possible_cases": ["Strep Throat", "Common Cold", "Allergy"],
                "selected_case": "Strep Throat",
                "selected_case_details": "Strep Throat: bacterial, may need antibiotics.",
                "emergency_advice": "See a doctor if sore throat is severe or lasts more than a week."
            })
        if "blurred vision" in symptoms:
            results.append({
                "possible_cases": ["Migraine", "Diabetes", "Eye Infection"],
                "selected_case": "Migraine",
                "selected_case_details": "Migraine: can cause visual disturbances, rest in a dark room.",
                "emergency_advice": "See a doctor if vision changes suddenly."
            })
        if "swelling" in symptoms:
            results.append({
                "possible_cases": ["Injury", "Infection", "Allergic Reaction"],
                "selected_case": "Injury",
                "selected_case_details": "Injury: rest, ice, compression, elevation.",
                "emergency_advice": "See a doctor if swelling is severe or with other symptoms."
            })
        if "palpitations" in symptoms:
            results.append({
                "possible_cases": ["Anxiety", "Arrhythmia", "Caffeine Overuse"],
                "selected_case": "Arrhythmia",
                "selected_case_details": "Arrhythmia: irregular heartbeat, may need ECG.",
                "emergency_advice": "See a doctor if palpitations are frequent or with chest pain."
            })
        if "weight loss" in symptoms:
            results.append({
                "possible_cases": ["Thyroid Disorder", "Diabetes", "Cancer"],
                "selected_case": "Thyroid Disorder",
                "selected_case_details": "Thyroid Disorder: affects metabolism, blood tests needed.",
                "emergency_advice": "See a doctor for unexplained weight loss."
            })
        if "night sweats" in symptoms:
            results.append({
                "possible_cases": ["Tuberculosis", "Menopause", "Lymphoma"],
                "selected_case": "Tuberculosis",
                "selected_case_details": "Tuberculosis: infectious, needs antibiotics.",
                "emergency_advice": "See a doctor for persistent night sweats."
            })
        if "fatigue" in symptoms:
            results.append({
                "possible_cases": ["Anemia", "Sleep Apnea", "Depression"],
                "selected_case": "Anemia",
                "selected_case_details": "Anemia: low red blood cells, treat with iron and diet.",
                "emergency_advice": "See a doctor if fatigue is persistent."
            })
        if "ear pain" in symptoms:
            results.append({
                "possible_cases": ["Ear Infection", "TMJ Disorder", "Foreign Body"],
                "selected_case": "Ear Infection",
                "selected_case_details": "Ear Infection: pain, possible fever, may need antibiotics.",
                "emergency_advice": "See a doctor if pain is severe or with hearing loss."
            })
        if "frequent urination" in symptoms:
            results.append({
                "possible_cases": ["Urinary Tract Infection", "Diabetes", "Pregnancy"],
                "selected_case": "Urinary Tract Infection",
                "selected_case_details": "UTI: burning sensation, may need antibiotics.",
                "emergency_advice": "See a doctor if symptoms persist."
            })
        if "yellow skin" in symptoms or "jaundice" in symptoms:
            results.append({
                "possible_cases": ["Hepatitis", "Gallstones", "Liver Disease"],
                "selected_case": "Hepatitis",
                "selected_case_details": "Hepatitis: inflammation of the liver, may need antiviral treatment.",
                "emergency_advice": "See a doctor promptly for jaundice."
            })
        if "leg swelling" in symptoms:
            results.append({
                "possible_cases": ["Heart Failure", "Deep Vein Thrombosis", "Kidney Disease"],
                "selected_case": "Deep Vein Thrombosis",
                "selected_case_details": "DVT: blood clot in leg, can be life-threatening.",
                "emergency_advice": "Seek emergency care for sudden leg swelling."
            })
        if "memory loss" in symptoms:
            results.append({
                "possible_cases": ["Dementia", "Alzheimer's Disease", "Vitamin Deficiency"],
                "selected_case": "Dementia",
                "selected_case_details": "Dementia: progressive memory loss, see a neurologist.",
                "emergency_advice": "See a doctor for evaluation."
            })
        if "bloody stool" in symptoms:
            results.append({
                "possible_cases": ["Hemorrhoids", "Colon Cancer", "Gastrointestinal Bleed"],
                "selected_case": "Gastrointestinal Bleed",
                "selected_case_details": "GI Bleed: can be serious, may need urgent care.",
                "emergency_advice": "Seek immediate medical attention."
            })
        if "persistent cough" in symptoms:
            results.append({
                "possible_cases": ["Tuberculosis", "Lung Cancer", "Asthma"],
                "selected_case": "Tuberculosis",
                "selected_case_details": "Tuberculosis: infectious, needs antibiotics.",
                "emergency_advice": "See a doctor for persistent cough."
            })
        if "difficulty swallowing" in symptoms:
            results.append({
                "possible_cases": ["Throat Infection", "Esophageal Cancer", "Acid Reflux"],
                "selected_case": "Throat Infection",
                "selected_case_details": "Throat Infection: may need antibiotics or further tests.",
                "emergency_advice": "See a doctor if swallowing is difficult."
            })
        if "numbness" in symptoms:
            results.append({
                "possible_cases": ["Stroke", "Nerve Compression", "Multiple Sclerosis"],
                "selected_case": "Stroke",
                "selected_case_details": "Stroke: sudden numbness, weakness, call 911 immediately.",
                "emergency_advice": "Call 911 or emergency services immediately."
            })
        if "double vision" in symptoms:
            results.append({
                "possible_cases": ["Stroke", "Brain Tumor", "Eye Muscle Problem"],
                "selected_case": "Eye Muscle Problem",
                "selected_case_details": "Eye Muscle Problem: may need eye specialist evaluation.",
                "emergency_advice": "See a doctor promptly for double vision."
            })
        if "blood in urine" in symptoms:
            results.append({
                "possible_cases": ["Urinary Tract Infection", "Kidney Stones", "Bladder Cancer"],
                "selected_case": "Kidney Stones",
                "selected_case_details": "Kidney Stones: can cause pain and blood in urine.",
                "emergency_advice": "See a doctor for blood in urine."
            })
        if "severe thirst" in symptoms:
            results.append({
                "possible_cases": ["Diabetes", "Dehydration", "Kidney Disease"],
                "selected_case": "Diabetes",
                "selected_case_details": "Diabetes: high blood sugar, needs blood tests and treatment.",
                "emergency_advice": "See a doctor for persistent severe thirst."
            })

        # If no matches, return a default response
        if not results:
            results.append({
                "possible_cases": ["Unknown"],
                "selected_case": "Unknown",
                "selected_case_details": "Not enough information.",
                "emergency_advice": "Consult a healthcare professional."
            })

        unique = []
        seen = set()
        for r in results:
            key = (r["selected_case"], r["selected_case_details"])
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
