from loguru import logger
from time import strftime
import os, sys
from functools import wraps
import time


class LoggerManager:

    def __init__(self):
        self.logger = logger
        # 移除自带的logger控制台输出，防止重复打印日志信息
        logger.remove()
        filename = strftime("%Y%m%d-%H_%M_%S")
        log_file_path = os.path.join(os.getcwd(), "logs/", filename + '.log')
        print("log_file_path: ", log_file_path)
        log_format = '<green>{time: YYYY-MM-DD HH:mm:ss.SSS}</green> {level} {message}'
        level_ = 'DEBUG'
        rotation_ = '5MB'

        self.logger.add(log_file_path, enqueue=True, backtrace=True, diagnose=True,
                        encoding='utf-8', rotation=rotation_)

        """
            标准错误流sys.stderr：用于输出错误信息和警告，通常用于指示程序运行中的问题
        """
        self.logger.add(sys.stderr, format=log_format, enqueue=True, backtrace=True,
                        diagnose=True, colorize=True, level=level_)

    def runtime_logger(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(f"{func.__name__} 当前开始执行")
            now1 = time.time()
            try:
                func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f"{func.__name__} 当前用例执行失败, 失败原因是: {e}")
            now2 = time.time()
            self.logger.success(f"{func.__name__} 当前执行成功, 耗时: {now2 - now1}ms")

            return func

        return wrapper

    # 类的装饰器
    def runtime_logger_class(self, cls):
        for attr_name in dir(cls):
            if attr_name in dir(cls):
                if attr_name.startswith('test_') and callable(getattr(cls, attr_name)):
                    setattr(cls, attr_name, self.runtime_logger(getattr(cls, attr_name)))
        return cls


my_logger = LoggerManager()

if __name__ == '__main__':
    my_logger = LoggerManager()
