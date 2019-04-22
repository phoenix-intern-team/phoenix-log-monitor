# import urllib.request
# import requests
# from requests.auth import HTTPProxyAuth
# import http.client

# def fetch_app_access_token(client_id, grant_type, scope, username, password):

#     # conn = http.client.HTTPSConnection("phoenix.default.philips.com")
#     proxyDict = { 
#             'http'  : '165.225.104.34:10015', 
#             'https' : '165.225.104.34:10015'
#         }
#     headers = {
#         'content-type': "application/x-www-form-urlencoded",
#         'cache-control': "no-cache",
#         # 'postman-token': "ba971cd4-c634-cd14-efe4-5c39e6bcb17c"
#     }

#     payload = {
#         'client_id': client_id,
#         'grant_type': grant_type,
#         'scope': scope,
#         'username': username,
#         'password': password
#     }
#     URL = "https://phoenix.default.philips.com/iam/api/v2.0/oauth2/token"
#     # conn.request("POST", "/iam/api/v2.0/oauth2/token", payload, headers)
   
#     response = requests.post(URL, params=payload, proxies=proxyDict, verify=False, headers=headers)

#     # res = conn.getresponse()
#     # data = res.read()
#     return response

# if __name__ == "__main__":
#     CLIENT_ID = "login"
#     GRANT_TYPE = "password"
#     SCOPE = "profile offline_access"
#     USERNAME = "superadmin"
#     PASSWORD = "Pass@1234"
#     res = fetch_app_access_token(CLIENT_ID, GRANT_TYPE, SCOPE, USERNAME, PASSWORD)
#     print(res)

import json, requests
proxyDict = { 
            'http'  : 'http://165.225.104.34:10015', 
            'https' : 'https://165.225.104.34:10015'
        }
data = { 'username' : 'superadmin', 'password' : 'Pass@1234' }
r = requests.post('https://phoenix.default.philips.com/iam/api/v2.0/oauth2/token', data=json.dumps(data), verify=False, proxies = proxyDict)
token = json.loads(r.text)['session']