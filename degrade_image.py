import cv2
import numpy as np
import sys

def apply_gaussian_noise(image, degradation_level):
    row, col, ch = image.shape
    mean = 0
    sigma = degradation_level
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    degraded_image = image + gauss
    degraded_image = np.clip(degraded_image, 0, 255)
    return degraded_image.astype(np.uint8)

def apply_blur(image, degradation_level):
    # Ensure the kernel size is an odd number
    kernel_size = degradation_level if degradation_level % 2 == 1 else degradation_level + 1
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def apply_pixelation(image, degradation_level):
    # Determine the size of each pixel block
    block_size = degradation_level

    # Resize the image to a smaller size
    small_image = cv2.resize(image, (image.shape[1] // block_size, image.shape[0] // block_size), interpolation=cv2.INTER_NEAREST)

    # Resize the small image back to the original size
    pixelated_image = cv2.resize(small_image, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)

    return pixelated_image

def degrade_image(image_path, degradation_level, degradation_type):
    try:
        # Load the image
        img = cv2.imread(image_path)

        if img is None:
            raise Exception("Unable to load the image. Check the file path and integrity.")

        if degradation_type == "gaussian":
            degraded_img = apply_gaussian_noise(img, degradation_level)
        elif degradation_type == "blur":
            degraded_img = apply_blur(img, degradation_level)
        elif degradation_type == "pixelate":
            degraded_img = apply_pixelation(img, degradation_level)
        else:
            raise ValueError("Unsupported degradation type. Use 'gaussian', 'blur', or 'pixelate'.")

        # Save the degraded image
        cv2.imwrite('degraded_image.jpg', degraded_img)
        print("The degraded image has been successfully saved.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <image_path> <degradation_level> <degradation_type>")
        sys.exit(1)

    image_path = sys.argv[1]
    degradation_level = int(sys.argv[2])
    degradation_type = sys.argv[3].lower()

    degrade_image(image_path, degradation_level, degradation_type)
