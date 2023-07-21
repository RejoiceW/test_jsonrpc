"""完成测试数据的组装, 通过调用不同的接口来实现具体业务逻辑"""
import os
from common.handle_path import CONF_DIR
from common.utils import Utils


class JsonrpcApi:

    # 读取配置文件数据
    conf_path = os.path.join(CONF_DIR, 'config.yaml')
    conf_data = Utils.handle_yaml(conf_path)  # 调用工具类封装的读取文件的方法
    headers = conf_data['request_headers']['headers']

    def eth_chainId(self, url, **data):
        """返回当前配置的链 ID"""
        payload = {
            'url': url,
            'method': 'post',
            'headers': self.headers,
            'json':  data
        }
        response = Utils.send_http(payload)
        return response

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
    #
    # def eth_gasPrice(self):
    #     """返回以 wei 为单位的当前 gas 价格"""
    #     payload = {
    #         'url': self.host,
    #         'method': 'post',
    #         'headers': self.headers,
    #         'json': {"jsonrpc": "2.0", "method": "eth_gasPrice", "params": [], "id": 1}
    #     }
    #     response = Utils.send_http(payload)
    #     return response
    #
    # def eth_getBalance(self, address, tag):
    #     """返回给定地址的账户余额"""
    #     payload = {
    #         'url': self.host,
    #         'method': 'post',
    #         'headers': self.headers,
    #         'json': {"jsonrpc": "2.0", "method": "eth_getBalance", "params": [address, tag], "id": 1}
    #     }
    #     response = Utils.send_http(payload)
    #     return response
