# Auto_data_api
## 项目描述
项目的主要目的是解决接口参数场景多变，无法通过代码描述接口预期。通过固化数据源，固化接口预期。通过遍历接口测试用例开发前的结果，与开发后的接口对比，找到本次开发对接口造成影响的用例，
分析所造成影响的用例是符合本次开发需求预期，从而达到控制需求开发对接口造成的影响的目的。
## 项目介绍
### excel_server.py
用于写入接口请求结果（代码前和代码后）。脚本命令：python path/excel_server.py sheet_name json_date
sheet_name：测试用例excel的sheet名称。一般情况 ，一个excel可能有多个sheet，包含多个测试用例模块											
### execute_test.py
用于接口结果对比校验，提取数据有变化的测试用例。脚本命令：pthon  path/execute_test.py
### config.py
用于读取config.ini配置文件的脚本。配置文件中包括接口服务地址（host）、excel文件目录（path）及一些接口参数的公共配置（parameters）
### file_logging.py
用于日志写入的脚本
### jvm_server.py
用于调用Jar包（Java方法）的脚本
### tool_class.py
用于某些工具类
