import os
from utils import *
import mysql.connector
from platform import system
from configparser import ConfigParser


def main() -> None:
    config = ConfigParser()
    config.read("config.ini")

    host = config.get("Database", "host")
    database = config.get("Database", "database_name")

    user = config.get("User", "user")
    password = config.get("User", "password")

    try:
        log(f"Start connection to: {host}")
        log(f"Database: {database}")
        log(f"User: {user}")
        log(f"Password: {'*' * len(password)}")

        conn = mysql.connector.connect(
            user=user, password=password, host=host, database=database
        )

    except mysql.connector.errors.DatabaseError as e:
        log(e, type="error")
        raise

    else:
        log("Succesfully connected", ending="\n\n")

    while True:
        query = input(f"{user}@{database}$ ").strip()
        query_lower = query.lower()

        if query_lower in ("end", "exit"):
            break

        elif query_lower in ("cls", "clear"):
            if system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
            continue

        try:
            cursor = conn.cursor()
            cursor.execute(query)

            result = cursor.fetchall()

        except mysql.connector.errors.ProgrammingError as e:
            log(e, type="error")
            continue

        if query_lower == "show tables":
            print(database)
            for record in result:
                print(f" |")
                print(f" |__{record[0]}")

        else:
            for record in result:
                print(record)

        print()


if __name__ == "__main__":
    main()
