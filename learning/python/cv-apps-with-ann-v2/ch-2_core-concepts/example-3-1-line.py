
import cv2
from consts import PATH_TO_IMG


def main():
    image = cv2.imread(PATH_TO_IMG)

    start_point = (image.shape[1], 0)
    end_point = (0, image.shape[0])
    new_color_bgr = (0, 255, 0)
    thickness = 10

    cv2.line(image, start_point, end_point, new_color_bgr, thickness)

    cv2.imshow("Modified example...", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
