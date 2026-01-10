class GardenError(Exception):
    """Custom Exception raised for Garden Problems"""
    def __init__(self, message: str = "") -> None:
        """"""
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """Returns the specific error raised"""
        if type(self) is PlantError:
            return f"Caught a garden error: The {self.message} "
            "plant is wilting!"
        if type(self) is WaterError:
            return "Not enough water in the tank!"


class PlantError(GardenError):
    """Custom Exception raised for Plant Problems"""
    def __init__(self, message) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        """Returns PlantError message"""
        return f"The {self.message} plant is wilting!"


class WaterError(GardenError):
    """Custom Exception raised for Water Problems"""
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        """Returns WaterError message"""
        return "Not enough water in the tank!"


def test_plant_error(plant: str = "tomato", is_wilting: bool = True) -> None:
    """Method where PlantError is raised"""
    if is_wilting:
        raise PlantError(plant)


def test_water_error(irrigation: int = 10, water_tank: int = 9) -> None:
    """Method where WaterError is raised"""
    if irrigation > water_tank:
        raise WaterError()
    water_tank -= irrigation


def handle_plant_error() -> None:
    """Method where PlantError Exception is caught"""
    try:
        test_plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def handle_water_error() -> None:
    """Method where WaterError Exception is caught"""
    try:
        test_water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def handle_garden_error(is_wilting: bool, water_tank: int) -> None:
    """Method where PlantError and WaterError Exceptions are caught
    They're dealt as GardenErrors"""
    try:
        test_plant_error("tomato", is_wilting)
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        test_water_error(10, water_tank)
    except GardenError as error:
        print(f"Caught a garden error: {error}")


def test_error_types() -> None:
    """Testing Errors method"""
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    handle_plant_error()
    print()
    print("Testing WaterError...")
    handle_water_error()
    print()
    print("Testing catching all garden errors...")
    handle_garden_error(True, 10)
    handle_garden_error(False, 9)
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_error_types()
