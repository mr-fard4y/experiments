import requests
import threading
import time


def do_request(url: str) -> None:
    print(f"Read data from {url}...")
    response = requests.get(url)
    print(response.status_code)


if __name__ == "__main__":
    print("Program started...")

    start_time = time.time()

    thread_1 = threading.Thread(target=do_request, args=("https://www.google.com",))
    thread_2 = threading.Thread(target=do_request, args=("https://www.google.com",))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    end_time = time.time()
    print(f"Execution time - {end_time-start_time:.3f}s...")

    print("Program finished...")
