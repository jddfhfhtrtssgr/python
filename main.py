# import random


import requests
   
# Making a GET request
r = requests.get('https://api.github.com/users/naveenkrnl')
  
# check status code for response received
print(r)
print(r.content)
