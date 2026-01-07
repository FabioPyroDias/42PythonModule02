def garden_operations(error: int) -> None:
    if error == 0:
        print("Testing ValueError...")
        try:
            tmp = int('abc')
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
    elif error == 1:
        print("Testing ZeroDivisionError...")
        try:
            tmp = 1 / 0
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
    elif error == 2:
        print("Testing FileNotFoundError...")
        try:
            with open("missing.txt", "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'")
    elif error == 3:
        print("Testing KeyError...")
        try:
            dictionary = {}
            print(dictionary[r'missing\_plant'])
        except KeyError:
            print(r"Caught KeyError: 'missing\_plant'")
    else:
        print("Testing multiple errors together...")
        try:
            tmp = int('abc')
            tmp = 1 / 0
            print(tmp)
            with open("missing.txt", "r") as file:
                content = file.read()
                print(content)
            dictionary = {}
            print(dictionary[r'missing\_plant'])
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations(0)
    print()
    garden_operations(1)
    print()
    garden_operations(2)
    print()
    garden_operations(3)
    print()
    garden_operations(4)
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
