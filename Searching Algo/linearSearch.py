print("Linear Search using Python")

list1=[]
list11= list(input("Please Enter the list without any space: "))
key1 = input("Please enter the key you want to find: ")


def solution(list1,key):

    for index in range (len(list1)):
        if list1[index] == key:
         print(key, "Found on",index, "no. position!")
         break

    if index == len(list1)-1 and list1[index]!= key:
        print(key, "is absent on your given list!")

solution(list11,key1)        

         