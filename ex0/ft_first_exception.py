def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
        if temp >= 0 and temp <= 40:
            return f"Temperature {temp}°C is perfect for plants!"
        if temp < 0:
            return f"Error: {temp}°C is too cold for plants (min 0°C)"
        else:
            return f"Error: {temp}°C is too hot for plants (max 40°C)"
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    print("Testing temperature: 25")
    print(check_temperature(25))
    print()
    print("Testing temperature: abc")
    print(check_temperature("abc"))
    print()
    print("Testing temperature: 100")
    print(check_temperature(100))
    print()
    print("Testing temperature: -50")
    print(check_temperature(-50))
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
