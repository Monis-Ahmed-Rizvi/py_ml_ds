#!/usr/bin/env python
# coding: utf-8

# # python crash course 

# ### Integer floats and arithmetic

# In[2]:


1.0 #float


# In[3]:


1+1


# In[4]:


print(2 * 3)
print(2-1)
print(1/2.0)
print(2**4)


# # order of operation

# In[5]:


print(2 + 3 * 5 + 5) #bidmas
print((2+3) * (5+5))


# # Modulo sign %

# In[6]:


4%2


# In[7]:


5%2


# In[8]:


8%2


# # variables and strings

# In[9]:


x_num = 5 # Assiging 
print(x_num)
x_num = x_num + x_num #re assingment
print(x_num) 

x_str = "hello World" # string assingment
dub_str = "hello world isn't" 
my_age = 25 # int
name = "pwnyoda" 
print(dub_str)
print("hello world iam {} my age is {}".format(name,my_age)) # formatting a string and printing variable with strings 
print("hello world my name is {n} and my age is {a}".format(n="Pwnyoda",a=23))

print(x_str[2])#indexing 
print(x_str[0:4]) # slicing the limit part is not included  [start:limit or end ]


# In[11]:


print(dub_str[5:10])


# # list 

# In[30]:


x_list = [10,20,30,['a','b','c',["hello","world"]],50] # creating list
x_list.append(60)         # appending to list
print(x_list)             # outputing list
x_list[1:4]               # slice
x_list[2] = 'M'           #reasingment
print(x_list)             # outputing 
print(x_list[3][3][0])


# # dictionaries

# In[22]:


x_dict = {'key1':'value'} # defining dictionary 
x_dict['key1'] = "val1" # reassinging value of a particular key
x_dict['key2'] = 34 # adding new key value in the dictionary 
x_dict['key3'] = [1,2,3,4] # list as value of the key
print(x_dict['key3'][0]) # accessing list value-pair and accessing a particular element from it   
x_dict['key4'] = {'k1':['k_val1','k_val2'],'m1':['m_val1','m_val2']} # nested dictionary with list key value pair 
print(x_dict['key4']['k1'][0])
x_dict_to_list = x_dict['key4']['k1'] # copying the list from the dictionary 
x_dict
x_dict_to_list


# # boolean

# In[18]:


True


# In[19]:


1


# In[20]:


False


# In[21]:


1==0


# # Tuple

# In[45]:


x_tup1 = (1,2,3,4,5) # creating tuple 
x_tup1[2] # accessing tuple 
# x_tup[1] = 99  not allowed tuples are immutable 
x_tup2 = (344,343,231,142)
x_tup1 = x_tup1 + x_tup2 # no new element can be added directly to a tuple on;y concatanation is possible 
x_tup1 = list(x_tup1) # converting a tuple to a list and inserting a element into it 
x_tup1.append(20) # inserting a new item 
print(type(x_tup1)) 
x_tup1 = tuple(x_tup1) # converting list back to tuple 
type(x_tup1)


# # set 

# In[54]:


x_set = {1,2,3,43,5,54,5,4,3,5,4,3,2} # no duplicates 
print(x_set)
# x_set[3] can not access particular item from a set 
x_set.add(50)
print(x_set)


# # comparison operator + logical operator

# In[8]:


print(1 > 2) # greater than operator
print(1 < 2) # lesser than operator
print(1==1)  # equal to operator 
print(1!=1)
print(1>2 or 1<2) # comparison operator with or (if one of the comparsion is correct the answer is true)
print(1>2 or 2<1) # both flase condition
print(1<2 and 2>1) # comparsion operator with and (both the conditions have to be true for it to be true other wise false )


#  # if else / elif

# In[12]:


a_int = int(input("enter a number"))

if a_int < 100:
    print("less")
else:
    print("More")


x_char = 'a'

choice = 'm'

if choice == 'a':
    print("a")
elif choice == 'b':
    print("b")
elif choice == 'm':
    print("m")


# In[ ]:




