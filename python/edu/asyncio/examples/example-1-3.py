import threading


def hello(name):
    thread = threading.current_thread()
    print(f"Hello, {name} from {thread}...")


if __name__ == "__main__":
    print("Program started...")

    my_name = "Fred"
    hello_thread = threading.Thread(target=hello, args=(my_name,))
    hello_thread.start()

    threads_count = threading.active_count()
    main_thread = threading.current_thread()

    print(f"Running {threads_count} threads...")
    print(f"Active thread: {main_thread.name}")
    print("Waiting sub-threads...")
    hello_thread.join()

    print("Program finished...")
