
import cv2
import numpy as np


IMAGE_SIZE = (300, 300, 3)


def main():
    image = np.zeros(IMAGE_SIZE, dtype="uint8")

    start_point = (20, 20)
    end_point = (200, 200)
    new_color_bgr = (255, 0, 0)
    thickness = 10
    # thickness = -1

    cv2.rectangle(image, start_point, end_point, new_color_bgr, thickness)
    # cv2.imwrite("rect-new.png", image)

    cv2.imshow("Modified example...", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
