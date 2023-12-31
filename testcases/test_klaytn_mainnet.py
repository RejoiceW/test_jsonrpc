import allure
import pytest
from loguru import logger
from common.utils import Utils
from apis.jsonrpc_api import JsonrpcApi


@pytest.mark.klaytn_mainnet
class TestKlaytnMainnet(JsonrpcApi):
    """通过调用不同的业务，来完成相关测试"""

    datas = JsonrpcApi.data

    @allure.feature('eth_chainId')
    @allure.story('返回当前配置的链id')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_chainId(self, env, data):
        result = self.eth_chainId(env['klaytn_mainnet'], **data['eth_chainId']['payload'])  # 解构
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_chainId']['expected'], result.json())
        logger.info('用例通过！')

    @allure.feature('eth_syncing')
    @allure.story('返回有关节点同步状态的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_syncing(self, env, data):
        result = self.eth_syncing(env['klaytn_mainnet'], **data['eth_syncing']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_syncing']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBlockByNumber')
    @allure.story('根据区块编号返回关于区块的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBlockByNumber(self, env, data):
        result = self.eth_getBlockByNumber(env['klaytn_mainnet'], **data['eth_getBlockByNumber']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBlockByNumber']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBlockByHash')
    @allure.story('根据哈希返回关于区块的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBlockByHash(self, env, data):
        result = self.eth_getBlockByHash(env['klaytn_mainnet'], **data['eth_getBlockByHash']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBlockByHash']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_blockNumber')
    @allure.story('返回最新区块的编号')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_blockNumber(self, env, data):
        result = self.eth_blockNumber(env['klaytn_mainnet'], **data['eth_blockNumber']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_blockNumber']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_gasPrice')
    @allure.story('返回以 wei 为单位的当前 gas 价格')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_gasPrice(self, env, data):
        result = self.eth_gasPrice(env['klaytn_mainnet'], **data['eth_gasPrice']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_gasPrice']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBalance')
    @allure.story('返回给定地址的账户余额')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBalance(self, env, data):
        result = self.eth_getBalance(env['klaytn_mainnet'], **data['eth_getBalance']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBalance']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getTransactionByHash')
    @allure.story('返回关于按交易哈希请求的交易的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getTransactionByHash(self, env, data):
        result = self.eth_getTransactionByHash(env['klaytn_mainnet'], **data['eth_getTransactionByHash']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getTransactionByHash']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getTransactionByBlockHashAndIndex')
    @allure.story('根据区块哈希和交易索引位置返回关于交易的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getTransactionByBlockHashAndIndex(self, env, data):
        result = self.eth_getTransactionByBlockHashAndIndex(env['klaytn_mainnet'],
                                                            **data['eth_getTransactionByBlockHashAndIndex']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getTransactionByBlockHashAndIndex']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getTransactionByBlockNumberAndIndex')
    @allure.story('根据区块编号和交易索引位置返回关于交易的信息')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getTransactionByBlockNumberAndIndex(self, env, data):
        result = self.eth_getTransactionByBlockNumberAndIndex(env['klaytn_mainnet'],
                                                              **data['eth_getTransactionByBlockNumberAndIndex'][
                                                                  'payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getTransactionByBlockNumberAndIndex']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getTransactionReceipt')
    @allure.story('根据交易哈希返回交易的数据')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getTransactionReceipt(self, env, data):
        result = self.eth_getTransactionReceipt(env['klaytn_mainnet'], **data['eth_getTransactionReceipt']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getTransactionReceipt']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getTransactionCount')
    @allure.story('返回从一个地址发送的交易数量')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getTransactionCount(self, env, data):
        result = self.eth_getTransactionCount(env['klaytn_mainnet'], **data['eth_getTransactionCount']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getTransactionCount']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBlockTransactionCountByHash')
    @allure.story('返回从一个地址发送的交易数量')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBlockTransactionCountByHash(self, env, data):
        result = self.eth_getBlockTransactionCountByHash(env['klaytn_mainnet'],
                                                         **data['eth_getBlockTransactionCountByHash']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBlockTransactionCountByHash']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getBlockTransactionCountByNumber')
    @allure.story('返回匹配给定区块编号的区块中的交易数量')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getBlockTransactionCountByNumber(self, env, data):
        result = self.eth_getBlockTransactionCountByNumber(env['klaytn_mainnet'],
                                                           **data['eth_getBlockTransactionCountByNumber']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getBlockTransactionCountByNumber']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getLogs')
    @allure.story('返回与给定过滤器对象匹配的所有日志的数组')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getLogs(self, env, data):
        result = self.eth_getLogs(env['klaytn_mainnet'], **data['eth_getLogs']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getLogs']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getCode')
    @allure.story('返回位于给定地址的代码')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getCode(self, env, data):
        result = self.eth_getCode(env['klaytn_mainnet'], **data['eth_getCode']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getCode']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_call')
    @allure.story('立即执行新的消息调用，而不在区块链上创建交易')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_call(self, env, data):
        result = self.eth_call(env['klaytn_mainnet'], **data['eth_call']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_call']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getStorageAt')
    @allure.story('从给定地址的存储位置返回值')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getStorageAt(self, env, data):
        result = self.eth_getStorageAt(env['klaytn_mainnet'], **data['eth_getStorageAt']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getStorageAt']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_estimateGas')
    @allure.story('生成并返回允许交易完成所需燃料数量的估算值')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_estimateGas(self, env, data):
        result = self.eth_estimateGas(env['klaytn_mainnet'], **data['eth_estimateGas']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_estimateGas']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_newFilter')
    @allure.story('基于过滤器选项创建一个过滤器对象，以在状态更改（日志）时发出通知')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_newFilter(self, env, data):
        result = self.eth_newFilter(env['klaytn_mainnet'], **data['eth_newFilter']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_newFilter']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_newBlockFilter')
    @allure.story('在节点中创建一个过滤器，以在新区块到达时发出通知')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_newBlockFilter(self, env, data):
        result = self.eth_newBlockFilter(env['klaytn_mainnet'], **data['eth_newBlockFilter']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_newBlockFilter']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_newPendingTransactionFilter')
    @allure.story('在节点中创建一个过滤器，以在新的待处理交易到达时发出通知')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_newPendingTransactionFilter(self, env, data):
        result = self.eth_newPendingTransactionFilter(env['klaytn_mainnet'], **data['eth_newPendingTransactionFilter']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_newPendingTransactionFilter']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('eth_getFilterChanges')
    @allure.story('过滤器的轮询方法，会返回自上次轮询以来产生的日志数组')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_eth_getFilterChanges(self, env, data):
        result = self.eth_getFilterChanges(env['klaytn_mainnet'], **data['eth_getFilterChanges']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['eth_getFilterChanges']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('net_version')
    @allure.story('返回当前网络 id')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_net_version(self, env, data):
        result = self.net_version(env['klaytn_mainnet'], **data['net_version']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['net_version']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('net_listening')
    @allure.story('如果客户端正在主动监听网络连接，则返回 true')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_net_listening(self, env, data):
        result = self.net_listening(env['klaytn_mainnet'], **data['net_listening']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['net_listening']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('net_peerCount')
    @allure.story('返回当前连接到客户端的对等点数')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_net_peerCount(self, env, data):
        result = self.net_peerCount(env['klaytn_mainnet'], **data['net_peerCount']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['net_peerCount']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('web3_clientVersion')
    @allure.story('返回当前客户端版本')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_web3_clientVersion(self, env, data):
        result = self.web3_clientVersion(env['klaytn_mainnet'], **data['web3_clientVersion']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['web3_clientVersion']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('web3_sha3')
    @allure.story('返回给定数据的 Keccak-256')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_web3_sha3(self, env, data):
        result = self.web3_sha3(env['klaytn_mainnet'], **data['web3_sha3']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['web3_sha3']['expected'], result.json())
        logger.info('用例通过!')

    @allure.feature('txpool_status')
    @allure.story('返回当前待包含在下一个块中的交易数量，以及计划仅在将来执行的交易数量')
    @pytest.mark.parametrize('data', [datas['klaytn_mainnet']])
    def test_txpool_status(self, env, data):
        result = self.txpool_status(env['klaytn_mainnet'], **data['txpool_status']['payload'])
        Utils.assert_response_status(result)
        Utils.assert_contains(data['txpool_status']['expected'], result.json())
        logger.info('用例通过!')