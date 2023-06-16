import threading
import time


def calc_fibo(number: int) -> None:
    def fibo(n: int) -> int:
        if n == 1 or n == 0:
            return 0
        if n == 2:
            return 1
        return fibo(n - 1) + fibo(n - 2)

    print(f"Starting calc fibo for {number}...")
    fibo_data = fibo(number)
    print(f"Fibo for {number} is {fibo_data}...")


def fibo_with_threading():
    thread_fibo_1 = threading.Thread(target=calc_fibo, args=(10,))
    thread_fibo_2 = threading.Thread(target=calc_fibo, args=(11,))

    thread_fibo_1.start()
    thread_fibo_2.start()
    thread_fibo_1.join()
    thread_fibo_2.join()


if __name__ == "__main__":
    print("Program started...")

    start_time = time.time()
    fibo_with_threading()
    end_time = time.time()

    print(f"Program execution time {end_time - start_time:3f}s...")
    print("Program finished...")
