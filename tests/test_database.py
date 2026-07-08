import sqlite3

connection = sqlite3.connect("database/automation.db")

cursor = connection.cursor()

print("\nUSER REQUESTS\n")

cursor.execute("SELECT * FROM user_requests")

for row in cursor.fetchall():
    print(row)

print("\nAPI RESULTS\n")

cursor.execute("SELECT * FROM api_results")

for row in cursor.fetchall():
    print(row)

print("\nAI OUTPUTS\n")

cursor.execute("SELECT * FROM ai_outputs")

for row in cursor.fetchall():
    print(row)

connection.close()