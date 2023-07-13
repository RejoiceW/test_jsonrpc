import os
from common.handle_path import CONF_DIR
from common.utils import Utils


class JsonrpcApi:
    """完成测试数据的组装, 通过调用不同的接口来实现具体业务逻辑"""

    # 读取配置文件数据
    conf_path = os.path.join(CONF_DIR, 'config.yaml')
    conf_data = Utils().handle_yaml(conf_path)  # 调用工具类封装的读取文件的方法
    host = conf_data['env']['host'] + conf_data['env']['key']
    headers = conf_data['request_headers']['headers']

    def eth_chainId(self, **data):
        """返回当前配置的链 ID"""
        payload = {
            'url': self.host,
            'method': 'post',
            'headers': self.headers,
            'json':  data
        }
        response = Utils.send_http(payload)
        return response

    def eth_syncing(self, **data):
        """返回有关节点同步状态的信息"""
        payload = {
            'url': self.host,
            'method': 'post',
            'headers': self.headers,
            'json': data
        }
        response = Utils.send_http(payload)
        return response

    def get_logs(self, **data):
        """"""
        payload = {

        }
    # def eth_getBlockByNumber(self, tag, boolean):
    #     """
    #     按区块号返回区块信息
    #     :param tag: 区块号的整数，或最新"latest"
    #     :param boolean: 如果为真，则返回完整的交易对象，如果为假，则返回交易的哈希值
    #     :return: 块对象，没有找到时返回null
    #     """
    #     payload = {
    #         'url': self.host,
    #         'method': 'post',
    #         'headers': self.headers,
    #         'json': {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [tag, boolean], "id": 1}
    #     }
    #     response = Utils.send_http(payload)
    #     return response
    #
    # def eth_getBlockByHash(self, data, boolean):
    #     """通过哈希返回区块信息"""
    #     payload = {
    #         'url': self.host,
    #         'method': 'post',
    #         'headers': self.headers,
    #         'json': {"jsonrpc": "2.0", "method": "eth_getBlockByHash",
    #                  "params": [data, boolean], "id": 1}
    #     }
    #     response = Utils.send_http(payload)
    #     return response
    #
    # def eth_blockNumber(self):
    #     """返回最近块的编号"""
    #     payload = {
    #         'url': self.host,
    #         'method': 'post',
    #         'headers': self.headers,
    #         'json': {"jsonrpc": "2.0", "method": "eth_blockNumber", "params": [], "id": 1}
    #     }
    #     response = Utils.send_http(payload)
    #     return response
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
