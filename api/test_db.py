from api.db import get_connection

def test():
    print("START TEST DB CONNECTION")

    try:
        conn = get_connection()
        print("CONNECTED SUCCESSFULLY")

        cursor = conn.cursor()
        cursor.execute("SELECT 1")

        result = cursor.fetchall()
        print("RESULT:", result)

        cursor.close()
        conn.close()

    except Exception as e:
        print("ERROR OCCURED:")
        print(e)

if __name__ == "__main__":
    test()
