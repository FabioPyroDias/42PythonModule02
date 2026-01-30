class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"Caught a garden error: {self.message}"


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught PlantError: {self.message}"


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self):
        return f"Caught WaterError: {self.message}"


def test_plant_error():
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(error)


def test_water_error():
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(error)


def test_garden_error():
    try:
        raise GardenError("The tomato plant is wilting!")
    except GardenError as error:
        print(error)
    try:
        raise GardenError("Not enough water in the tank!")
    except GardenError as error:
        print(error)


def test_errors():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    test_plant_error()
    print()
    print("Testing WaterError...")
    test_water_error()
    print()
    print("Testing catching all garden errors...")
    test_garden_error()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
