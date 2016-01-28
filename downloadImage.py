import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR3O1Nai4wbOkeSHT_LxCewPpFRB1UKMQM2AQoQ4RomREvOg4vGTrsSPvjo")
