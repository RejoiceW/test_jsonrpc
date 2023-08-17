import allure
import requests
from loguru import logger
import yaml


class Utils:
    """提供工具方法"""

    @classmethod
    def send_http(cls, data: dict):
        """
        发送http请求
        :param data: 请求数据
        :return:
        """
        try:
            Utils.__api_log(**data)  # 打印请求参数日志
            response = requests.request(**data)
            logger.info(f"响应结果为：{response.status_code}")
        except Exception as e:
            logger.error(f'发送请求失败，请求参数为：{data}')
            logger.exception(f'发生的错误为：{e}')
            raise e
        else:
            return response

    @classmethod
    def __api_log(cls, method, url, headers=None, params=None, json=None):
        """记录请求数据日志"""
        logger.info(f"请求方式：{method}")
        logger.info(f"请求地址：{url}")
        logger.info(f"请求头：{headers}")
        logger.info(f"请求参数：{params}")
        logger.info(f"请求体：{json}")
        # logger.error(f"请求方式：{method}")

    @classmethod
    def handle_yaml(cls, file_name):
        """
        读取yaml文件
        :param file_name:
        :return:
        """
        try:
            with open(file_name, encoding='utf-8') as file:  # 打开文件
                yaml_data = yaml.safe_load(file)  # 读取文件
        except Exception as e:  # 如果出现任何异常
            logger.error(f'yaml文件读取失败，文件名称：{file_name}')  # 记录错误日志
            raise e
        else:  # 如果没有发生异常
            return yaml_data

    @staticmethod
    @allure.step('step:断言')  # 测试用例的操作步骤
    def assert_response_status(response):
        """断言响应码"""
        try:
            assert response.status_code == 200
        except AssertionError as e:
            logger.error(f"eq断言失败，预期结果：200，实际结果：{response.status_code}")
            logger.error("用例失败！")
            raise e

    @staticmethod
    @allure.step('step:断言')
    def assert_equal(ex, re):
        """
        断言相等
        :param ex: 预期结果
        :param re: 实际结果
        :return:
        """
        try:
            assert str(ex) == str(re)
        except AssertionError as e:
            logger.error(f"eq断言失败，预期结果：{ex}，实际结果：{re}")
            logger.error("用例失败！")
            raise e

    @staticmethod
    @allure.step('step:断言')
    def assert_contains(content, target):
        """
        断言包含
        :param content: 文本内容
        :param target: 目标文本
        :return:
        """
        new_content = str(content).strip('{}')  # 去掉首尾括号
        try:
            assert new_content in str(target)
        except AssertionError as e:
            logger.error(f"contains断言失败，目标文本{target}，包含文本{new_content}")
            raise e
