import openpyxl
import math


def load_data(sheet, mapper):
    """
    从excel中读取原始数据，
    :param sheet: excel 工作表对象
    :param mapper : 数据映射
    :return: {"仓库编号":{"物料编号":[但前库存,月需求量,库存天数,需求量]}}
    """
    data_dict = {}
    row_index = 3
    while True:
        # 读取仓库编号
        warehouse_no = sheet.cell(row=row_index, column=1).value
        # 读取物料编号
        material_no = sheet.cell(row=row_index, column=1).value
        if not warehouse_no or not material_no:
            break
        if not mapper.__contains__(material_no):
            continue
        msg = mapper[material_no]
        if not data_dict.__contains__(warehouse_no):
            data_dict[warehouse_no] = {str(warehouse_no): {str(material_no): []}}
        # 获取当前库存
        stock = int(sheet.cell(row=row_index, column=4).value)
        # 获取月需求量
        forecast = int(sheet.cell(row=row_index, column=5).value)
        # 请求库存天数
        dos = int(math.ceil(float(stock) * 30 / float(forecast)))
        demand = 0  # 需求量
        if msg[1] > dos:
            demand = forecast * msg[2] - stock
        data_dict[warehouse_no][material_no] = list[stock, forecast, dos, demand]
    return data_dict


def record_data(sheet, result_data):
    """
    纪录处理结果数据
    :param sheet: 需要纪录数据当新工作表
    :param result_data: 结果数据
    :return:
    """
    pass


def compute_demand(raw_data, limit_line, months):
    """
    计算单一物料最大月需求量
    :param raw_data: 原始数据（仓库编号，物料编号，库存，月需）
    :param limit_line: 控制线，当库存天数不小于控制线时不参与分配
    :param months: 最大需要分配几个月当库存。
    :return:
    """
    pass


def count_max_demand(raw_data, limit_line, months):
    """
    计算单一物料最大需求量,sum(max(months*forecase-stock))
    :param raw_data: 原始数据（仓库编号，物料编号，库存，月需）
    :param limit_line: 控制线，当库存天数不小于控制线时不参与分配
    :param months: 最大需要分配几个月当库存。
    :return:
    """
    pass


def compute_count_average_dos(raw_data, allocation):
    """
    计算总共物料可供给天数均值
    :param raw_data: 原始数据
    :param allocation: 可分配物料数量
    :return:
    """
    pass


if __name__ == "__main__":
    # 物料字典，{"物料编号":[物料可分配量,当前物料可分配上限天数,物料最大供给月数]}
    material_dic = {"_1": [8, 45, 2], "_2": [20, 45, 1.5], "_3": [8, 45, 2]}
    # 加载excel文件
    wb = openpyxl.load_workbook("material.xlsx")
    input_sheet = wb['input']
    print("hello world!")
    print(math.ceil(2))
