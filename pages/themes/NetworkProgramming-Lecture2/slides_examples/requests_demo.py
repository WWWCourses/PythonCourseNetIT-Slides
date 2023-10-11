import requests


# requests.get() send the request and returns a Response Object:
response = requests.get('https://softwareacademy.bg/')

### We can access the request object from the response as:
print(response.request)

# Let's see the deafult headers sent:
print(response.request.headers)