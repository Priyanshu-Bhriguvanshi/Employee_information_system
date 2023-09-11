from mysql.connector import connect
conn=connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)
print("Database Connected...")

#choice

print("1. Add Record \n2. Update record \n3. Delete Record \n4. Find Record \n5. Find all Record \n ")
choice = int(input("Enter the Choice : "))

#data insert

if choice==1:
    print("1. Single Data Insert \n2. Bulk Data insert\n")
    ins_choice=int(input("Enter Choice : "))
    if ins_choice==1:
        sql="insert into emp values(%s, %s,%s,%s,%s)"
        eid=int(input("Enter Emp id : "))
        ename=input("Enter Emp name : ")
        dno=int(input("Enter Dno. : "))
        sal=int(input("Enter Salary : "))
        email=input("Enter Email : ")
        val=(eid,ename,dno,sal,email)
        curr=conn.cursor()
        curr.execute(sql,val)
        conn.commit()
        print(curr.rowcount, "data inserted")

# bulk insert

    elif ins_choice ==2:
        list=[]
        while True:
            sql="insert into emp values(%s, %s,%s,%s,%s)"
            eid=int(input("Enter Emp id : "))
            ename=input("Enter Emp name : ")
            dno=int(input("Enter Dno. : "))
            sal=int(input("Enter Salary : "))
            email=input("Enter Email : ")
            val=(eid,ename,dno,sal,email)
            list.append(val)
            print("\ndou you wnat to continue ? Y or N ")
            y_or_no=input("Enter Choice : ").lower()
            if y_or_no == "n":
                break
        curr=conn.cursor()
        curr.executemany(sql,list)
        conn.commit()
        print(curr.rowcount, "data inserted")
    else:
        print("Wrong Insert Option")


#update record

elif choice==2:
    list=[]
    while True:
        sql = "update emp set sal=%s where eid= %s"
        sal=int(input("\nEnter Correct salary : "))
        eid=int(input("Enter emp id : "))
        val = (sal, eid)
        list.append(val)
        print("\nDo u want to continue? y or n")
        y_or_no=input("Enter Choice ...").lower()
        if y_or_no=="n":
            print("You Chosse to exit...")
            break
    curr=conn.cursor()
    curr.executemany(sql, list)
    conn.commit()
    print(curr.rowcount, "Data Updated...")

#delete record

elif choice==3:
    count=0
    while True:
        count=count+1
        sql= "delete from emp where eid=%s"
        eid=input("Enter Emp id : ")
        curr=conn.cursor()
        curr.execute(sql,(eid,))
        conn.commit()
        print("\nDo u want to continue? y or n")
        y_or_no=input("Enter Choice ...").lower()
        if y_or_no=="n":
            print(count, "Row Deleted...")
            print("You Chosse to exit...")
            break

# find record

elif choice==4:
    emp_id = input("Enter Emp ID to search: ")
    sql = "SELECT * FROM emp WHERE eid = %s"
    val = (emp_id,)
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        print("Employee Found:")
        print("Emp ID:", result["eid"])
        print("Emp Name:", result["ename"])
        print("Dno.:", result["dno"])
        print("Salary:", result["sal"])
        print("Email:", result["email"])
    else:
        print("Employee not found.")


#Find All record


elif choice == 5:
    sql="select * from emp"
    curr=conn.cursor()
    curr.execute(sql)
    records = curr.fetchall()
    for record in records:
        print(record)



else :
    print("Yoou Enter Wrong Choice")

#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

