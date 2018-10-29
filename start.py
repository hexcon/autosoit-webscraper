import requests
from bs4 import BeautifulSoup

phpsessid_token = None

#Get PHPSESSID
def getphptoken():
    s = requests.Session()
    data = s.get("http://autosoit.ee")
    c = data.cookies.get_dict()
    return c

def dofirstlogin():
    phpsessid_token = getphptoken()["PHPSESSID"]
    headers = {"G_ENABLED_IDPS" : "google",  "PHPSESSID" : phpsessid_token, "Referer" : "https://www.e-autokool.eu/",
    "Content-Type" : "application/x-www-form-urlencoded", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    url = "https://www.e-autokool.eu/"
    payload = "username=[username]&password=[password]&login=Sisene"
    login = requests.post(url, headers=headers, data=payload)
    print(login.text)

def getbookinglist():
    url="https://www.e-autokool.eu/?module=estudent&submodule=booking"
    headers = {"G_ENABLED_IDPS" : "google",  "PHPSESSID" : phpsessid_token, "Referer" : "https://www.e-autokool.eu/",
    "Content-Type" : "application/x-www-form-urlencoded", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
    payload = "starttime=29.10.2018&endtime=03.11.2018&region=N&teacher_ID=0&booking_type_ID=4&language=EST&choose=Vali"
    request = requests.get(url, headers=headers, data=payload)
    print(request.text())

def getfinaldata():
    soup = BeautifulSoup(data.text, "html.parser")
