from __future__ import division, print_function
import os
import numpy as np

# Keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename



# Define a flask app
app = Flask(__name__)



# Model saved with Keras model.save()
MODEL_PATH = 'realistic_model.h5'



# Load your trained model
model = load_model(MODEL_PATH)



def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(64, 64))
    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = np.vstack([x])
    result = model.predict(x)

    if result[0][0] == 1:
        prediction = '0'
    elif result[0][1] == 1:
        prediction = '1'
    elif result[0][2] == 1:
        prediction = '2'
    elif result[0][3] == 1:
        prediction = '3'
    elif result[0][4] == 1:
        prediction = '4'
    elif result[0][5] == 1:
        prediction = '5'
    elif result[0][6] == 1:
        prediction = '6'
    elif result[0][7] == 1:
        prediction = '7'
    elif result[0][8] == 1:
        prediction = '8'
    elif result[0][9] == 1:
        prediction = '9'
    elif result[0][10] == 1:
        prediction = 'A'
    elif result[0][11] == 1:
        prediction = 'B'
    elif result[0][12] == 1:
        prediction = 'C'
    elif result[0][13] == 1:
        prediction = 'D'
    elif result[0][14] == 1:
        prediction = 'E'
    elif result[0][15] == 1:
        prediction = 'F'
    elif result[0][16] == 1:
        prediction = 'G'
    elif result[0][17] == 1:
        prediction = 'H'
    elif result[0][18] == 1:
        prediction = 'I'
    elif result[0][19] == 1:
        prediction = 'J'
    elif result[0][20] == 1:
        prediction = 'K'
    elif result[0][21] == 1:
        prediction = 'L'
    elif result[0][22] == 1:
        prediction = 'M'
    elif result[0][23] == 1:
        prediction = 'N'
    elif result[0][24] == 1:
        prediction = 'O'
    elif result[0][25] == 1:
        prediction = 'P'
    elif result[0][26] == 1:
        prediction = 'Q'
    elif result[0][27] == 1:
        prediction = 'R'
    elif result[0][28] == 1:
        prediction = 'S'
    elif result[0][29] == 1:
        prediction = 'T'
    elif result[0][30] == 1:
        prediction = 'U'
    elif result[0][31] == 1:
        prediction = 'V'
    elif result[0][32] == 1:
        prediction = 'W'
    elif result[0][33] == 1:
        prediction = 'X'
    elif result[0][34] == 1:
        prediction = 'Y'
    elif result[0][35] == 1:
        prediction = 'Z'
        
    else:
        prediction = "XXXXXXXX"

    return prediction


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')



@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        return preds
    return None


if __name__ == '__main__':
    app.run(debug=True)