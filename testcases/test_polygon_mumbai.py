import os
import allure
import pytest
import yaml
from apis.jsonrpc_api import JsonrpcApi
from loguru import logger
from common.handle_path import DATA_DIR
from common.utils import Utils
from common.handle_path import CONF_DIR

# 读取测试用例文件数据
case_data_path = os.path.join(DATA_DIR, 'case_data.yaml')
datas = yaml.safe_load(open(case_data_path, encoding='utf-8'))
# 读取配置文件数据
conf_path = os.path.join(CONF_DIR, 'config.yaml')
conf_data = Utils.handle_yaml(conf_path)  # 调用工具类封装的读取文件的方法
url = conf_data['url']['polygon_mumbai']


class TestPolygonMumbai(JsonrpcApi):
    """通过调用不同的业务，来完成相关测试"""

    # @pytest.mark.skip(reason="不执行该用例，还没写好！")  # 跳过用例
    @allure.feature('返回当前配置的链 ID')
    @pytest.mark.parametrize('data', datas['polygon_mumbai']['eth_chainId'])  # 读取测试用例文件数据实现参数化
    def test_eth_chainId(self, data):
        result = self.eth_chainId(url, **data['payload'])  # 解构,等价于self.eth_chainId(jsonrpc="xxx“,method="xxxx")
        Utils.assert_response_status(result)
        Utils.assert_equal(data['expected'], result.json())
        logger.info('用例通过！')

    @allure.feature('返回有关节点同步状态的信息')
    @pytest.mark.parametrize('data', datas['polygon_mumbai']['eth_syncing'])
    def test_eth_syncing(self, data):
        result = self.eth_syncing(url, **data['payload'])
        Utils.assert_response_status(result)
        Utils.assert_equal(data['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('根据区块编号返回关于区块的信息')
    @pytest.mark.parametrize('data', datas['polygon_mumbai']['eth_getBlockByNumber'])
    def test_eth_getBlockByNumber(self, data):
        result = self.eth_syncing(url, **data['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('根据哈希返回关于区块的信息')
    @pytest.mark.parametrize('data', datas['polygon_mumbai']['eth_getBlockByHash'])
    def test_eth_getBlockByHash(self, data):
        result = self.eth_getBlockByHash(url, **data['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('根据哈希返回关于区块的信息')
    @pytest.mark.parametrize('data', datas['polygon_mumbai']['eth_blockNumber'])
    def test_eth_getBlockByHash(self, data):
        result = self.eth_blockNumber(url, **data['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['expected'], result.json())
        logger.info('用例通过!')
