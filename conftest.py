"""集中管理固件，pytest 会自动调用"""
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


@pytest.fixture(scope="session", autouse=True)
def get_env(pytestconfig):
    """获取命令行参数"""
    return pytestconfig.getoption("--env")


@pytest.fixture(scope="session")
def env(get_env):
    env = ''
    # 读取配置文件数据
    data = yaml.safe_load(open(CONFIG_DIR, encoding='utf-8'))
    if get_env == 'alphanet':
        env = data['url']['alphanet']
        logger.info(f'测试环境为：alphanet')
    elif get_env == 'testnet':
        env = data['url']['testnet']
    return env


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
