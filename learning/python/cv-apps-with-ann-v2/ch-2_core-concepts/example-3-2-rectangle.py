
import cv2
from consts import PATH_TO_IMG


def main():
    image = cv2.imread(PATH_TO_IMG)

    start_point = (30, 50)
    end_point = (230, 300)
    new_color_bgr = (0, 0, 255)
    thickness = 10

    cv2.rectangle(image, start_point, end_point, new_color_bgr, thickness)
    # cv2.imwrite("rect.png", image)

    cv2.imshow("Modified example...", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
