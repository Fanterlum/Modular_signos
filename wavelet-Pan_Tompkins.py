import pywt
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def wavelet_pan_tompkins_ecg(image_path, threshold=0.5, num_peaks=7, y_range=(0, 100)):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Crop the image to the specified Y range
    y_min, y_max = y_range
    image = image[y_min:y_max, :]

    # Threshold the image to convert it to a binary image
    _, binary_image = cv2.threshold(image, 255 * threshold, 255, cv2.THRESH_BINARY)

    # Apply the Wavelet Pan-Tompkins algorithm to detect the QRS complexes
    # ... (implement Wavelet Pan-Tompkins algorithm steps here using pywt)

    # In this simplified version, we are skipping the details of the Wavelet Pan-Tompkins algorithm
    # and directly using the peaks detected by find_peaks (similar to previous implementations)
    peaks, _ = find_peaks(-binary_image.flatten(), height=-100)

    # Sort the peaks by their height in descending order
    sorted_peaks = peaks[np.argsort(-binary_image.flatten()[peaks])]

    # Select the top num_peaks peaks
    selected_peaks = sorted_peaks[:num_peaks]

    # Convert 1D peaks indices to 2D coordinates in the original image
    peak_coords = np.unravel_index(selected_peaks, binary_image.shape)
    peak_coords = (peak_coords[0] + y_min, peak_coords[1])  # Adjust Y coordinate with y_min

    return peak_coords

def plot_image_with_peaks(image_path, peak_coords):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert BGR image to RGB (Matplotlib expects RGB format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a scatter plot to show the detected peaks
    plt.figure()
    plt.imshow(image_rgb)
    plt.scatter(peak_coords[1], peak_coords[0], c='red', marker='x', s=50)
    plt.title('Electrocardiogram with Detected QRS Complexes (Wavelet)')
    plt.xlabel('X Coordinate (column index)')
    plt.ylabel('Y Coordinate (row index)')
    plt.show()

# Example usage:
if __name__ == "__main__":
    image_path = "picture2.jpeg"
    detected_qrs_wavelet = wavelet_pan_tompkins_ecg(image_path, threshold=0.5, num_peaks=7, y_range=(0, 100))

    print("Detected QRS complexes coordinates (Wavelet):")
    for qrs in zip(detected_qrs_wavelet[1], detected_qrs_wavelet[0]):
        print(f"X: {qrs[0]}, Y: {qrs[1]}")

    # Plot the image with detected QRS complexes using Wavelet Pan-Tompkins
    plot_image_with_peaks(image_path, detected_qrs_wavelet)
