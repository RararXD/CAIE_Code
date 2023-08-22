from .error import Error, StackError
from .options import *

error_messages = []
running_mod = 'file'  # file / line
running_path = ''  # 当前运行文件

# 变量
def __init__():
    global error_messages, running_mod
    error_messages = []
    running_mod = 'file'

def add_error_message(msg, obj):
    error_messages.append(Error(msg, obj))

def get_error_messages():
    return error_messages

def clear_error_messages():
    global error_messages
    error_messages = []

def add_stack_error_messages(msg):
    error_messages.append(StackError(msg))

def set_running_mod(mod):
    global running_mod
    running_mod = mod

def get_running_mod():
    return running_mod

def set_running_path(p):
    global running_path
    running_path = p

# 输出错误信息
def output_error():
    if not show_error:
        # 如果不显示错误信息
        # 清空错误并直接返回
        clear_error_messages()
        return

    l = list(set(get_error_messages()))
    if l:
        # 输出文件路径
        if running_path:
            print(f'File `{running_path}`: ')
        # 输出错误信息
        for i in l:
            print('\t', end='')
            i.raise_err()
        # 清空错误数组
        clear_error_messages()
