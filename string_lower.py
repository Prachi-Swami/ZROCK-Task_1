#Write a Python program to convert a string to lowercase.

def string_lower(string):
  result=string.lower()
  return result
string=input("please enter your string: ")
print(f" your lower string is : {string_lower(string)}")