from database.db import (
    get_all_user_requests,
    get_all_api_results,
    get_all_ai_outputs
)

print("\nUSER REQUESTS\n")

for row in get_all_user_requests():
    print(row)

print("\nAPI RESULTS\n")

for row in get_all_api_results():
    print(row)

print("\nAI OUTPUTS\n")

for row in get_all_ai_outputs():
    print(row)