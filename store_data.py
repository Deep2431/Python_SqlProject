from SqlMain import Database

def app():
    db = Database()
    while True:
        print("Press 1 to insert data")
        print("Press 2 to view data")
        print("Press 3 to delete data")
        print("Press 4 to update data")
        print("Press 5 to generate bill")
        print("Press 6 to exit")

        try:
            choice = int(input())
            if (choice == 1):
                pro_id = int(input("Enter the product Id"))
                name = input("Enter name of the product")
                type = input("Enter the type of the product")
                cost = int(input("Enter the cost of the product"))
                db.fetchData(pro_id, name, type, cost)

            elif (choice == 2):
                db.fetchData()

            elif (choice == 3):
                pro_id = int(input("Enter the product Id of the product, which is to be deleted.."))
                db.deleteData(pro_id)

            elif (choice == 4):
                pro_id = int(input("Enter the product Id"))
                new_name = input("Enter new name of the product: ")
                new_type = input("Enter new the type of the product: ")
                new_cost = int(input("Enter new the cost of the product: "))
                db.updateData(pro_id, new_name, new_type, new_cost)

            elif (choice == 5):
                db.generateBill()   

            elif (choice == 6):
                break       

            else:
                print("Enter a valid input")
        
        except Exception as e:
            print(e)
            print("Invalid details, Please try again")

if __name__ == "__main__":
    app()
