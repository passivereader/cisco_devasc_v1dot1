# pip install requests
# this is a Python interactive sesion >>> and not a script
# NOTE: neither the JSESSIONID cookie nor the CSRF token are safe to share
import requests, pprint, urllib3

# testing environments often use self-signed (or no) certificates
# this goes hand-in-hand with verify=False a few lines below
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
url = "https://sandbox-sdwan-2.cisco.com/j_security_check"
headers = {"Content-Type": "x-www-form-urlencoded"}
data = {"j_username": "devnetuser", "j_password": "the_password"}
r = session.post(url, headers=headers, data=data, verify=False)
r.text # output might indicate that login failed
# if login failed then login manually
# obtain JSESSIONID cookie via F12 - Storage in your browser

# obtain device list
dev_url = "https://sandbox-sdwan-2.cisco.com/dataservice/device"
dev_hdr = "{'Content-Type': 'application/json', 'Cookie': 'JSESSIONID=yadayada'}"
r = session.get(dev_url, headers=dev_hdr)
pprint.pprint(r.json())

# get CSRF prevention token (required for most POST operations)
csrf_hdr = "{'Content-Type': 'application/json', 'Cookie': 'JSESSIONID=yadayada'}"
csrf_url = "https://sandbox-sdwan-2.cisco.com/dataservice/client/token"
r = session.get(csrf_url, headers=csrf_hdr)
r.text # CSRF token output: '10CDCEEE...'
