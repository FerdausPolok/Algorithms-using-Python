print("Linear Search using Python")

list1=[]
list1= list(input("Please Enter the list without any space: "))
key = input("Please enter the key you want to find: ")

for index in range (len(list1)):
    if list1[index] == key:
        print(key, "Found on",index, "no. position!")


         