"""
CP1404/CP5632 Practical
Read, process and display Wimbledon data
Estimate: 45 minutes
Actual:   55 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Get and read Wimbledon file, process the data and print the champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Get records from the file and append lines into a list."""
    records = []
    with open(filename, 'r', encoding='utf-8-sig') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records


def process_records(records):
    """Create dictionary of champions and set of countries from the records list."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions:")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()
