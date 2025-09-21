import mysql.connector as ms
myconnector = ms.connect(host="localhost",user="root",passwd="similemi123@",database="liberty_library")

if myconnector.is_connected():
        print('ypip')