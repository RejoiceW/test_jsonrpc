from loguru import logger
import sys


def api_call(func):
    """
    接口调用记录
    :param func: 装饰的函数
    :return:
    """

    def inner(*args, **kwargs):
        # 输出到控制台的日志级别
        logger.remove()  # 删去import logger之后自动产生的handler，不删除的话会出现重复输出的现象
        handler_id = logger.add(sys.stderr, level="ERROR")  # 添加一个可以修改控制的handler
        logger.info(f"开始调用接口：{func.__name__}")
        res = func(*args, **kwargs)
        logger.info(f"结束调用接口：{func.__name__}")
        return res

    return inner
