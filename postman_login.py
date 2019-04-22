import http.client
import ssl


# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     # Legacy Python that doesn't verify HTTPS certificates by default
#     pass
# else:
#     # Handle target environment that doesn't support HTTPS verification
#     ssl._create_default_https_context = _create_unverified_https_context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.check_hostname = False
conn = http.client.HTTPConnection("161.85.111.217")

payload = "client_id=login&grant_type=password&scope=profile%20offline_access&username=superadmin&password=Pass%401234"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    # 'postman-token': "ba971cd4-c634-cd14-efe4-5c39e6bcb17c"
    }

conn.request("POST", "/iam/api/v2.0/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))