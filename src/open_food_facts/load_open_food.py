import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(
    host='caltestdb.cf8tp8471cpq.us-west-1.redshift.amazonaws.com',
    user='caldb',
    port=5439,
    password='Calpass123',
    dbname='fooddb')

cur = conn.cursor()

sql = """copy openfoodfacts from 's3://caldbtest/load.manifest'
    credentials 'aws_iam_role=arn:aws:iam::587308539385:role/aws-service-role/redshift.amazonaws.com/AWSServiceRoleForRedshift'
    gzip delimiter ','
    ssh ignoreheader 1
    null as '000'
    removequotes
    maxerror as 20000;"""
cur.execute(sql)
conn.commit()
