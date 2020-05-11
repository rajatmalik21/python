  
# function which return reverse of a string 
'''def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
'''


def isPalindrome(s):
    # Run loop from 0 to len/2
    for i in range(0, (len(s) // 2)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# Driver code 
x = input("Enter a word to check if its a palindrome or not: ")
ans = isPalindrome(x)
  
if ans == 1: 
    print("Yes, this word is a palindrome")
else: 
    print("No, this word is not a palindrome")
