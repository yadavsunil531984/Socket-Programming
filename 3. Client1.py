#!/usr/bin/env python
# coding: utf-8

# ## Consider Own machine as Client and Own Machine as server

# In[1]:


import socket as skt


# In[2]:


# TCP/IP Client 

s = skt.socket(skt.AF_INET,skt.SOCK_STREAM)
s.connect(("192.168.1.101",5001))                      # IP Address of Server
msg=s.recv(1024)
print('Message from server are:'+msg.decode())
s.close()


# In[ ]:




