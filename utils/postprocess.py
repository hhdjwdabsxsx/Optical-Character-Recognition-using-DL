import numpy as np

def decode_output(prediction):
    # Define the character set (update this based on your model's training)
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Decode the predicted indices into characters
    decoded_text = ""
    for prob in prediction[0]:  # Assuming prediction[0] is a sequence of probabilities
        char_index = np.argmax(prob)  # Get the index of the max probability
        if char_index < len(characters):  # Ensure index is within bounds
            decoded_text += characters[char_index]
        else:
            decoded_text += "?"  # Add a placeholder for unrecognized characters
    return decoded_text


