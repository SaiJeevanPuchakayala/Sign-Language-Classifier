import gradio as gr
from tensorflow.keras.models import load_model
import numpy as np

# Model saved with Keras model.save()
MODEL_PATH = 'realistic_model.h5'

class_names = ['0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] # categories


def model_predict(image):
    img = image.reshape((-1, 64, 64, 3))
    # Load your trained model
    model = load_model(MODEL_PATH)
    result = model.predict(img).flatten()
    return {class_names[i]: float(result[i]) for i in range(36)}


image = gr.inputs.Image(shape = (64, 64)) # initializing the input component
label = gr.outputs.Label(num_top_classes = 1) # initializing the output component


sample_images = [["./sample_images/1.jpeg"],["./sample_images/5.jpeg"],["./sample_images/8.jpeg"],["./sample_images/c.jpg"],["./sample_images/l.jpeg"],["./sample_images/m.jpeg"],["./sample_images/p.jpg"],["./sample_images/i.jpeg"]]

# launching the interface
gr.Interface([model_predict], inputs = image,outputs = label ,capture_session = True, examples = sample_images, title="Sign Language Classifier", description="Demo for Sign Language Classifier. To use it, simply upload A picture, or click one of the examples from below to load them.", theme = 'darkdefault',).launch()

# To create a public link, set `share=True` in `launch()`