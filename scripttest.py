import requests
import base64
from urllib.parse import urlencode
import json

client_id = "af37f76b6c204b16b5f781ce1e54603d"
client_secret = "0b7da67cfaff4798b3644d23a1876ae6"


client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())
print(base64.b64decode(client_creds_b64).decode())
print(client_creds)
print(client_creds_b64.decode())




token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = {
    "grant_type":"client_credentials",
}
token_headers = {
    "Authorization" : f"Basic {client_creds_b64.decode()}",
}
token_data_enc = urlencode(token_data)

token_headers_json = json.dumps(token_headers)

r = requests.post(token_url,  data="grant_type=client_credentials", headers=token_headers)
print(r.status_code)