from database.db import (
    search_by_service,
    search_by_date
)

print("Search Options")
print("1. Service")
print("2. Date")

choice = input("Enter Choice: ")

if choice == "1":

    service = input(
        "Enter Service (Weather/Currency/Cryptocurrency): "
    )

    results = search_by_service(service)

elif choice == "2":

    date = input(
        "Enter Date (YYYY-MM-DD): "
    )

    results = search_by_date(date)

else:

    results = []

for row in results:
    print(row)