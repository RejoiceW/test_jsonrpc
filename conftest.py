"""集中管理固件，pytest 会自动调用"""
import os
import pytest
import yaml
from loguru import logger
from common.handle_path import CONFIG_DIR


# 注册自定义参数 env 到配置对象
def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="alphanet",
        choices=['testnet', 'alphanet'],
        help="将命令行参数添加到 pytest 配置对象中"
    )


# 获取命令行参数
@pytest.fixture(scope="session", autouse=True)
def get_env(pytestconfig):
    return pytestconfig.getoption("--env")


# 根据命令行 --env 参数读取配置文件下不同环境数据
@pytest.fixture(scope="session")
def env(get_env):
    env = ''
    data = yaml.safe_load(open(CONFIG_DIR, encoding='utf-8'))  # 读取配置文件数据
    if get_env == 'alphanet':
        env = data['url']['alphanet']
        logger.info(f'测试环境为：alphanet')
    elif get_env == 'testnet':
        env = data['url']['testnet']
        logger.info(f'测试环境为：testnet')
    return env


# 标记测试任务的开始和结束
@pytest.fixture(scope='session', autouse=True)
def task_mark():
    logger.debug("======================测试任务开始======================")
    yield
    logger.debug("======================测试任务结束======================")


# 标记测试用例的开始和结束
@pytest.fixture(autouse=True)
def case_mark():
    logger.debug("======================用例开始======================")
    yield
    logger.debug("======================用例结束======================")


def pytest_sessionfinish(session):
    """在测试用例执行完成后执行"""
    # 从./report/json目录将生成的报告输出到./report/html目录中,-c用于在生成新报告之前清理先前的报告
    os.system('allure generate ./report/json -o ./report/html -c')
    # 浏览器打开生成测试报告
    os.system('allure open -h 127.0.0.1 -p 8883 ./report/html')
