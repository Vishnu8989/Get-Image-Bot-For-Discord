import shutil
import json  # to help in returned json files from http requests
import requests  # allow code to make http requests


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def get_pic(name):
    image_url = "https://source.unsplash.com/900x600/?random"
    if(name):
        image_url = "https://source.unsplash.com/900x600/?{}".format(name)
    print(name)
    response = requests.get(image_url, stream=True)
    file = open("test1.jpg", "wb")
    response.raw_decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response
