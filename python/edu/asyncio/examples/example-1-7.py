import requests
import time


def do_request(url: str) -> None:
    print(f"Read data from {url}...")
    response = requests.get(url)
    print(response.status_code)


if __name__ == "__main__":
    print("Program started...")

    start_time = time.time()

    do_request("https://www.google.com")
    do_request("https://www.google.com")

    end_time = time.time()
    print(f"Execution time - {end_time-start_time:.3f}s...")

    print("Program finished...")
