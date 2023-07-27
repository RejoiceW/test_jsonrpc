"""集中管理固件，pytest 会自动调用"""
import pytest
from loguru import logger


# 标记测试任务的开始和结束
@pytest.fixture(scope='session', autouse=True)
def task_mark():
    logger.debug("{:=^50}".format('测试任务开始'))
    yield
    logger.debug("{:=^50}".format('测试任务结束'))


# 标记测试用例的开始和结束
@pytest.fixture(autouse=True)
def case_mark():
    logger.debug("{:=^50}".format('用例开始'))
    yield
    logger.debug("{:=^50}".format('用例结束'))
