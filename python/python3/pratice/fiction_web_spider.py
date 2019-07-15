# -*- coding: utf-8 -*-
import requests


if __name__ == "__main__":
    target = "https://www.biqukan.com/1_1094/5403177.html"
    req = requests.get(url=target)
    print(req.text)
