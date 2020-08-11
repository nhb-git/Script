import os
import glob
import datetime
import argparse
import asyncio


def _argparse():
    """获取命令行参数"""
    # 定义接收参数的对象
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', dest='config', help="recv include path's file")
    parser.add_argument('-b', '--before', type=int, dest='before', default=30, help='delete file before days')
    args = parser.parse_args()
    return args


def get_dir_list(config_file, before):
    """从文件中获取目录列表"""
    try:
        dir_list = list()
        before_datetime = datetime.timedelta(days=before)
        now = datetime.datetime.now()
        with open(config_file.strip()) as f:
            for dir_name in f:
                dir_name = dir_name.strip()
                if os.path.isdir(dir_name):
                    for name in glob.glob(os.path.join(dir_name, '*')):
                        if os.path.isdir(name) and (
                                now-datetime.datetime.fromtimestamp(os.path.getctime(name)) > before_datetime):
                            dir_list.append(name)
        return dir_list
    except FileNotFoundError:
        print('文件不存在')
    except FileExistsError:
        print('文件有错误')


async def del_dir(dir_name):
    """删除指定天数前创建的目录"""
    proc = await asyncio.create_subprocess_shell(
        f'rm -rf {dir_name}', stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    await proc.communicate()
    print(f'{dir_name} 目录已被删除')


async def main():
    parser = _argparse()
    print(parser)
    dir_list = get_dir_list(parser.config, parser.before)
    print(dir_list)
    # for dir_name in dir_list:
    #     await del_dir(dir_name)


if __name__ == '__main__':
    asyncio.run(main())
