import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_highest_peak(image_path, threshold=0.5):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Threshold the image to convert it to a binary image
    _, binary_image = cv2.threshold(image, 255 * threshold, 255, cv2.THRESH_BINARY)

    # Find the index of the highest peak in the image
    highest_peak_index = np.argmax(-binary_image.flatten())

    # Convert 1D index to 2D coordinates
    highest_peak_coord = np.unravel_index(highest_peak_index, binary_image.shape)

    return highest_peak_coord

def plot_image_with_peak(image_path, peak_coord):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Convert BGR image to RGB (Matplotlib expects RGB format)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a scatter plot to show the detected peak
    plt.figure()
    plt.imshow(image_rgb)
    plt.scatter(peak_coord[1], peak_coord[0], c='red', marker='x', s=50)
    plt.title('Electrocardiogram with Highest Peak')
    plt.xlabel('X Coordinate (column index)')
    plt.ylabel('Y Coordinate (row index)')
    plt.show()

# Example usage:
if __name__ == "__main__":
    image_path = "picture2.jpeg"
    highest_peak_coord = detect_highest_peak(image_path)

    print("Coordinates of the highest peak:")
    print(f"X: {highest_peak_coord[1]}, Y: {highest_peak_coord[0]}")

    # Plot the image with the highest peak
    plot_image_with_peak(image_path, highest_peak_coord)
