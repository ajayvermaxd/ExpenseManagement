#creating new file
def creat_expenses():
    fileObject=open("expence.csv", "x")
    data = "date, category, description,amount"
    fileObject.write(data)
#tanking input of expences
def taking_from_user():
    fileObject= open("expence.csv", "a")
    date = input("please enter the date : ")
    catagory = input ("please input the catagory : ")
    description = input ("please input description : ")
    amount = input("please enter amount : ")
    data =  "\n" + (date + "," + catagory + "," + description + "," + amount )
    fileObject.write(data)
    #reading the file
def read_file():
    fileObject = open("expence.csv", "r")
    data = fileObject.read()
    print(data)
creat_expenses()
taking_from_user()
read_file()


