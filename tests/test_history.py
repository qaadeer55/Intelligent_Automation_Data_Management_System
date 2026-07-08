from database.db import get_all_user_requests

print("\n========== AUTOMATION HISTORY ==========\n")

records = get_all_user_requests()

for record in records:

    print(f"Request ID : {record[0]}")
    print(f"Service    : {record[1]}")
    print(f"Query      : {record[2]}")
    print(f"Created At : {record[3]}")
    print("-" * 45)