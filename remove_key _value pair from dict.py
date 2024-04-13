#4. Write a Python program to remove a key-value pair from a dictionary.
def remove_key_value(dict,key):
  if key in dict:
   del dict[key]
   return dict
dict={"roll_no":1,"name":"prachi","age":26}
print(dict)
key=input("Enter key for remove : ")
print(f" Your dictionary is {dict}\n After removed  key {key} dictionary is { remove_key_value(dict,key)}")