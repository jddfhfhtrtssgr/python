import requests
   
# Making a GET request
r = requests.get('https://api.github.com/users/naveenkrnl')
  
# 200 code
print(r)
print(r.content)
