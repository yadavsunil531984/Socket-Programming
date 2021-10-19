#!/usr/bin/env python
# coding: utf-8

# # Types of addresses in PYTHON
# 

# In[6]:


import uuid as x


# In[7]:


# How to find mac Adress of our own PC
mac=x.getnode() 
print ("Physical adress in Decimal:",mac) 
print ("Physical adress in hex:",hex(mac))


# In[8]:


import socket as skt


# In[9]:


# How to find IP adress and Name of own PC
hostname = skt.gethostname()    
IPAddr = skt.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)  


# In[10]:


# How to find IP adress of Google
addr=skt.gethostbyname('www.google.com')
print("IP Adress="+addr)


# In[11]:


# How to find IP addres
ip=skt.gethostbyname("localhost")
print("IP adress are:",ip)


# In[15]:


# Find the service name from port number

a = skt.getservbyport(80, 'tcp')
print("Service for port 80 is:",a)

b = skt.getservbyport(25, 'tcp')
print("Service for port 25 is:",b)

c = skt.getservbyport(20, 'tcp')
print("Service for port 20 is:",c)


# In[ ]:


from socket import *
import time


# In[ ]:


# Port Scanning Note: It is illegal to Scan port of other PC

startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)

