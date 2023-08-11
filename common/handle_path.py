"""路径处理，方便通过变量引用不同目录的路径"""

import os

# 获取当前文件的上一级目录，确定根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 构建配置文件的路径
CONF_DIR = os.path.join(BASE_DIR, "conf")  # 将多个路径组合成一个路径
CONFIG_DIR = os.path.join(CONF_DIR, 'config.yaml')
# 构建用例数据目录的路径
DATA_DIR = os.path.join(BASE_DIR, "data")
CASE_DIR = os.path.join(DATA_DIR, "case_data.yaml")
# 构建日志文件目录的路径
LOG_DIR = os.path.join(BASE_DIR, "log")
# 构建测试报告目录的路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")
