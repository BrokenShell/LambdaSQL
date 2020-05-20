"""
Titanic Data

"""
import psycopg2
from module4.creds import cred


cloud = psycopg2.connect(
    dbname=cred.dbname,
    user=cred.user,
    password=cred.password,
    host=cred.host,
)

curs = cloud.cursor()

curs.execute("""
SELECT * FROM Titanic
WHERE Age < 18;
""")

print("Kids:", *curs.fetchall(), sep='\n')
