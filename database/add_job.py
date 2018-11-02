import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
    cur = con.cursor()
    cur.execute("insert into jobs values(?,?,?)",('DP','MS.NET Developer',10000))
    con.commit()  # make changes permanent
    print("Added Job Successfully!")
except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()





