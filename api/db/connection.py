import os
from databricks import sql

def get_connection():
    host = os.getenv("DATABRICKS_HOST")
    http_path = os.getenv("DATABRICKS_HTTP_PATH")
    token = os.getenv("DATABRICKS_TOKEN")

    if not host or not http_path or not token:
        raise Exception("Missing Databricks environment variables")

    return sql.connect(
        server_hostname=host,
        http_path=http_path,
        access_token=token
    )
