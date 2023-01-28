import requests
   
# Making a post request
r = requests.get('https://api.github.com/users/github')

print(r.content)
