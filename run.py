import os
import pytest
from loguru import logger

if __name__ == '__main__':
    # 配置日志记录器，备份文件保留一周
    logger.add('./log/{time}.log', rotation='20 MB', retention='1 week', encoding='utf-8')
    # 调用pytest库的主函数 main()执行所有的pytest测试用例
    pytest.main(['-v', '-s', r"--alluredir=report/json", "--clean-alluredir"])
    # 从./report/json目录将生成的报告输出到./report/html目录中,-c用于在生成新报告之前清理先前的报告
    os.system('allure generate ./report/json -o ./report/html -c')

