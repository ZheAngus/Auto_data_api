import jpype
import time
import os

from file_logging import Logger

# jvmPath = jpype.getDefaultJVMPath()
# jpype.startJVM(jvmPath)
# jpype.java.lang.System.out.println("hello world!")
# jpype.shutdownJVM()

class JvmServer:
    def open_JVM(self):
        # jar_path = os.path.join(os.path.abspath('.'), r'E:\Jmter_Project\tool_jar\custools-sign.jar')   # jar包路径
        # jvmPath_32 = r'D:\Program Files\Java\jdk1.8.0_201\jre\bin\server\jvm.dll'     # jre路径
        Logger.logger().debug("虚拟机运行状态：{JVMstart}".format(JVMstart=jpype.isJVMStarted()))
        # print("虚拟机运行状态：{JVMstart}".format(JVMstart=jpype.isJVMStarted()))
        if jpype.isJVMStarted() is False:
            Logger.logger().debug("虚拟机未运行，启动虚拟机，直接调用Jar包")
            # print("虚拟机未运行，启动虚拟机，直接调用Jar包")
            jvmPath = jpype.getDefaultJVMPath()
            jpype.startJVM(jvmPath, '-Djava.class.path=tool\custools-sign.jar')  # 启动虚拟机
            Logger.logger().debug("虚拟机启动，等待5s！")
            # print("虚拟机启动，等待5s！")
            time.sleep(5)
        Logger.logger().debug("虚拟机已运行，可直接调用Jar包")
        # print("虚拟机已运行，可直接调用Jar包")

    def get_data_api_header(self):
        JPackage = jpype.JPackage('com.study.md5s.hearderss')
        difference = JPackage.Md5Password.getHesders()
        header = {}
        header["flag"] = str(difference.get("flag"))
        header["appid"] = str(difference.get("appid"))
        header["sign"] = str(difference.get("sign"))
        header["nonce"] = str(difference.get("nonce"))
        header["timestamp"] = str(difference.get("timestamp"))
        header["Content-Type"] = "application/json;charset=UTF-8"
        header["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"

        return header

    def close_JVM(self):
        Logger.logger().debug("关闭虚拟机")
        # print("关闭虚拟机")
        jpype.shutdownJVM()  # 关闭虚拟机

if __name__ == '__main__':
    JVMServer = JvmServer()
    JVMServer.open_JVM()
    header = JVMServer.get_data_api_header()
    JVMServer.close_JVM()
    print(header)