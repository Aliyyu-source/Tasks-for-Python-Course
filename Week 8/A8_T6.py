import svgwrite
from svgwrite.shapes import Rect, Circle

def print_menu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
    print("0 - Exit")


def drawSquare(PDwg: svgwrite.Drawing) -> None:
    print("Insert square")
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    PDwg.add(
        Rect(
            insert=(left, top),
            size=(side, side),
            fill=fill,
            stroke=stroke,
        )
    )
    print()


def drawCircle(PDwg: svgwrite.Drawing) -> None:
    print("Insert circle")
    cx = float(input("- Center X position: "))
    cy = float(input("- Center Y position: "))
    radius = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    PDwg.add(
        Circle(
            center=(cx, cy),
            r=radius,
            fill=fill,
            stroke=stroke,
        )
    )
    print()


def saveSvg(PDwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ")
    print(f"Saving file to \"{filename}\"")
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        # pretty=True and indent=2 for nice formatted SVG[web:211][web:214]
        PDwg.saveas(filename, pretty=True, indent=2)
        print("Vector saved successfully!\n")
    else:
        print("Save cancelled.\n")


def main() -> None:
    print("Program starting.")
    # 1. Initialise drawing (no filename yet)
    dwg = svgwrite.Drawing()

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            drawSquare(dwg)
        elif choice == "2":
            drawCircle(dwg)
        elif choice == "3":
            saveSvg(dwg)
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
