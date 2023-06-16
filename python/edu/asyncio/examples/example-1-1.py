import requests

TEST_URL = "https://www.google.com"


if __name__ == "__main__":
    print("Program started...")

    # io-bound
    resp = requests.get(TEST_URL)

    # cpu-bound
    headers = resp.headers.items()
    headers = ["{}: {}".format(item_id, item_val) for item_id, item_val in headers]
    output_data = "\n".join(headers)

    # cpu-bound
    with open("output.txt", "w") as f:
        f.write(output_data)

    print("Program finished...")
