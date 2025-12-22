import math
import svgwrite
from svgwrite.shapes import Rect, Circle
from svgwrite.shapes import Polygon


def print_menu() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")


def draw_square(dwg: svgwrite.Drawing) -> None:
    print("Insert square")
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    dwg.add(
        Rect(
            insert=(left, top),
            size=(side, side),
            fill=fill,
            stroke=stroke,
        )
    )
    print()


def draw_circle(dwg: svgwrite.Drawing) -> None:
    print("Insert circle")
    cx = float(input("- Center X position: "))
    cy = float(input("- Center Y position: "))
    radius = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    dwg.add(
        Circle(
            center=(cx, cy),
            r=radius,
            fill=fill,
            stroke=stroke,
        )
    )
    print()


def draw_hexagon(dwg: svgwrite.Drawing) -> None:
    print("Insert hexagon details:")
    cx = float(input("Middle point X: "))
    cy = float(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    # apothem a, circumradius R for regular hexagon: a = R * cos(30°) ⇒ R = a / cos(30°)[web:232][web:234][web:237]
    R = apothem / math.cos(math.radians(30))

    # angles for corners: start at top-right, go clockwise:
    # top-right = -60°, right = 0°, bottom-right = 60°, bottom-left = 120°,
    # left = 180°, top-left = 240°
    angles_deg = [-60, 0, 60, 120, 180, 240]

    points: list[tuple[int, int]] = []

    for ang in angles_deg:
        rad = math.radians(ang)
        x = cx + R * math.cos(rad)
        y = cy + R * math.sin(rad)
        points.append((round(x), round(y)))  # round to integers before polygon[web:230][web:232][web:238]

    hexagon = Polygon(points=points, fill=fill, stroke=stroke)
    dwg.add(hexagon)
    print()


def save_svg(dwg: svgwrite.Drawing) -> None:
    filename = input("Insert filename: ")
    print(f"Saving file to \"{filename}\"")
    proceed = input("Proceed (y/n)?: ")
    if proceed.lower() == "y":
        dwg.saveas(filename, pretty=True, indent=2)  # pretty SVG with 2-space indent[web:211][web:214]
        print("Vector saved successfully!\n")
    else:
        print("Save cancelled.\n")


def main() -> None:
    print("Program starting.")
    dwg = svgwrite.Drawing()

    while True:
        print_menu()
        choice = input("Your choice: ")

        if choice == "1":
            draw_square(dwg)
        elif choice == "2":
            draw_circle(dwg)
        elif choice == "3":
            draw_hexagon(dwg)
        elif choice == "4":
            save_svg(dwg)
        elif choice == "0":
            print("Exiting program.\n")
            break
        else:
            print("Invalid choice.\n")

    print("Program ending.")


if __name__ == "__main__":
    main()
