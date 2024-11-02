import os.path
import psycopg
from flask import current_app

def create_database():
    schema_path = os.path.join(os.path.abspath("./db"), "seed.sql")
    with open(schema_path, "r") as file:
        schema = file.read()

    with psycopg.connect(current_app.config["SQLALCHEMY_DATABASE_URI"]) as conn:
        with conn.cursor() as cur:
            cur.execute(schema)
            conn.commit()
