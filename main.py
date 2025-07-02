def main():
    with open("data.txt", "r") as f:
        data = f.read()

    transformed = data.upper()

    with open("output.txt", "w") as f:
        f.write(transformed)

    print("Successfully transformed data!")

if __name__ == "__main__":
    main()
