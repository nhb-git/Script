# -*- coding: utf-8 -*-
import re
import requests


r = requests.get('http://louiszhai.github.io')
re.findall('"(https?://.*?)"', r.content.decode('utf-8'))
