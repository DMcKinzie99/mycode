#!/usr/bin/python3

import requests

URL= "http://api.open-notify.org/astros.json"

def main():
    # requests.get() requests info from the URL
    # .json() method transforms that data into a Pythonic dictionary!
    sliceme= requests.get(URL).json()

    print(sliceme)
    print(type(sliceme))

    print("People in Space:", sliceme['number'])
    for every_dict in sliceme["people"]:
        print(every_dict["name"])
main()
