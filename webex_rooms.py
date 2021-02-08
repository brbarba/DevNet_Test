
import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'ZDc2ZDY0NjYtYzVlNC00MGY0LWI0NTItOThkZjRhZDIxZjFlYjViNWE1ZDctMDEw_P0A1_974dde6a-da6b-4f08-99e0-2e97dfbfbdac'

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
queryParams = { 'sortBy': 'lastactivity', 'max': '2' }
response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams )
print( response.status_code )
 print( response.text )
 
