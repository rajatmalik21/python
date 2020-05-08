
# Python3 program to swap elements at given positions 
  
# Swap function 
def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
  
# Driver function 
List = [20, 07, 21, 07] 
pos1, pos2  = 1, 3
  
print(swapPositions(List, pos1-1, pos2-1)) 


"""

# Second program to swap elements 
# at given positions 
  
# Swap function 
def swapPositions(list, pos1, pos2): 
      
    # popping both the elements from list 
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    # inserting in each others positions 
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)   
      
    return list
  
# Driver function 
List = [20, 07, 21, 07] 
pos1, pos2  = 1, 3
  
print(swapPositions(List, pos1-1, pos2-1)) 
"""
