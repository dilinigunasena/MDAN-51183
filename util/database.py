import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'admin',
    password = 'admin123'    
)

# prepare a cursor-object 
cursorObj = dataBase.cursor()

#creating a database 
cursorObj.execute("CREATE DATABASE bicyclestore")

print('All is Welllll')
print('admin username : superadmin /  password: super123 ')