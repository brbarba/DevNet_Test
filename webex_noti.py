
import requests
# documentation at https://developer.webex.com/docs/api/v1/messages/create-a-message

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'ZDc2ZDY0NjYtYzVlNC00MGY0LWI0NTItOThkZjRhZDIxZjFlYjViNWE1ZDctMDEw_P0A1_974dde6a-da6b-4f08-99e0-2e97dfbfbdac'
room_ID = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNWEwNzNjYzAtNmE0YS0xMWViLTllNjctNWYxYjVlZTU3Mjlh'
email_ID = 'gifbot@webex.bot'
httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }

body = { 'roomId': room_ID, 'text': 'Test notification 4\nusando room_ID como variable\nFrom Pyhton' }
#body = { 'toPersonEmail': 'gifbot@webex.bot', 'text': 'Hello' }

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print( response.status_code )
print( response.text )

messages = [
    '**Warning!!!**',
    '_Warning!!!_',
    '[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)'
    ]

for message in messages:

    body = { 'roomId': room_ID,, 'markdown': message }
    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

    print( response.status_code )
    print( response.text )
