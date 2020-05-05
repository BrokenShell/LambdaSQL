"""
Titanic Data

"""
import psycopg2


cloud = psycopg2.connect(
    dbname="rphzklxx",
    user="rphzklxx",
    password="J0i83etc3hsiBVaNQ5F999zzJJcFxluM",
    host="rajje.db.elephantsql.com",
    port="5432",
)
curs = cloud.cursor()

curs.execute("""
SELECT * FROM Titanic
WHERE Age < 18;
""")

print("Kids:", *curs.fetchall(), sep='\n')

