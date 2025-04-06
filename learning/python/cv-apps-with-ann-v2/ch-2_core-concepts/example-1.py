
import cv2
from consts import PATH_TO_IMG


def main():
    image = cv2.imread(PATH_TO_IMG)

    print(f"Dimension: {image.ndim}")
    print(f"Height: {image.shape[0]}")
    print(f"Width: {image.shape[1]}")
    print(f"Channels: {image.shape[2]}")
    print(f"Size: {image.size}")

    cv2.imshow("Example...", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()
