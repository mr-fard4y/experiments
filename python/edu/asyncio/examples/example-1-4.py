import multiprocessing
import os


def print_by_process():
    print(f"Hello by process in {os.getpid()}...")


if __name__ == "__main__":
    print("Program started...")

    process = multiprocessing.Process(target=print_by_process)
    process.start()

    print(f"Main process {os.getpid()}...")
    process.join()
    print("Program finished...")
