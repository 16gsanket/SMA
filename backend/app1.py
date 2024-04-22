from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Load the trained Isolation Forest model
model = joblib.load('isolation_forest_model.pkl')

# Define endpoint for anomaly detection
@app.route('/detect-anomalies', methods=['POST'])
def detect_anomalies():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        try:
            # Read CSV file
            df = pd.read_csv(file)

               # Read the CSV file into a DataFrame
            df = pd.read_csv(file, delimiter=';')
            
            # Extract relevant features from the dataset
            features = df[['like', 'share', 'comment']]  # Adjust this according to your dataset
            
            # Process the data (pass it through your trained model)
            result = model.predict(features)
            
            # Return the result
            return jsonify({'result': result.tolist()})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
