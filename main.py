import requests
   
# Making a GET request
r = requests.get('https://api.github.com/users/github')
  
# 200 code
print(r)
print(r.content)
