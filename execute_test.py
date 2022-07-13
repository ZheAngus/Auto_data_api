import json_tools
import json
import sys
from jsonsearch import JsonSearch

from config import ConfigOperation
from file_logging import Logger
from excel_server import ExcelServer
from tool_class import ToolClass


class RunTest:
    def json_diff(self, wb, sheet):
        row_index = 2
        case_index = 1
        while row_index <= sheet.max_row:
            result_json = json.loads(sheet.cell(row=row_index, column=15).value)  # 接口返回结果
            expect_json = json.loads(sheet.cell(row=row_index, column=13).value)  # 期望返回结果
            result = json_tools.diff(result_json, expect_json)  # Json对比结果
            Logger.logger().debug("第{case_index}条用例Json对比结果：{result}".format(result=result, case_index=case_index))
            # print("第{case_index}条用例Json对比结果：{result}".format(result=result, case_index=case_index))
            if len(result) == 1 and result[0]["replace"] == "/timestamp":
                sheet.cell(row=row_index, column=17).value = "pass"
            else:
                sheet.cell(row=row_index, column=17).value = str(result)
            try:
                wb.save(ConfigOperation.read_config().get("file", "path"))
            except Exception as e:
                Logger.logger().error(e)
            row_index = row_index + 1
            case_index = case_index + 1

    def target_diff(self, target_name, wb, sheet):
        row_index = 2
        case_index = 1
        while row_index <= sheet.max_row:
            result_json = json.loads(sheet.cell(row=row_index, column=15).value)  # 接口返回结果
            if target_name == "gpRat":
                jsondata = JsonSearch(object=result_json, mode='j')
                jsonlist = jsondata.search_all_path(key=target_name)
                for jd in jsonlist:
                    jsonbase = result_json[jd[0]][jd[1]][jd[2]][jd[3]]
                    if "saleAmt" in jsonbase:
                        saleAmt = ToolClass.strToNumber(jsonbase["saleAmt"])
                        if saleAmt == 0:
                            if float(jsonbase[target_name]) == 0:
                                print("通过")
                            else:
                                print(jd)
                                print("============")
                                print(sheet.cell(row=row_index, column=2).value)
                        else:
                            # print(jsonbase["saleAmt"])
                            # print(jsonbase["gpAmt"])
                            # print(jsonbase[target_name])
                            # print("-------------------")
                            # print(jsonbase["saleAmt"].find("万"))

                            # gpAmt = float(jsonbase["gpAmt"].replace("万", "")) * 10000 if jsonbase["gpAmt"].find(
                            #     "万") != -1 else float(jsonbase["gpAmt"])
                            gpAmt = ToolClass.strToNumber(jsonbase["gpAmt"])
                            # gpRat = float(jsonbase[target_name].replace("万", "")) * 10000 if jsonbase[target_name].find(
                            #     "万") != -1 else float(jsonbase[target_name])
                            gpRat = ToolClass.strToNumber(jsonbase[target_name])
                            # print(sheet.cell(row=row_index, column=2).value)
                            # print(saleAmt)
                            # print(gpAmt)
                            # print(gpRat)
                            # print(round(gpAmt / saleAmt * 100, 2))
                            if gpRat == round(gpAmt / saleAmt * 100, 2):
                                print("通过")
                            else:
                                print(jd)





            # expect_json = json.loads(sheet.cell(row=row_index, column=13).value)  # 期望返回结果
            # result = json_tools.diff(result_json, expect_json)  # Json对比结果
            # Logger.logger().debug("第{case_index}条用例Json对比结果：{result}".format(result=result, case_index=case_index))
            # # print("第{case_index}条用例Json对比结果：{result}".format(result=result, case_index=case_index))
            # if len(result) == 1 and result[0]["replace"] == "/timestamp":
            #     sheet.cell(row=row_index, column=17).value = "pass"
            # else:
            #     sheet.cell(row=row_index, column=17).value = str(result)
            # try:
            #     wb.save(ConfigOperation.read_config().get("file", "path"))
            # except Exception as e:
            #     Logger.logger().error(e)
            row_index = row_index + 1
            # case_index = case_index + 1



if __name__ == "__main__":
    excel_server = ExcelServer()
    wb = excel_server.open_excel()
    runt = RunTest()
    # runt.json_diff(wb, wb[sys.argv[1]])
    runt.target_diff("gpRat", wb, wb["【总经理驾驶室】经营分析【实时】"])
    print('')