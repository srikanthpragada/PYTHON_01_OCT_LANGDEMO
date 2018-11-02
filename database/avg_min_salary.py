import sqlite3

con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
cur = con.cursor()
cur.execute("select avg(min_salary) from jobs")
print("Average Min Salary : ", cur.fetchone()[0])
con.close()





