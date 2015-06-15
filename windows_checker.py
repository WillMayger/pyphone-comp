from time import sleep
import requests
from options import options
while(True):
    s = requests.session()
    request = s.get('https://3f3a917a.ngrok.com/check/?pass=password')
    app = str(request._content).upper()
    options(app)
    sleep(1)


