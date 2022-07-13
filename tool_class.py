class ToolClass:
    @staticmethod
    def strToNumber(s):
        if s.find("万") != -1:
            s = float(s.replace("万", "")) * 10000
        elif s.find("亿") != -1:
            s = float(s.replace("亿", "")) * 100000000
        elif s.find("十万") != -1:
            s = float(s.replace("十万", "")) * 100000
        elif s.find("百万") != -1:
            s = float(s.replace("百万", "")) * 1000000
        elif s.find("千万") != -1:
            s = float(s.replace("千万", "")) * 10000000
        elif s.find("千") != -1:
            s = float(s.replace("千", "")) * 1000
        elif s.find("百") != -1:
            s = float(s.replace("千万", "")) * 100
        else:
            s = float(s)
        return s