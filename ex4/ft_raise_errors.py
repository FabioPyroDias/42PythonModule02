def check_plant_health(plant_name, water_level, sunlight_hours) -> str:
    """Receives a plant name, water level and sunlight hours.
    Ensures they are valid and raises exceptions when they're not"""
    try:
        if plant_name is None:
            raise ValueError
    except ValueError:
        return "Error: Plant name cannot be empty!"
    try:
        if water_level < 1 or water_level > 10:
            raise ValueError
    except ValueError:
        if water_level < 1:
            return f"Error: Water level {water_level} is too low (min 1)"
        else:
            return f"Error: Water level {water_level} is too high (max 10)"
    try:
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError
    except ValueError:
        if sunlight_hours < 2:
            return f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        else:
            return (f"Error: Sunlight hours {sunlight_hours} "
                    "is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Tests all options, both good and bad, of the previous method"""
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    print(check_plant_health("tomato", 3, 9))
    print()
    print("Testing empty plant name...")
    print(check_plant_health(None, 5, 5))
    print()
    print("Testing bad water level...")
    print(check_plant_health("tomato", 15, 12))
    print()
    print("Testing bad sunlight hours...")
    print(check_plant_health("tomato", 4, 0))
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
