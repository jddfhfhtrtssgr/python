import requests
   
# Making a GET request
r = requests.get('https://api.github.com/users/github')

print(r.content)
