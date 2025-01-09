from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import numpy as np
from tensorflow.keras.models import load_model
from utils.preprocess import preprocess_image
from utils.postprocess import decode_output

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the pre-trained model
model = load_model('model/VGG19_model.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess the image
        processed_image = preprocess_image(filepath)

        # Perform OCR prediction
        prediction = model.predict(processed_image)
        print("Raw prediction output:", prediction)  # Debugging the raw output

        # Decode the prediction into readable text
        decoded_text = decode_output(prediction)
        print("Decoded text:", decoded_text)  # Debugging the decoded text

        return render_template('result.html', text=decoded_text, image_path=filename)


if __name__ == '__main__':
    app.run(debug=True)