import numpy as np
from utils.postprocess import decode_output

# Test case for decode_output
if __name__ == "__main__":
    # Define a dummy prediction for testing
    dummy_prediction = np.array([[[0.1, 0.2, 0.7], [0.8, 0.1, 0.1], [0.1, 0.9, 0.0]]])  # Example probabilities
    
    # Expected character set (same as defined in decode_output)
    characters = "abc"  # Adjust this based on your decode_output function
    
    # Call decode_output and print the result
    decoded_text = decode_output(dummy_prediction)
    print("Decoded text:", decoded_text)  # Expected output: "cab"
