import mysql.connector

#Connect to the server
cnx = mysql.connector.connect(user='root', password='Pucky11SQL20',
                              host='127.0.0.1',
                              database='company')

'''
Note in the future for your project, instead of entering the username and password
you prompt the user through str(input()) and login that way!!
'''

cur = cnx.cursor()

#Execute a couple queries
cur.execute("use company") #.execute() executes a string as an SQL query
cur.execute("select * from employee")

#Fetch results
col_names = cur.column_names #Gets the names of the columns as an array
print("Attribute List:\n", col_names)
rows = cur.fetchall() #Gets all of the content in an array
print("Number of entries in table", len(rows))
print("Current employee table content:\n", rows)

#Slightly better formatting
#For more formatting notes, look at 233 string formatting notes.
cur.execute("select * from employee")
rows = cur.fetchall()
print("Current content:\n")
size = len(rows)
for i in range(size):
    for x in range(len(rows[i])):
        print(rows[i][x], end='\t')
    print()
    
#Note: The execute function can run insert, update, and delete statements too!
# Be aware that these changes will be reflected on the database as well if you inlcude:
# cnx.commit()!!!!

cnx.close()