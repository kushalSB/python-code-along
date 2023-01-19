import pandas as pd

#Empty list to add our user inputed data
my_products=[]

#Loop that breaks when user presses exit condition
while True:
    a= input("Enter Product name or 0 to exit: ")
    if a=='0':
        break
    my_products.append(a)

#Only runs if user provides the data
if len(my_products)>0:
    #Converting the list to a dataframe object
    df=pd.DataFrame({"Products":my_products})
    #Converting the dataframe object to a csv file
    df.to_csv("products.csv")

    #We can also convert the data to jsons
    df.to_json("products.json")