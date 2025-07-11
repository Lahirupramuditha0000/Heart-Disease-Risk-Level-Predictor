from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Dynamically find the model file relative to main.py
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'heart_risk_prediction_regression_model.sav')
model = joblib.load(MODEL_PATH)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/getresults', methods=['POST'])
def getresults():
    try:
        result = request.form

        name = result['name']
        gender = float(result['gender'])
        age = float(result['age'])
        tc = float(result['tc'])
        hdl = float(result['hdl'])
        sbp = float(result['sbp'])
        smoke = float(result['smoke'])
        bpm = float(result['bpm'])
        diab = float(result['diab'])

        # Prepare input for prediction
        test_data = np.array([gender, age, tc, hdl, sbp, smoke, bpm, diab]).reshape(1, -1)
        prediction = model.predict(test_data)

        # You can define risk levels based on prediction value
        score = round(prediction[0], 2)
        if score < 0.3:
            risk_level = "🟢 Low Risk"
        elif score < 0.6:
            risk_level = "🟠 Moderate Risk"
        else:
            risk_level = "🔴 High Risk"

        resultDict = {
            "name": name,
            "risk": score,
            "level": risk_level
        }

        return render_template('results.html', results=resultDict)

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
