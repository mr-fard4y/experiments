
import cv2
import numpy as np


IMAGE_SIZE = (400, 400, 3)


def main():
    image = np.zeros(IMAGE_SIZE, dtype="uint8")

    center_point = (200, 200)
    radius = 80
    new_color_bgr = (0, 0, 255)
    thickness = 5

    cv2.circle(image, center_point, radius, new_color_bgr, thickness)
    # cv2.imwrite("rect.png", image)

    cv2.imshow("Modified example...", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
