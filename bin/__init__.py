# import pyreadline
from utils import *
import mysql.connector
import platform
from configparser import ConfigParser

from commands.SHOW import _show_query_handling


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

    # readline.set_completer(sql_syntax_completer)
    # readline.parse_and_bind("tab: complete")

    # pyreadline.parse_and_bind(
    #     "tab: complete"
    # )

    while True:
        query = input(f"{user}@{database}$ ").strip()
        query_lower = query.lower()

        if query_lower in ("end", "exit"):
            break

        elif query_lower in ("cls", "clear"):
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
            continue

        try:
            cursor = conn.cursor()
            cursor.execute(query)

            result = cursor.fetchall()

        except Exception as e:
            log(e, type="error")
            continue

        if query_lower.startswith("show"):
            _show_query_handling(query_lower, result, database)

        else:
            for record in result:
                print(record)

        print()


if __name__ == "__main__":
    main()
