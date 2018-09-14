'''
Created on Sep 5, 2018

@author: hiramrios 80552404 last edited on Sep 5, 2018 
The purpose of this program is that given a text file with a username saltvalue and hashvalue will 
will try to find all the passwords to the file 
'''
import hashlib
import string
#import random 




def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def main():
    hex_dig = hash_with_sha256( "1089fhfulw") #This is how you hash a string with sha256''''
    print(hex_dig)
    
    

'''                
What generateHighValue does is that given a integer it would determine the max char length and give the highest value 
for eg give 5 it would return 99999    
   ''' 
    

def generateHighValue(y):
    
    i=0
    max = ""
    if y <=0:
        print("we need the max amount of charcters ")
    else:
        while i<y:
            max +="9"
            i+=1
        
        max = int(max)
    
        return max

'''
Given it a int generateLowValue will give the min least amount for eg 3 would return 100
'''
def generateLowValue(x):
    min = "1"
    i=0
    if x==1:
        min= 0
        return min 
    else:
        while i < x-1:
            min+="0"
            i+=1
        min = int(min)
        
        return min 


    




'''findPassword will find the password of the lists! it generates string integers like 999-0 in the first 
while generating special strings like 0012 in the secon while 

'''
    
    
def findPasword(row, highVal, lowVal, maxChar, minChar, temp):
    i = 0    
    
    if row <0:
        print("found all the passwords for the list ")
        
        
    else:
        i=lowVal
        while i<= highVal:
            password = str(i) + lines[row][1]
            
            hex_dig = hash_with_sha256(password) 
            if hex_dig == lines[row][2]:
                print(str(i) + " is the correct password to " + lines[row][0])
                break
            elif hex_dig!= lines[row][2] and i<highVal:
               
                i+=1
            else:
                
                i=0
               
                while i<=highVal:
                    maxdig = str(i)
                    me = maxdig.rjust(maxChar,'0')
                    password = me + lines[row][1]
                    hex_dig = hash_with_sha256(password) 
                    if hex_dig == lines[row][2]:
                        print(me + " is the correct password to " + lines[row][0])
                        #print("serching for next password")
                        break
                    elif hex_dig != lines[row][2] and i==highVal:
                        maxChar-=1
                
                        i=0
                        i+=1
                        
                    elif hex_dig != lines[row][2] and maxChar < minChar and i==highVal:
                        print("can't find password")
                        break 
                    else:
                        i +=1
            
                maxChar = temp
                break
                #findPasword(row-1, highVal, lowVal, maxChar, minChar, temp)
      
                
        print("searching for next password ")
        maxChar = temp
        findPasword(row-1, highVal, lowVal, maxChar, minChar, temp)
    
   
        
  


#main()
print("Hello I am porgrmam cp54 and my purpose is find all your passwords to your accounts.")
print("before we begin! Can I get the name of the file with your accounts.")
file= raw_input()

print("what is the minimum amount of characters that your password can have?")
minChar= input()
while(minChar< 0):
    minchar = input('Enter a positive integer> ')
    try:
        minchar= int(minchar)
    except ValueError:
        minchar=-1

print("What is the maximum amount of characters that your password can have? ")
maxChar = input()
while(maxChar< 0):
    maxChar = input('Enter a positive integer> ')
    try:
        maxChar = int(maxChar)
    except ValueError:
        maxChar=-1



with open(file) as textFile:
    lines = [line.strip().split(",") for line in textFile]

row = len(lines)-1


lowVal = generateLowValue(minChar)
highVal = generateHighValue(maxChar) 
temp = maxChar

#print(lowVal)
#print(highVal)
print("Generating passwords")

findPasword(row, highVal, lowVal, maxChar, minChar, temp)

print("ending program")
