def garden_operations(option: int) -> None:
    if option == 0:
        try:
            int("abc")
        except ValueError:
            return "Caught ValueError: invalid literal for int()"
    elif option == 1:
        try:
            test = 1 / 0
        except ZeroDivisionError:
            return "Caught ZeroDivisionError: division by zero"
    elif option == 2:
        try:
            open("missing.txt")
        except FileNotFoundError:
            return "Caught FileNotFoundError: No such file 'missing.txt'"
    elif option == 3:
        try:
            test = {}
            test["missing\\_plant"]
        except KeyError:
            return "Caught KeyError: 'missing\\_plant'"
    else:
        try:
            int("abc")
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            return "Caught an error, but program continues!"


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()
    print("Testing ValueError...")
    print(garden_operations(0))
    print()
    print("Testing ZeroDivisionError...")
    print(garden_operations(1))
    print()
    print("Testing FileNotFoundError...")
    print(garden_operations(2))
    print()
    print("Testing KeyError..")
    print(garden_operations(3))
    print()
    print("Testing multiple errors together...")
    print(garden_operations(4))
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
