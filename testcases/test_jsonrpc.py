import os
import allure
import pytest
import yaml
from apis.jsonrpc_api import JsonrpcApi
from loguru import logger
from common.handle_path import DATA_DIR
from common.utils import Utils

# 读取测试用例文件数据
case_data_path = os.path.join(DATA_DIR, 'case_data.yaml')
datas = yaml.safe_load(open(case_data_path, encoding='utf-8'))


class TestJsonrpc(JsonrpcApi):
    """通过调用不同的业务，来完成相关测试"""

    @allure.feature("polygon_mumbai")  # 定义模块
    @allure.description('获取当前配置的链 ID')  # 用例描述
    @pytest.mark.parametrize('data', datas['polygon_mumbai']['eth_chainId'])  # 读取测试用例文件数据实现参数化
    def test_eth_chainId(self, data):
        result = self.eth_chainId(**data['payload'])  # 解构,等价于self.eth_chainId(jsonrpc="xxx“,method="xxxx")
        Utils.assert_response_status(result)
        Utils.assert_equal(data['expected'], result.json())
        logger.info('用例通过！')

    @pytest.mark.polygon_mumbai
    @allure.feature('返回有关节点同步状态的信息')
    @allure.title('{data[title]}')
    @pytest.mark.parametrize('data', datas['polygon_mumbai']['eth_syncing'])
    def test_eth_syncing(self, data):
        result = self.eth_syncing(**data['payload'])
        Utils.assert_response_status(result)
        Utils.assert_equal(data['expected'], result.json())
        logger.info('用例通过!')

    @pytest.mark.skip(reason="不执行该用例，还没写好！")  # 跳过用例
    @pytest.mark.polygon_mumbai
    def test_eth_getBlockByNumber(self, data):
        result = self.eth_syncing(**data['payload'])
        Utils.assert_response_status(result)
        logger.info('用例通过!')
