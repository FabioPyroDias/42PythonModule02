class GardenError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


class Plant:
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    def __init__(self):
        self.__plants = []
        self.__water_tank = 8

    def add_plant(self, plant: Plant) -> None:
        try:
            if plant.name is None or len(plant.name) == 0:
                raise PlantError("Plant name cannot be empty")
            if plant.water_level < 1:
                raise PlantError(f"Water level {self.water_level} "
                                 f"is too low (min 1)")
            if plant.water_level > 10:
                raise PlantError(f"Water level {self.water_level} "
                                 f"is too high (max 10)")
            if plant.sunlight_hours < 2:
                raise PlantError(f"Sunlight hours {self.sunlight_hours} "
                                 f"is too low (min 2)")
            if plant.sunlight_hours > 12:
                raise PlantError(f"Sunlight hours {self.sunlight_hours} "
                                 f"is too high (max 12)")
            self.__plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self):
        index = 0
        print("Opening watering system")
        try:
            while index < len(self.__plants):
                if self.__water_tank < 4:
                    raise WaterError("Not enough water in tank")
                self.__plants[index].water_level += 4
                self.__water_tank -= 4
                print(f"Watering {self.__plants[index].name} - sucess")
                index += 1
        except WaterError:
            print(f"Watering {self.__plants[index].name} - failure")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self):
        index = 0
        while index < len(self.__plants):
            try:
                if self.__plants[index].water_level > 10:
                    raise PlantError(f"Water level "
                                     f"{self.__plants[index].water_level} "
                                     f"is too high (max 10)")
                if self.__plants[index].water_level < 1:
                    raise PlantError(f"Water level "
                                     f"{self.__plants[index].water_level} "
                                     f"is too low (min 1)")
                if self.__plants[index].sunlight_hours > 12:
                    raise PlantError(f"Sunlight hours {self.sunlight_hours} "
                                     f"is too high (max 12)")
                if self.__plants[index].sunlight_hours < 2:
                    raise PlantError(f"Sunlight hours {self.sunlight_hours} "
                                     f"is too low (min 2)")
                print(f"{self.__plants[index].name}: healthy (water "
                      f"{self.__plants[index].water_level}, sun: "
                      f"{self.__plants[index].sunlight_hours})")
            except PlantError as error:
                print(f"Error checking {self.__plants[index].name}: {error}")
            index += 1

    def check_status(self) -> None:
        try:
            if self.__water_tank <= 0:
                raise GardenError("Not enough water in tank")
        except GardenError as error:
            print(f"Caught GardenError: {error}")
            self.__water_tank += 8
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    tomato = Plant("tomato", 1, 8)
    lettuce = Plant("lettuce", 10, 5)
    no_name = Plant("", 2, 3)
    manager = GardenManager()
    manager.add_plant(tomato)
    manager.add_plant(lettuce)
    manager.add_plant(no_name)
    print()
    print("Watering plants...")
    manager.water_plants()
    print()
    print("Checking plant health...")
    manager.check_plants_health()
    print()
    print("Testing error recovery...")
    manager.check_status()
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
