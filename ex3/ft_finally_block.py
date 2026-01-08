class Plant():
    """Simple Plant class with only name property"""
    def __init__(self, name: str = None):
        """Initializer"""
        self.name = name


def water_plants(plant_list):
    """Waters all plants in the plant_list, raising Exceptions if Plant's
    name is None"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError
            print(f"Watering {plant.name}")
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    """Tester function"""
    normal_list = {Plant("tomato"), Plant("lettuce"), Plant("carrots")}
    error_list = {Plant("tomato"), Plant()}
    print("=== Garden Watering System ===")
    print()
    water_plants(normal_list)
    print()
    water_plants(error_list)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
