import sqlite3

try:
    con = sqlite3.connect(r"e:\classroom\python\oct1\hr.db")
    cur = con.cursor()
    id = input("Enter job id : ")
    title =input("Enter new job title : ")
    cur.execute("update jobs set job_title = ? where job_id = ?", (title,id))
    if cur.rowcount == 1:
        print("Updated Successfully!")
        con.commit()  # make changes permanent
    else:
        print("Job id not found!")
except Exception as ex:
    print("Error : ", ex)
finally:
    con.close()





