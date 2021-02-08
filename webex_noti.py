
import requests

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'ZDc2ZDY0NjYtYzVlNC00MGY0LWI0NTItOThkZjRhZDIxZjFlYjViNWE1ZDctMDEw_P0A1_974dde6a-da6b-4f08-99e0-2e97dfbfbdac'
room_ID = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNWEwNzNjYzAtNmE0YS0xMWViLTllNjctNWYxYjVlZTU3Mjlh'

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }

body = { 'roomId': 'room_ID', 'text': 'Test notification 3 From Pyhton' }

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print( response.status_code )
print( response.text )
