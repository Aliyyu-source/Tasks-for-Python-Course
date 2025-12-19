from dataclasses import dataclass

DELIMITER = ";"


@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float


@dataclass
class DAY_USAGE:
    weekday: str
    total_consumption: float
    total_cost: float


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


def analyse_daily_usage(timestamps: list[TIMESTAMP]) -> list[DAY_USAGE]:
    # prepare helper for each weekday
    weekdays_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturnday",
        "Sunday",
    ]

    usage_by_day: dict[str, DAY_USAGE] = {}

    # initialize gatherers
    for day in weekdays_order:
        usage_by_day[day] = DAY_USAGE(day, 0.0, 0.0)

    # gather consumption and cost
    for ts in timestamps:
        day_usage = usage_by_day.get(ts.weekday)
        if day_usage is None:
            # unknown day name, skip
            continue
        day_usage.total_consumption += ts.consumption
        day_usage.total_cost += ts.consumption * ts.price

    # build results list in fixed order
    results: list[DAY_USAGE] = []
    for day in weekdays_order:
        results.append(usage_by_day[day])

    return results


def build_result_lines(day_usages: list[DAY_USAGE]) -> list[str]:
    lines: list[str] = []
    lines.append("### Electricity consumption summary ###")
    for du in day_usages:
        line = (
            f" - {du.weekday} usage {du.total_consumption:.2f} kWh, "
            f"cost {du.total_cost:.2f} €"
        )
        lines.append(line)
    lines.append("### Electricity consumption summary ###")
    return lines


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    print(f"Reading file \"{filename}\".")

    timestamps = read_timestamps(filename)

    print("Analysing timestamps.")
    day_usages = analyse_daily_usage(timestamps)

    print("Displaying results.")
    result_lines = build_result_lines(day_usages)
    for line in result_lines:
        print(line)

    print("Program ending.")


if __name__ == "__main__":
    main()
