import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def detect_highest_peaks(image_path, threshold=0.5, num_peaks=7, prominence=100, distance=None, y_range=(0, 100)):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Crop the image to the specified Y range
    y_min, y_max = y_range
    image = image[y_min:y_max, :]

    # Threshold the image to convert it to a binary image
    _, binary_image = cv2.threshold(image, 255 * threshold, 255, cv2.THRESH_BINARY)

    # Find the peaks in the image using scipy.signal.find_peaks
    peaks, _ = find_peaks(-binary_image.flatten(), height=-prominence, distance=distance)

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
    plt.title('Electrocardiogram with Detected Highest Peaks')
    plt.xlabel('X Coordinate (column index)')
    plt.ylabel('Y Coordinate (row index)')
    plt.show()

# Example usage:
if __name__ == "__main__":
    image_path = "picture2.jpeg"
    detected_peaks = detect_highest_peaks(image_path, num_peaks=7, prominence=200, distance=100, y_range=(0, 100))

    print("Detected highest peaks coordinates:")
    for peak in zip(detected_peaks[1], detected_peaks[0]):
        print(f"X: {peak[0]}, Y: {peak[1]}")

    # Plot the image with detected highest peaks
    plot_image_with_peaks(image_path, detected_peaks)
