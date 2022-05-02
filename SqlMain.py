import pyodbc as pc

class Database:
    def __init__(self):
        self.con =  pc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-QVF90N1;DATABASE=Project;Trusted_Connection=yes')
        query = "create table ShopData (product_id int primary key, name varchar(50), type varchar(50), cost int)"
        cur = self.con.cursor()
        cur.execute(query)
        print("Done!!")
    
    def insert(self, pro_id, name, type, cost):
        query = "insert into ShopData (pro_id, name, type, cost) values ({},{},{},{})".format(pro_id, name, type, cost)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Data inserted!!")

    def fetchData(self):
        query = "select * from ShopData"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print('pro_id: ', row[0])
            print('name: ', row[1])
            print('type: ', row[2])
            print('cost: ', row[3])
            print()
        
    def deleteData(self, pro_id):
        query = "delete from user where pro_id = {}".format(pro_id)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted!!!")

    def updateData(self,pro_id, new_name, new_type, new_cost):
        query = "update ShopData set name='{}', type='{}', cost={}where pro_id={}".format(new_name, new_type, new_cost, pro_id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Your data has been updated")

    def generateBill(self):
        query = "select sum(cost) as TotalBill from ShopData"
        cur = self.con.cursor()
        cur.execute(query)
        print("Bill generated")
