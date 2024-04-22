from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load the trained Isolation Forest model
model = joblib.load('isolation_forest_model.pkl')

# Define endpoint for anomaly detection
@app.route('/detect-anomalies', methods=['POST'])
def detect_anomalies():
    # Get the data from the request
    data = request.json
    
    # Process the data (you can pass it through your trained model)
    # Here you'll need to adapt this part according to how your model is used
    
    # For example, if your model expects a certain format of input data:
    # result = model.predict(data)
    
    # Return the result
    return jsonify({'result': 'anomaly detection result'})

if __name__ == '__main__':
    app.run(debug=True)
