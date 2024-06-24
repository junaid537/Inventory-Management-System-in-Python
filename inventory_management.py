import json
import pandas as pd

class Products:
    def __init__(self,id,name,price,qty,threshold):
        self.id=id
        self.name=name
        self.price=price
        self.qty=qty
        self.threshold=threshold
    
class Inventory:
    
    
    #constructor that initializes instance variable filename and class/static variable products(dictionary).Also calls load_data()
    def __init__(self,filename):
        self.products={}
        self.filename=filename
        self.load_data()     #  To Load inventory data from the JSON file at the start of the program.
        
    #load_data method loads data from json file to class variable products(dictionary)
    def load_data(self):
        try:
            with open(self.filename) as data_file:
                data=json.load(data_file) 
            self.products=data
        except FileNotFoundError:
            print("file not found , please enter the location of file accurately")
            pass
    
    #display method displays all products
    def display(self):
        print(json.dumps(self.products,indent=4))
        df=pd.DataFrame(self.products)
        print(df)
        
        
    #To get Data on Excel sheet
    def generateExcelreport(self):
        df=pd.DataFrame(self.products)
        print(df)
        df.to_excel('data.xlsx')
        
    #add method adds a product to products dictionary
    def add(self,product):
        self.products[str(product.id)]=product.__dict__
        self.display()
        self.saveTojson()
        self.lowStockAlert()
     
    #update method updates a product's name or price or quantity and calls savetojson() method to save data into json file for data persistency
    def update(self,old,product):
        if old in self.products.keys():
            if product.name:
                self.products[old]['name']=product.name
                print("Name Updated successfully, check json file")
            if product.qty:
                self.products[old]['qty']=int(product.qty)
                print("Qty Updated successfully, check json file")
                
            if product.price:
                self.products[old]['price']=float(product.price)
                print("Price Updated successfully, check json file")
            if product.threshold:
                self.products[old]['threshold']=int(product.threshold)
                print("Threshold Updated successfully, check json file")
        else:
            print("Sorry, given Product ID does not exist in the inventory, no update possible !!")
        self.lowStockAlert()
        self.saveTojson()
        self.display()
    
    # saveTojson method saves all the data to json file
    def saveTojson(self):
        with open("/Users/junaidiqbalkhalidi/Desktop/python ques/project/data.json", "w") as outfile: 
            json.dump(self.products, outfile)
    
    #showProduct method is used to view a specific product
    def showProduct(self,id):
        if id not in self.products.keys():
            print("No such product exists")
        else:
            print("Product details are")
            print("Product ID: {},Product name: {}, Product Price: {} Product Quantity: {}".format(self.products[id]['id'],self.products[id]["name"],self.products[id]['price'],self.products[id]['qty']))
    
    #delete method is used to delete a product  
    def delete(self,id):
        if id not in self.products.keys():
            print("No such product exists with productID {}".format(id))
        else:
            del self.products[id]
            print("Product with ID {} deleted successfully".format(id))
            self.saveTojson()
            
    #totalInventory method is used to print total Inventory value
    def totalInventoryValue(self):
        sum=0.00
        for key in self.products.keys():
            sum+=float(self.products[key]['price'])
        print("Total Inventory Value is {}$".format(sum))
    
    #lowStockAlert method alerts on when any product goes below its mininimum threshold  
    def lowStockAlert(self):
        flag=0
        for key in self.products.keys():
            if self.products[key]['qty']<self.products[key]['threshold']:
                flag=1
                print("ALERT !!! Product {} is going low in stock & has crossed minimum threshold limit by {} units".format(self.products[key]['name'],self.products[key]['threshold']-self.products[key]['qty']))
        if flag==0:
            print("FULL STOCK IN INVENTORY")
            
def main():
    
    #Inventory Object creation 
    i1=Inventory("/Users/junaidiqbalkhalidi/Desktop/python ques/project/data.json")
    
    while(True):
        print("1. Display all Products")
        print("2. Update a Product")
        print("3. To Insert a Product")
        print("4. Delete a  Product")
        print("5. View a Specific Product")
        print("6. Low Stock Alert")
        print("7. Total Inventory Value")
        print("8. Exit") 
        print("9. Get data in Excel Sheet")   
        
        option=input("enter your choice")
    
        if option=="1":
            i1.display()
            
        elif option=="2":
            old=input("enter product id")
            pname=input("enter new product name or else leave  blank by pressing Enter Key")
            qty=input("enter new quantity or else leave  blank by pressing Enter Key")
            price=input("enter new price or else leave  blank by pressing Enter Key")
            threshold=input("enter minimum quantity limit for this product or or else leave  blank by pressing Enter Key")
            product=Products(old,pname,price,qty,threshold)
            i1.update(old,product)
            
        elif option=="3":
            pid=input("add product id")
            pname=input("enter product name")
            qty=input("enter product quantity")
            price=input("enter product price")
            threshold=input("enter minimum quantity reqiured for alert notification")
            if not pid:
                print("product id not mentioned , start again")
                continue
            if not pname:
                print("product name not mentioned , start again")
                continue
            if not qty:
                print("product qty not mentioned , start again")
                continue
            if not price:
                print("product price not mentioned , start again")
                continue
            if not threshold:
                print("product threshold not mentioned , start again")
                continue
            if price.isnumeric()==False or price.is_float()==False: 
                print("product price is not numerical , start again")
                continue
            if qty.isnumeric()==False:
                print("product qty is not numerical , start again")
                continue
            if threshold.isnumeric()==False:
                print("product threshold is not numerical , start again")
                continue
                
            product=Products(pid,pname,float(price),int(qty),int(threshold))
            i1.add(product)
        
        elif option=="4":
            id=input("Enter ID of product whose details you wanna delete")
            i1.delete(id)
               
        elif option=="5":
            id=input("Enter ID of product whose details you wanna see")
            i1.showProduct(id)
            
        elif option=="6":
            i1.lowStockAlert()
            
        elif option=="7":
            i1.totalInventoryValue()
            
        elif option=="8":
            return
        
        elif option=="9":
            i1.generateExcelreport()
       
        else:
            print("Invalid Input, Please enter from the above given options")

#Initiation of the program happens here with the main function call               
if __name__ == '__main__':
    main()