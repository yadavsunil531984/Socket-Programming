#!/usr/bin/env python
# coding: utf-8

# ## Consider Own machine as Client and Own Machine as server
Process To Run Programm
Step-1: Open New file in Jupyter give Name Server1
Step-2: Write Python code for Server1 Program.
Step-3: Save Server1 Program.
Step-4: Open New file in Jupyter give Name Client1
Step-5: Write Python code for Client1 Program.
Step-6: Save Client1 Program.
Step-7: Run Code of Server1 Program.
Step-8: Run Code of Client1 Program
# In[2]:


import socket as skt


# In[5]:


# Find the IP adress and Name of own PC
hostname = skt.gethostname()    
IPAddr = skt.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)  


# In[6]:


#TCP/IP Server
s=skt.socket(skt.AF_INET,skt.SOCK_STREAM)
s.bind(("192.168.1.101",5001))
s.listen(1)
c,addr=s.accept()
c.send(b"Hello Bro, How are you !")
c.close()

