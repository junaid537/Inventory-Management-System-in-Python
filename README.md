# Inventory-Management-System-in-Python
Install pandas to see data in Tabular form
Run the command to get data in excel sheet: pip install xlwt openpyxl xlrd

Run my program by running the command : python3 inventory_management.py

Each item/product has attributes id,name,price,qty,threshold . "threshold" refers to the minimum quatity required to not reach Low Stock Alert . 
If anytime quantity of a product hits below or equal to threshold then Low Stock Alert will be generated

insert the number from 1 to 9 to implement any of the functionalities
To insert the name enter alphabets and to insert id,price,threshold and qty insert as numbers.Althought care has been taken for invalid input .

For updating a product , first press option 2, enter the product id of the product you want to update. If you just want to update quantity pr price, then fill value for quantity or price and leave the name , threshold fields blank by not giving any input and just press Enter key .

To delete any product, select the opion 4 and enter product id of the product you want to delete .

To generate report in Excel sheet , please press option 9

If you want to see for Low Stock , press option 6.
Also, after each addition and update of item, Low Stock Alert will be printed if there is any





My Assumed format for JSON Data in JSON File is: 
    {
        "233": {
            "id": 233,
            "name": "Dal",
            "qty": 70,
            "price": 24.6,
            "threshold": 10
        },
        "323": {
            "id": 323,
            "name": "Pepsi",
            "qty": 10,
            "price": 23.7878,
            "threshold": 10
        },
        "243": {
            "id": 243,
            "name": "Milk",
            "qty": 20,
            "price": 34.89,
            "threshold": 10
        },
        "153": {
            "id": 153,
            "name": "Laptop",
            "qty": 34,
            "price": 89.67,
            "threshold": 67
        },
        "283": {
            "id": 283,
            "name": "TV",
            "qty": 2,
            "price": 89.78,
            "threshold": 10
        }
    }

