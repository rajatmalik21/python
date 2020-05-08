
# Python code to find the URL from an input string 
# Using the regular expression 
import re 
  
def Find(string): 
    # findall() has been used  
    # with valid conditions for urls in string 
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] 
    |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
    return url 
      
# Driver Code 
string = 'My Profile: https://auth.geeksforgeeks.org 
/ user / Friend % 20Rajat / articles in 
the portal of http://www.geeksforgeeks.org/' 
print("Urls: ", Find(string)) 
