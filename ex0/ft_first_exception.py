def check_temperature(temp_str) -> int:
    """"""
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print()
    print("Testing temperature: 25")
    check_temperature(25)
    print()
    print("Testing temperature: abc")
    check_temperature('abc')
    print()
    print("Testing temperature: 100")
    check_temperature(100)
    print()
    print("Testing temperature: -50")
    check_temperature(-50)
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
