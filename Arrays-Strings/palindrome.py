#Check if an array is a palindrome
arr=[1,2,3,4,5,4,3,2,1]
if(arr==arr[::-1]):
    print("Palindrome")
else:
    print("Not a palindrome")
