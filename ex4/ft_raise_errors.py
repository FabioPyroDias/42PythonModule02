class Plant():
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.__name = None
        self.__water_level = water_level
        self.__sunlight_hours = sunlight_hours
        self.set_name(name)
        self.set_water_level(water_level)
        self.set_sunlight_hours(sunlight_hours)
        print(f"Plant '{self.__name}' is healthy!")

    def set_name(self, name: str) -> None:
        if name is None or len(name) == 0:
            raise ValueError("Error: Plant name cannot be empty")
        self.__name = name

    def set_water_level(self, water_level: int) -> None:
        if water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too low (min 1)")
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too high (max 10)")
        self.__water_level = water_level

    def set_sunlight_hours(self, sunlight_hours: int) -> None:
        if sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        self.__sunlight_hours = sunlight_hours


def test_plant_check():
    print("=== Garden Plant Health Checker ===")
    print()
    print("Testing good values...")
    try:
        Plant("tomato", 3, 6)
    except ValueError as error:
        print(error)
    print()
    print("Testing empty plant name...")
    try:
        Plant("", 3, 6)
    except ValueError as error:
        print(error)
    print()
    print("Testing bad water level...")
    try:
        Plant("tomato", 15, 6)
    except ValueError as error:
        print(error)
    print()
    print("Testing bad sunlight hours...")
    try:
        Plant("tomato", 3, 0)
    except ValueError as error:
        print(error)
    print()
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_check()
