
from datetime import datetime
import shutil
import json  # to help in returned json files from http requests
import requests  # allow code to make http requests
import config


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def get_pic(name):
    image_url = "https://source.unsplash.com/3840x2160/?random"
    if(name):
        image_url = "https://source.unsplash.com/3840x2160/?{}".format(name)
    print(name)
    date_time = config.get_time()
    # print("Generator : "+date_time)
    response = requests.get(image_url, stream=True)
    image_name = name+"_" + date_time + ".jpg"
    # print("Generator : "+image_name)
    file = open(image_name, "wb")
    response.raw_decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response
