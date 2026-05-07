from api.db.connection import get_connection
from api.kafka_producer import send_trip_event


def create_trip(trip: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1")  # placeholder DB logic

    conn.commit()
    cursor.close()
    conn.close()

    # 🚀 SEND TO KAFKA
    send_trip_event({
        "event": "trip_created",
        "data": trip
    })

    return {
        "status": "created",
        "trip": trip
    }


def get_trips():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result
