########################################################
# Task A10_T7
# Developer Aliyyu Zen-Abdeen
# Date 2025-12-24
########################################################

import random

random.seed(1234)  # deterministic placement for testing[web:382][web:379]


def layMines(PMineField: list[list[int]], PMines: int):
    """
    Randomly places PMines mines (value 9) into PMineField, which is a
    pre-initialized 2D matrix with zeros.
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0

    # collect all possible cell coordinates
    all_positions: list[tuple[int, int]] = []
    for r in range(rows):
        for c in range(cols):
            all_positions.append((r, c))

    # shuffle and pick first PMines positions
    random.shuffle(all_positions)  # uses global seed above[web:382]
    for i in range(min(PMines, len(all_positions))):
        r, c = all_positions[i]
        PMineField[r][c] = 9

    return None


def calculateNearbys(PMineField: list[list[int]]) -> None:
    """
    Given a 2D matrix where mines are marked with 9 and other cells are 0,
    calculate nearby mine counts for all non-mine cells.
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0

    # directions for all 8 neighbours[web:378][web:381][web:380]
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for r in range(rows):
        for c in range(cols):
            if PMineField[r][c] == 9:
                continue  # keep mines as 9
            count = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        count += 1
            PMineField[r][c] = count

    return None


def generateMinefield(
    PMineField: list[list[int]],
    PRows: int,
    PCols: int,
    PMines: int,
) -> None:
    """
    Initialize PMineField as PRows x PCols grid of zeros,
    lay PMines mines, then calculate neighbour counts.
    """
    # 1. Clear 2D-Matrix
    PMineField.clear()

    # 2. Initialize with zeros
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)

    # 3. Lay mines
    layMines(PMineField, PMines)

    # 4. Calculate nearbys
    calculateNearbys(PMineField)

    return None


def print_board(board: list[list[int]]) -> None:
    """Helper: print board one row per line like in example."""
    for row in board:
        print(row)


def save_board(board: list[list[int]], filename: str) -> None:
    """Save board to file in comma-separated format, each row on its own line."""
    with open(filename, "w", encoding="utf-8") as f:
        for row in board:
            line = ",".join(str(v) for v in row)
            f.write(line + "\n")


def print_menu() -> None:
    print("Options:")
    print("1 - Generate minesweeper board")
    print("2 - Show generated board")
    print("3 - Save generated board")
    print("0 - Exit")


def main() -> None:
    MineField: list[list[int]] = []

    print("Program starting.")

    while True:
        print()
        print_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            # Generate board
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))
            except ValueError:
                print("Invalid input. Please enter integers.")
                continue

            if rows <= 0 or cols <= 0:
                print("Rows and columns must be positive.")
                continue

            max_mines = rows * cols
            if mines < 0 or mines > max_mines:
                print(f"Mines must be between 0 and {max_mines}.")
                continue

            generateMinefield(MineField, rows, cols, mines)
        elif choice == "2":
            # Show board
            if not MineField:
                print("No board generated yet. Choose option 1 first.")
            else:
                print_board(MineField)
        elif choice == "3":
            # Save board
            if not MineField:
                print("No board generated yet. Choose option 1 first.")
            else:
                filename = input("Insert filename: ").strip()
                if filename == "":
                    print("Filename cannot be empty.")
                else:
                    save_board(MineField, filename)
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 0, 1, 2 or 3.")

    print("Program ending.")


if __name__ == "__main__":
    main()
