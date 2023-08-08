### 项目结构说明

apis ---->接口层，单接口封装\
common ---->公共方法\
handle_path ---->路径处理\
utils ---->工具方法、断言封装\
wrapper ---->日志装饰器\
conf ---->配置文件\
data ---->测试数据\
log --->日志\
report --->测试报告\
testcases --->测试用例\
conftest --->前置条件处理\
pytest.ini --->pytest配置文件\
run.py --->测试用例运行主程序

### 测试报告
运行run.py后，当用例全部执行完毕，allure会自动收集测试报告到/report/html/中，打开index.html即可看到完整测试报告。