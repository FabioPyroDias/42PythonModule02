class Plant():
    """"""
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int) -> None:
        """"""
        self.name = name
        self.__water_level = water_level
        self.__sunlight_hours = sunlight_hours

    def set_water_level(self, water_level: int) -> None:
        """"""
        self.__water_level = water_level

    def set_sunlight_hours(self, sunlight_hours: int) -> None:
        """"""
        self.__sunlight_hours = sunlight_hours

    def get_water_level(self) -> int:
        """"""
        return self.__water_level

    def get_sunlight_hours(self) -> int:
        """"""
        return self.__sunlight_hours


class GardenError(Exception):
    """Custom Exception raised for Garden Problems"""
    def __init__(self, message: str = "") -> None:
        """"""
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """Returns the specific error raised"""
        return f"Caught GardenError: {self.message}"


class PlantError(GardenError):
    """"""
    def __init__(self, message: str) -> None:
        """"""
        super().__init__(message)

    def __str__(self) -> str:
        """"""
        return self.message


class WaterError(GardenError):
    """Custom Exception raised for Water Problems"""
    def __init__(self, message) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        """Returns WaterError message"""
        return self.message


class GardenManager():
    """"""
    def __init__(self) -> None:
        """"""
        self.__plants = []
        self.__water_level = 10
        self.__water_cost = 4

    def check_plant(self, plant: Plant) -> None:
        """"""
        if plant.name is None:
            raise PlantError("Plant name cannot be empty!")
        water = plant.get_water_level()
        sun = plant.get_sunlight_hours()
        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")

    def add_plant(self, plant: Plant) -> None:
        """"""
        try:
            self.check_plant(plant)
        except PlantError as error:
            print(f"Error adding plant: {error}")
            return
        print(f"Added {plant.name} successfully")
        self.__plants.append(plant)

    def water_plants(self) -> None:
        """"""
        print("Opening watering system")
        try:
            for plant in self.__plants:
                if self.__water_level - self.__water_cost < 0:
                    raise WaterError("Not enough water in the tank")
                plant.set_water_level(plant.get_water_level()
                                      + self.__water_cost)
                self.__water_level -= self.__water_cost
                print(f"Watering {plant.name} - success")
        except WaterError as error:
            print(f"Error watering plants: {error}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self) -> None:
        """"""
        for plant in self.__plants:
            try:
                self.check_plant(plant)
                print(f"{plant.name}: healthy (water: "
                      f"{plant.get_water_level()} sun: "
                      f"{plant.get_sunlight_hours()})")
            except PlantError as error:
                print(f"Error checking {plant.name}: {error}")

    def error_recovery(self) -> None:
        """"""
        total_water_cost = 0
        for index in range(len(self.__plants)):
            total_water_cost += 1
        total_water_cost *= self.__water_cost
        try:
            if total_water_cost > self.__water_level:
                raise GardenError("Not enough water in tank")
        except GardenError as error:
            print(error)
        finally:
            print("System recovered and continuing...")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    print()
    garden = GardenManager()
    tomato = Plant("tomato", 1, 8)
    lettuce = Plant("lettuce", 10, 3)
    unnamed = Plant(None, 5, 5)
    print("Adding plants to garden...")
    garden.add_plant(tomato)
    garden.add_plant(lettuce)
    garden.add_plant(unnamed)
    print()
    print("Watering plants...")
    garden.water_plants()
    print()
    print("Checking plant health...")
    garden.check_plants_health()
    print()
    print("Testing error recovery...")
    garden.error_recovery()
    print()
    print("Garden management system test complete!")
