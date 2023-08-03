import allure
import pytest
from loguru import logger
from common.utils import Utils
from apis.jsonrpc_api import JsonrpcApi

datas = JsonrpcApi.data


class TestKlaytnmainnet(JsonrpcApi):
    """通过调用不同的业务，来完成相关测试"""

    @allure.feature('eth_chainId')
    @allure.title('返回当前配置的链id')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])  # 读取测试用例文件数据实现参数化
    def test_eth_chainId(self, data):
        result = self.eth_chainId(data['url'], **data['eth_chainId']['payload'])  # 解构
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_chainId']['expected'], result.json())
        logger.info('用例通过！')

    @allure.feature('eth_syncing')
    @allure.title('返回有关节点同步状态的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_syncing(self, data):
        result = self.eth_syncing(data['url'], **data['eth_syncing']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_syncing']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBlockByNumber')
    @allure.title('根据区块编号返回关于区块的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBlockByNumber(self, data):
        result = self.eth_getBlockByNumber(data['url'], **data['eth_getBlockByNumber']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBlockByNumber']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBlockByHash')
    @allure.title('根据哈希返回关于区块的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBlockByHash(self, data):
        result = self.eth_getBlockByHash(data['url'], **data['eth_getBlockByHash']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBlockByHash']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_blockNumber')
    @allure.title('返回最新区块的编号')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_blockNumber(self, data):
        result = self.eth_blockNumber(data['url'], **data['eth_blockNumber']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_blockNumber']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_gasPrice')
    @allure.title('返回以 wei 为单位的当前 gas 价格')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_gasPrice(self, data):
        result = self.eth_gasPrice(data['url'], **data['eth_gasPrice']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_gasPrice']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBalance')
    @allure.title('返回给定地址的账户余额')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBalance(self, data):
        result = self.eth_getBalance(data['url'], **data['eth_getBalance']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBalance']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getLogs')
    @allure.title('返回与给定过滤器对象匹配的所有日志的数组')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getLogs(self, data):
        result = self.eth_getLogs(data['url'], **data['eth_getLogs']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getLogs']['expected'], result.json())
        logger.info('用例通过!')
