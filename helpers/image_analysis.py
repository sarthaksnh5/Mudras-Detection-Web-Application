from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import tensorflow as tf

# Load the trained model
model_path = '/media/sarthak/Projects/python/Tanvi Classes/webapp/helpers/few_hand.keras'
model = tf.keras.models.load_model(model_path)

mudras = ['Fist', 'Open Hand']

# helpers/image_analysis.py
def predict_single_image(img_path):
    # Load the image
    img = image.load_img(img_path, target_size=(150, 150))
    
    # Convert the image to an array
    img_array = image.img_to_array(img)
    
    # Expand the dimensions to match the input shape of the model (1, 150, 150, 3)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Preprocess the image
    img_array = preprocess_input(img_array)
    
    # Predict the class of the image
    prediction = model.predict(img_array)

    index = np.argmax(prediction)

    # Get the confidence value of the prediction
    confidence = prediction[0][index]
    
    # Check if the confidence is greater than 0.8
    if confidence > 0.8:
        # Replace this with the actual class label based on the index
        return mudras[index]
    else:
        return "Not Detected"    

def analyze_image(image_path):
    # Your model logic here
    return predict_single_image(image_path)

