def askDimension(PPrompt: str) -> float:
    """Ask user for a dimension (width or height) and return it as float."""
    value = float(input(f"Insert {PPrompt}: "))
    return value


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    """Calculate and return the area of a rectangle."""
    area = PWidth * PHeight
    return area


def main() -> None:
    """Main program logic."""
    print("Program starting.")
    width = askDimension("width")
    height = askDimension("height")

    print()
    area = calcRectangleArea(width, height)
    print(f"Area is {area}²")
    print("Program ending.")


if __name__ == "__main__":
    main()
