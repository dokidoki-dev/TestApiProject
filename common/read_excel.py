import xlrd
import os

file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Excel:
    """
    Excel操作类
    """
    @staticmethod
    def read(file_name: str, sheet_name: str, row: int):
        """
        读取excel数据,读取单行数据
        """
        x1 = xlrd.open_workbook(file_path + file_name).sheet_by_name(sheet_name)
        return x1.row_values(row)

    @staticmethod
    def reads(file_name: str, sheet_name: str, row_start: int, row_end: int):
        """
        读取excel文件，读取多行数据
        """
        x1 = xlrd.open_workbook(file_path + file_name).sheet_by_name(sheet_name)
        lists = []
        for i in range(row_start, row_end):
            lists.append(x1.row_values(i))
        return lists
