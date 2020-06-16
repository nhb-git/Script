# -*- coding: utf-8 -*-


import logging
from logging import handlers


# 生成logger
lg = logging.getLogger('web')
lg.setLevel(logging.DEBUG)

# 生成handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh = handlers.RotatingFileHandler('07 web.log', maxBytes=50, backupCount=3)
fh.setLevel(logging.WARNING)

## 绑定handler对象到logger对象
lg.addHandler(ch)
lg.addHandler(fh)

# 生成filter

# 生成format
f = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
ch.setFormatter(f)
fh.setFormatter(f)

lg.debug('debug log')
lg.warning('warning log')
