import os
import threading


if __name__ == "__main__":
    print("Program started...")

    print(f"Started process with ID: {os.getpid()}...")

    threads_count = threading.active_count()
    main_thread = threading.current_thread()

    print(f"Running {threads_count} threads...")
    print(f"Active thread: {main_thread.name}")

    print("Program finished...")
