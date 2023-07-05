from utils import *


def _show_query_handling(query: str, result: list, database_name: str) -> None:
    content = " ".join(query.split(" ")[1:])

    match content:
        case "tables":
            sys.stdout.write(f"\nDatabase: {database_name}\n")
            sys.stdout.write(f"━┳{'━' * (len(database_name) + 8)}\n")
            sys.stdout.write(f" ┣╸ {result[0][0]}\n")
            
            for record in result[1:-1]:
                sys.stdout.write(f" ┃\n")
                sys.stdout.write(f" ┣╸ {record[0]}\n")
            
            sys.stdout.write(f" ┃\n")
            sys.stdout.write(f" ┗╸ {result[-1][0]}\n")
            
        case _:
            pass
