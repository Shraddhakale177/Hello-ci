def hello(name: str = "world") -> str:
    message = f"Hallo, {name}!"
    return message


def main() -> None:
    result = hello()
    print(result)


if __name__ == "__main__":
    main()
