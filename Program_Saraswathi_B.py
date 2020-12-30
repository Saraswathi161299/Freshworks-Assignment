import threading 
#This will be executed in python 3.0 and above. Use import thread for python2.0 versions
from threading import*
import time

dic={}
#Here 'd' refers to the dictionary in which we store data that we create

#1.create operation 
#Syntax :    "create(key_name,value,timeout_value)" timeout is optional

def create(key,val,tout=0):
    if key in dic:
        print("ERROR : This key already exists.")     #Error message1
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1024*1024) and val<=(16*1024*1024):   #Constraints for file size less than 1GB and JSON object value less than 16KB 
                if tout==0:
                    lis=[val,tout]
                else:
                    lis=[val,time.time()+tout]
                if len(key)<=32:    #Constraints for input key_name capped at 32chars
                    dic[key]=lis
                    print("Key is created successfully.")
            else:
                print("ERROR : Memory limit exceeded!!! ")    #Error message2
        else:
            print("ERROR : Invalid key name!!! --> key_name must contain only alphabets and no special characters or numbers.")   #Error message3

#2.read operation
#Syntax:     "read(key_name)"
            
def read(key):
    if key not in dic:
        print("ERROR : Entered key does not exist in database. Please enter a valid key.") #Error message4
    else:
        a=dic[key]
        if a[1]!=0:
            if time.time()<a[1]:    #Comparing the current time with expiry time
                string=str(key)+":"+str(a[0])     #This is to return the value in JSON object format i.e.,"key_name:value"
                return string
            else:
                print("ERROR : Time-to-Live of ",key," has expired.")   #Error message5
        else:
            string=str(key)+":"+str(a[0])
            return string

#3.delete operation
#Syntax :    "delete(key_name)"

def delete(key):
    if key not in dic:
        print("ERROR : Entered key does not exist in database. Please enter a valid key.") #Error message4
    else:
        a=dic[key]
        if a[1]!=0:
            if time.time()<a[1]:    #Comparing the current time with expiry time
                del dic[key]
                print("Key is deleted successfully.")
            else:
                print("ERROR : Time-to-Live of ",key," has expired.")   #Error message5
        else:
            del dic[key]
            print("Key is deleted successfully.")

