import logging

class Logger:

    @staticmethod
    def logger():

        logger = logging.getLogger('test_logger')

        logger.setLevel(logging.DEBUG)

        # 判断当前日志对象中是否有处理器，如果没有，添加处理器
        if not logger.handlers:
            # fh为文件处理，输出日志至文件
            fh = logging.FileHandler(r'log\test.log', 'a', encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            formateer = logging.Formatter('%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s -%(process)s')
            fh.setFormatter(formateer)
            logger.addHandler(fh)

            # sh为控制台处理器，输出日志至控制台
            sh = logging.StreamHandler()
            sh.setFormatter(formateer)
            logger.addHandler(sh)

        return logger

if __name__ == "__main__":
    logger = Logger().logger()
    logger.debug('-----调试信息[debug]-----')
    logger.info('[info]')
    logger.warning('警告xinxi[warning]')
    logger.error('错误信息[error]')
    logger.critical('严重错误信息[crtical]')