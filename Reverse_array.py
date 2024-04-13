# Write a Python program to reverse an array.

def reverse_array(array):
  result=array[::-1]
  return result

array=input("enter your array seperated by spaces : ").split()
print(f"Reverse array is: {reverse_array(array)} ")