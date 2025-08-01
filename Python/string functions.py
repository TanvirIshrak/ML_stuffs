details = "ishrak is a boy reads in PSTU cse department"

#string functions
print(len(details))  #it will print the number of characters that have
print(details.endswith("department"))  #return in true or false
print(details.count("i"))  #it will count ,how much times that char/word exist
print(details.capitalize())  #it will capitalize the first character of that string

print(details.find("boy"))
print(details.replace("reads","studies"))



#practicing by making a prompt and replace them using user input
letter =''' Dear |Name|
You are selcted!

Date : |date|'''

name = input("Enter your name:")
date = input("Enter today's date:")
letter = letter.replace("|Name|",name)
letter = letter.replace("|date|",date)

print(letter)
print()



def remove_and_strip(string,word):
    newStr = string.replace(word , "")  #(replace which one , by which)
    return newStr.strip()

this = "       Ishrak is bad      "
# print(this)
# print(this.strip())   #this function just removes unwanted spaces

n=remove_and_strip(this,"Ishrak")
print(n)