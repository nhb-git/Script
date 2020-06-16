import shutil


# 复制文件内容
# shutil.copyfile('02.txt', '02_copy.txt')

# 复制文件权限
# shutil.copymode(src='02.txt', dst='02_copy.txt')

# 复制文件状态，如文件time、flag
# shutil.copystat(src='02.txt', dst='02_copy.txt')

# 复制文件内容和文件权限
# shutil.copy(src='02.txt', dst='02_copy.txt')

# 复制文件内容和文件状态
# shutil.copy2('02.txt', '02_copy.txt')

# 复制目录
# shutil.copytree('test', 'test_copy', ignore=shutil.ignore_patterns('test1', 'test.py'))

# 压缩目录
# shutil.make_archive(
    # base_name='D:\Github\Script\python3\common_models1', format='gztar', root_dir='./test',
# )
import os
import zipfile


# zip压缩文件
# zip_object = zipfile.ZipFile(file='test_zip.zip', mode='w')
# zip_object.write('02 序列化.py')
# zip_object.write('02_copy.txt')
# filelist = []
# for root, dirname, files in os.walk('test'):
    # for file in files:
#         filelist.append(os.path.join(root, file))
# for file_path in filelist:
#     print(file_path)
#     zip_object.write(file_path)
# zip_object.close()

# zip解压文件
# zip_object = zipfile.ZipFile('test_zip.zip', mode='r')
# zip_object.extractall(path='./test/test1')
# zip_object.close()
