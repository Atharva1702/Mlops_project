from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('urban_heat_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Get values from the form
        density = float(request.form['density'])
        green = float(request.form['green'])
        traffic = float(request.form['traffic'])
        water = float(request.form['water'])  
        temp = float(request.form['temp'])

        # 2. Arrange them in the EXACT order the model expects
        # Order: building_density, green_space, traffic_score, distance_to_water, avg_regional_temp
        final_features = np.array([[density, green, traffic, water, temp]])
        
        # 3. Predict
        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template('index.html', 
                               prediction_text=f'Predicted Heat Increase: {output}°C')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')
if __name__ == "__main__":
    app.run(debug=True)