import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template
from sklearn.decomposition import PCA

# Create Flask app
app = Flask(__name__)

# Load your model and PCA object
import os

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
pca_path = os.path.join(os.path.dirname(__file__), 'pca.pkl')

model = pickle.load(open(model_path, 'rb'))
pca = pickle.load(open(pca_path, 'rb'))
# Route the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route the predict URL
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        # Extract features from form input
        iFeatures = [float(data) for data in request.form.values()]
        iFeatures = np.array(iFeatures).reshape(1, -1)  # Ensure input is a 2D array
        
        # Transform input features using the pre-fitted PCA
        input_transformed = pca.transform(iFeatures)
        
        # Predict using the loaded model
        prediction = model.predict(input_transformed)

        if prediction[0] == 0.0:
            prediction_text = "The person is most likely to pay off the loan."
        elif prediction[0] == 1.0:
            prediction_text = "The person is not likely to repay the loan."
        else:
            prediction_text = "The prediction result is unclear."

        return render_template(
            'index.html',
            prediction_text=prediction_text
        )
    except Exception as e:
        
        return render_template(
            'index.html',
            prediction_text=f"An error occurred: {e}"
        )

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode in production
