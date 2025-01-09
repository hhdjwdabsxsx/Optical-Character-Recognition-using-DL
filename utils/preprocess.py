from tensorflow.keras.preprocessing import image
import numpy as np

def preprocess_image(image_path, target_size=(32, 32)):
    img = image.load_img(image_path, target_size=target_size, color_mode="grayscale")
    img_array = image.img_to_array(img)
    
    # Convert grayscale (1 channel) to RGB (3 channels)
    img_array = np.repeat(img_array, 3, axis=-1)
    
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize to [0, 1]
    return img_array
