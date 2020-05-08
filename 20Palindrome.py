  
# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = input("Enter a word to check if its a palindrome or not: ")
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes, this word is a palindrome")
else: 
    print("No, this word is not a palindrome")
