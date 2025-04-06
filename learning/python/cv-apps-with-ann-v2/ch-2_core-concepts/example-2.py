
import cv2
from consts import PATH_TO_IMG


def main():
    image = cv2.imread(PATH_TO_IMG)

    (b, g, r) = image[0, 0]
    print(f"BGR at point (0, 0): {b}/{g}/{r}")

    image[0:50, 0:50] = (0, 255, 0)

    cv2.imshow("Modified example...", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
