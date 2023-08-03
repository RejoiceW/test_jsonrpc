"""完成测试数据的组装, 通过调用不同的接口来实现具体业务逻辑"""

import os
import yaml
from common.handle_path import CONF_DIR, DATA_DIR
from common.utils import Utils
from common.wrapper import api_call


class JsonrpcApi:
    # 读取配置文件数据
    conf_path = os.path.join(CONF_DIR, 'config.yaml')
    conf_data = Utils.handle_yaml(conf_path)  # 调用工具类封装的读取文件的方法
    headers = conf_data['request_headers']['headers']
    # 读取测试用例文件数据
    # case_data_path = os.path.join(DATA_DIR, 'testnet_case_data.yaml')  # 测试环境
    case_data_path = os.path.join(DATA_DIR, 'alphanet_case_data.yaml')  # 正式环境
    data = yaml.safe_load(open(case_data_path, encoding='utf-8'))

    @api_call
    def eth_chainId(self, url, **data):
        """返回当前配置的链 ID"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_syncing(self, url, **data):
        """返回一个对象，其中包含有关同步状态的数据或 false"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getBlockByNumber(self, url, **data):
        """根据区块编号返回关于区块的信息"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getBlockByHash(self, url, **data):
        """根据哈希返回区块信息"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getBlockReceipts(self, url, **data):
        """获取给定区块的所有交易数据"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_blockNumber(self, url, **data):
        """返回最新区块的编号"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_gasPrice(self, url, **data):
        """返回以 wei 为单位的当前 gas 价格"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getBalance(self, url, **data):
        """返回给定地址的账户余额"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getTransactionByHash(self, url, **data):
        """返回关于按交易哈希请求的交易的信息"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getTransactionByBlockHashAndIndex(self, url, **data):
        """根据区块哈希和交易索引位置返回关于交易的信息"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getTransactionByBlockNumberAndIndex(self, url, **data):
        """根据区块编号和交易索引位置返回关于交易的信息"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getTransactionReceipt(self, url, **data):
        """根据交易哈希返回交易的收据"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getTransactionCount(self, url, **data):
        """返回从一个地址发送的交易数量"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getBlockTransactionCountByHash(self, url, **data):
        """返回匹配给定区块哈希的区块中的交易数量"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getBlockTransactionCountByNumber(self, url, **data):
        """返回匹配给定区块编号的区块中的交易数量"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getLogs(self, url, **data):
        """返回与给定过滤器对象匹配的所有日志的数组"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getCode(self, url, **data):
        """返回位于给定地址的代码"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_call(self, url, **data):
        """立即执行新的消息调用，而不在区块链上创建交易"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_batchCall(self, url, **data):
        """批量执行消息调用"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getStorageAt(self, url, **data):
        """从给定地址的存储位置返回值"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_estimateGas(self, url, **data):
        """生成并返回允许交易完成所需燃料数量的估算值"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_newFilter(self, url, **data):
        """基于过滤器选项创建一个过滤器对象，以在状态更改（日志）时发出通知"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_newBlockFilter(self, url, **data):
        """在节点中创建一个过滤器，以在新区块到达时发出通知"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_newPendingTransactionFilter(self, url, **data):
        """在节点中创建一个过滤器，以在新的待处理交易到达时发出通知"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def eth_getFilterChanges(self, url, **data):
        """过滤器的轮询方法，会返回自上次轮询以来产生的日志数组"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def net_version(self, url, **data):
        """返回当前网络 id"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def net_listening(self, url, **data):
        """如果客户端正在主动监听网络连接，则返回 true"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def net_peerCount(self, url, **data):
        """返回当前连接到客户端的对等点数"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    @api_call
    def web3_clientVersion(self, url, **data):
        """返回当前客户端版本"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response
