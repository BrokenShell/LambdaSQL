import psycopg2
import pandas as pd
from module2.creds import cred


url = "https://github.com/BrokenShell/DS-Unit-3-Sprint-2-SQL-and-Databases/raw/master/module2-sql-for-analysis/titanic.csv"
titanic = pd.read_csv(url).rename({
    "Siblings/Spouses Aboard": "SiblingsSpouses",
    "Parents/Children Aboard": "ParentsChildren",
}, axis=1)
titanic['Name'] = titanic["Name"].str.replace("'", "")
print(titanic.head().to_string())

cloud = psycopg2.connect(
    dbname=cred.dbname,
    user=cred.user,
    password=cred.password,
    host=cred.host,
)

cloud.cursor().execute("""
CREATE TABLE Titanic (
    Survived            INT,
    Pclass              INT,
    Name                varchar(120),
    Sex                 varchar(10),
    Age                 INT,
    SiblingsSpouses     INT,
    ParentsChildren     INT,
    Fare                INT);
""")
for row in titanic.values:
    cloud.cursor().execute(f"""
    INSERT INTO Titanic
    (Survived, Pclass, Name, Sex, Age, SiblingsSpouses, ParentsChildren, Fare)
    VALUES {tuple(row)};
    """)
cloud.commit()
