#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 7
y = x/3
z = x == 7
s = "Hello python programmer!"
type(x)


# In[2]:


type(y)


# In[3]:


type(z)


# In[4]:


type(s)


# In[5]:


quantity = 2
price = 10.5
text = f"I want to pay {quantity} riyals for {price} pieces of this item."
print(text)


# In[7]:


def bigger_than_10():      
    if x >= 10:
                print(f"{x} is bigger than 10")
    else:
                print(f"{x} is less than 10")
                print(" bigger_than_10(19)")    
     


# In[8]:



     fruites = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
     fruites[-2:]


# In[11]:


fruites = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for x in fruites:
         print(x)


# In[10]:


colors = {
  "blue": "0000FF",
  "green": "00FF00",
  "yellow": "FFFF00",
  "red": "FF0000",
  "white": "unknown",
  "Black":"000000" ,
}
del colors['white']
colors1 = {"White": "FFFFFF"}
colors1.update(colors)
print(colors1)


# In[3]:


def exchange_values(lista):
    colors = {
  "blue": "0000FF",
  "green": "00FF00",
  "yellow": "FFFF00",
  "red": "FF0000",
  "white": "unknown",
  "Black":"000000" 
}
    print("write a color")
    i = input()
    print('value ', colors.get(i))
    lista = ['blue', 'white', 'black', 'yellow', 'green', 'red']
    lista2 =['0000FF','FFFFFF','000000','FFFF00','00FF00','FF0000']
    print(listToDict(lsta, lsta2))
    print(exchange_values(lista))


# In[ ]:




