#首先安装xlrd包    pip install xlrd
import xlrd
def xlxs_read(name,index):
    excel = xlrd.open_workbook(name)
    sheet = excel.sheets()[index]
    return sheet

if __name__ == '__main__':
    context = xlxs_read('2.xlsx',0)
    #context = xlxs_read(r'K:\PythonProjects\venv\test',0)   #也可以使用绝对路径，r表示字符串里的\不转义
    for i in range(1,context.nrows):
        rows = context.row_values(i)
        print(rows)
        print(rows[1])
        print(context.cell(0,0).value)