import requests

# base url
url = 'http://localhost:8000'

data = {
    'username':'python_course_test',
    'password':'python_course_test123'
}


# send request
response = requests.post(url, data=data)

# we can access the request object from the response as:
request = response.request

# Let's see the default headers and body sent:
print('Responce Headers: ', response.headers )
