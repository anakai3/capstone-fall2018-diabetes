import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def open_db_connection():
    # Connect to the database
    conn = psycopg2.connect(
        host='caltestdb.cf8tp8471cpq.us-west-1.redshift.amazonaws.com',
        user='caldb',
        port=5439,
        password='Calpass123',
        dbname='fooddb')
    return conn

def close_db_connection(conn):
    if not conn:
        return
    conn.close()
