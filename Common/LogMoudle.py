# encoding:utf-8

import logging
import sys
import threading


Lock = threading.Lock()

class LogSingleton():
    __LogInstance = None

    def __init__(self):

        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__LogInstance:
            try:
                Lock.acquire()
                # double check
                if not cls.__LogInstance:
                    print("test")
                    cls.__LogInstance = logging.getLogger()
            finally:
                Lock.release()
        return cls.__LogInstance

def SetLog():
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

    # 文件日志
    file_handler = logging.FileHandler("test.log")
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值

    # 为logger添加的日志处理器
    logging.addHandler(file_handler)
    logging.addHandler(console_handler)
    # 指定日志的最低输出级别，默认为WARN级别
    logging.setLevel(logging.INFO)


def test():
    log = LogSingleton()
    SetLog()
    log.info("buyunhui")









def test():

    log = LogSingleton()
    log.warning("test")


def func():
    pass

test()


