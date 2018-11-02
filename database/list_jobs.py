import sqlite3

con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
cur = con.cursor()
cur.execute("select * from jobs order by min_salary")

for job in cur.fetchall():
    print(job)

con.close()





