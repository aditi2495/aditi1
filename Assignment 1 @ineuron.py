#!/usr/bin/env python
# coding: utf-8
Question 1:Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 
# In[22]:


b = []
for i in range(2000,3000):
    if (i%7 ==0)  and (i%5 !=0):
        b.append(str(i))
      
print(','.join(b))

Question 2:Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
# In[ ]:


a = input("Enter your First-name : ")
b= input("Enter your Last-name : ")
print(b +" " + a)

Question 3:To calculate volume of sphere
# In[ ]:


def sphere_Volume(r):
    Volume = (4/3 * 22/7 * r**3)
    print("The volume of sphere is:",Volume)
    
    


# In[ ]:


sphere_Volume(6)


# In[ ]:




