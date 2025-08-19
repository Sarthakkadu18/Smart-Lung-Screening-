import os
import numpy as np
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import tensorflow as tf

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"

# --- Model Loading ---
# Define the path to the trained model
MODEL_PATH = '../model_training/lung_cancer_model.h5'

# Load the trained model
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# --- Image Preprocessing ---
def preprocess_image(image_path, target_size=(224, 224)):
    """
    Preprocesses an image for model prediction.
    """
    try:
        img = Image.open(image_path)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img = img.resize(target_size)
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize to [0, 1]
        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

# --- Flask Routes ---
@app.route('/', methods=['GET'])
def index():
    """Renders the main page with the upload form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the image upload and prediction."""
    if model is None:
        flash('Model is not loaded. Please check server logs.', 'danger')
        return redirect(url_for('index'))

    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        upload_folder = os.path.join('static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        processed_image = preprocess_image(filepath)
        if processed_image is not None:
            prediction = model.predict(processed_image)
            probability = prediction[0][0]
            
            if probability > 0.5:
                result = "Cancerous"
                confidence = f"{probability * 100:.2f}%"
            else:
                result = "Non-Cancerous"
                confidence = f"{(1 - probability) * 100:.2f}%"

            return render_template('index.html', prediction=result, confidence=confidence, image_path=filepath)
        else:
            flash('Error processing the image.', 'danger')
            return redirect(url_for('index'))

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)