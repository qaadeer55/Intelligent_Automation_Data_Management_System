from database.db import update_user_request

request_id = int(
    input("Enter Request ID: ")
)

new_query = input(
    "Enter New Query: "
)

update_user_request(
    request_id,
    new_query
)

print("\nRecord Updated Successfully.")