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


def fibo_without_threading():
    calc_fibo(10)
    calc_fibo(11)


if __name__ == "__main__":
    print("Program started...")

    start_time = time.time()
    fibo_without_threading()
    end_time = time.time()

    print(f"Program execution time {end_time - start_time:3f}s...")
    print("Program finished...")
