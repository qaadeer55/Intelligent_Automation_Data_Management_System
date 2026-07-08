from database.db import delete_user_request

request_id = int(
    input("Enter Request ID to Delete: ")
)

delete_user_request(
    request_id
)

print("\nRecord Deleted Successfully.")