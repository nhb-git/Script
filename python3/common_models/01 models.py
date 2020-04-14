from asyncio.events import get_child_watcher as re_get_child_watcher
import sys as re_sys
import os as re_os


# print(re_os.getenv('PYTHON'))
# print(re_sys.path)
current_dir = re_os.getcwd()
# print(re_os.getcwd())
# print(re_os.listdir())
# print(re_os.path.isdir(current_dir))
# print(re_os.path.isfile(current_dir))
# print(re_os.path.isabs(current_dir))
# print(re_os.path.exists(current_dir))
# print(re_os.path.dirname(current_dir))
# print(re_os.path.abspath(current_dir))
# print(__file__)
# print(re_os.path.abspath(__file__))
# print(re_os.path.basename(current_dir))
# print(re_os.system('ls'))
# print(re_os.getenv('HOME'))
# print(re_os.environ)
# re_os.environ.setdefault('HOME', '/home/niu')
# print(re_os.getenv('HOME'))
# print(re_os.linesep)
# print(re_os.name)
# re_os.makedirs(new_dir)
# old_dir = r'D:\Github\Script\python3\common_models\test\test1\test2'
# new_dir = r'D:\Github\Script\python3\common_models\test\test1\test3'
# re_os.rename(old_dir, new_dir)

###### time 模块 ####
import time
# print(time.time())
# print(time.localtime())
# print(time.gmtime(time.time()))
# time.sleep(3)
# print(time.mktime(time.gmtime()))
# print(time.asctime(time.gmtime()))
# print(time.ctime())
# print(time.strftime('%Y-%m-%d %H:%M %p %j', time.localtime()))
# print(time.strptime('2020/04/08 12', '%Y/%m/%d %H'))
import datetime


# print(datetime.date.today())
# print(type(datetime.date.fromtimestamp(time.time())))
# print(datetime.datetime.fromtimestamp(time.time()))
# print(datetime.datetime.now())
t = datetime.datetime.now()
# print(t - datetime.timedelta(days=3))
print(t.replace(year=2015, month=10))
