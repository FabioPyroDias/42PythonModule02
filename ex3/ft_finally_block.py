class PlantError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


def water_plants(plant_list) -> None:
    print("Opening watering system")
    index = 0
    try:
        while index < len(plant_list):
            if plant_list[index] is None:
                raise PlantError(f"Error: cannot water "
                                 f"{plant_list[index]} - invalid plant!")
            print(f"Watering {plant_list[index]}")
            index += 1
    except PlantError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    print()
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()
    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
