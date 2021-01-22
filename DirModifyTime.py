from myfunc import func
from datetime import datetime
import time

cmd_dir_modify_time = []
my_dir = ['/install', '/home']
for my_dir_tmp in my_dir:
    cmd_dir_modify_time.append('find ' + my_dir_tmp + ' -mtime -3 -printf \'%CY%Cm%Cd,%CH:%CM,%p\n\'')
# print(cmd_dir_modify_time)


res = func.ssh('192.168.3.78', cmd_dir_modify_time)[0].split('\n')
modify_time = []
for res_tmp in res:
    # print(res_tmp.strip())
    time_string = res_tmp.strip().split(',')
    # print(time_string[0], time_string[1])
    # 将时间保存至字符串
    time_string = time_string[0] + ' ' + time_string[1]
    # 将时间字符串转换为时间数组
    time_array = time.strptime(time_string, '%Y%m%d %H:%M')
    # 将时间数组转换为时间戳
    time_stamp = int(time.mktime(time_array))
    modify_time.append(time_stamp)
# print(modify_time)
# 转换为时间戳后就可以通过list输出最大值
# print(max(modify_time))
# 将list中最大的时间戳转换为时间数组
time_array2 = time.localtime(max(modify_time))
# 将时间数组转换为时间字符串
time_string2 = time.strftime('%Y%m%d %H:%M:%S', time_array2)
print(time_string2)
