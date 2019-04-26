import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries
from helpers import connect_database

def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    conn = connect_database()
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    # insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()