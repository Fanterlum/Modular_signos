import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def detect_highest_peaks(image_path, threshold=0.5):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Threshold the image to convert it to a binary image
    _, binary_image = cv2.threshold(image, 255 * threshold, 255, cv2.THRESH_BINARY)

    # Find the highest peaks in the image
    peaks, _ = find_peaks(-binary_image.flatten(), distance=image.shape[1] // 10)

    # Convert 1D peaks indices to 2D coordinates
    peak_coords = np.unravel_index(peaks, binary_image.shape)

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
    plt.title('Electrocardiogram with Detected Peaks')
    plt.xlabel('X Coordinate (column index)')
    plt.ylabel('Y Coordinate (row index)')
    plt.show()

# Example usage:
if __name__ == "__main__":
    image_path = "img/sin_Error.png"
    detected_peaks = detect_highest_peaks(image_path)

    print("Detected peaks coordinates:")
    for x, y in zip(detected_peaks[1], detected_peaks[0]):
        print(f"X: {x}, Y: {y}")

    # Plot the image with detected peaks
    plot_image_with_peaks(image_path, detected_peaks)
