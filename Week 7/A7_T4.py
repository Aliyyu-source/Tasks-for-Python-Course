from dataclasses import dataclass

DELIMITER = ";"


@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float


def read_timestamps(filename: str) -> list[TIMESTAMP]:
    timestamps: list[TIMESTAMP] = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            row = line.rstrip()
            if row == "":
                continue
            columns = row.split(DELIMITER)
            ts = TIMESTAMP(
                weekday=columns[0],
                hour=columns[1],
                consumption=float(columns[2]),
                price=float(columns[3]),
            )
            timestamps.append(ts)

    return timestamps


def print_timestamps(timestamps: list[TIMESTAMP]) -> None:
    print("Electricity usage:")
    total_consumption = 0.0
    total_price = 0.0

    for ts in timestamps:
        row_total = ts.consumption * ts.price
        total_consumption += ts.consumption
        total_price += row_total
        print(
            f" - {ts.weekday} {ts.hour}, price {ts.price:.2f} €, "
            f"consumption {ts.consumption:.2f} kWh, total {row_total:.2f} €"
        )

    print(f"Total consumption: {total_consumption:.2f} kWh")
    print(f"Total cost: {total_price:.2f} €")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f"Reading file \"{filename}\".")

    timestamps = read_timestamps(filename)
    print_timestamps(timestamps)

    print("Program ending.")


if __name__ == "__main__":
    main()
