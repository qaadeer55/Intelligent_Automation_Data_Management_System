import sqlite3
import json


DATABASE_PATH = "database/automation.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def save_user_request(service_type, user_query):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO user_requests
        (service_type, user_query)
        VALUES (?, ?)
    """, (service_type, user_query))

    connection.commit()

    request_id = cursor.lastrowid

    connection.close()

    return request_id


def save_api_result(request_id, api_name, raw_response):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO api_results
        (request_id, api_name, raw_response)
        VALUES (?, ?, ?)
    """, (
        request_id,
        api_name,
        json.dumps(raw_response)
    ))

    connection.commit()

    connection.close()


def save_ai_output(request_id, ai_response):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO ai_outputs
        (request_id, ai_response, model_name)
        VALUES (?, ?, ?)
    """, (
        request_id,
        ai_response,
        "llama3.2:latest"
    ))

    connection.commit()

    connection.close()

def get_all_user_requests():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM user_requests
        ORDER BY request_id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


def get_all_api_results():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM api_results
        ORDER BY api_result_id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


def get_all_ai_outputs():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM ai_outputs
        ORDER BY output_id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records

def search_by_service(service):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM user_requests
        WHERE service_type = ?
    """, (service,))

    records = cursor.fetchall()

    connection.close()

    return records


def search_by_date(date):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM user_requests
        WHERE DATE(created_at)=?
    """, (date,))

    records = cursor.fetchall()

    connection.close()

    return records
    
def update_user_request(request_id, new_query):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE user_requests
        SET user_query=?
        WHERE request_id=?
    """, (
        new_query,
        request_id
    ))

    connection.commit()

    connection.close()


def delete_user_request(request_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM user_requests
        WHERE request_id=?
    """, (
        request_id,
    ))

    connection.commit()

    connection.close()