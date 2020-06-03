import mysql.connector

class bd_conn:



    def __init__(self,name,cat,qua,pri,dec,id):

        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="ice_creame")

        cursor=mydb.cursor()

        sql="insert into products (pro_name,pro_cat,pro_quant,pro_price,decp) values (%s,%s,%s,%s,%s)"
        var=(name,cat,qua,pri,dec)
        cursor.execute(sql,var)
        mydb.commit()


        #print(cursor.lastrowid)
        self.id=int(cursor.lastrowid)
        self.name=name




#mi=bd_conn("bhai","apple",7,4,"aka")
