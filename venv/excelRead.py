import xlrd

# word = xlrd.open_workbook(r'K:\权益中心\工作交接\笔记文档\权益中心--天宫测试环境--数据库.xlsx')
# sheet = word.sheets()[0]
# # sheet = word.sheet_by_name('管理控制台')
# # sheet = word.sheet_by_index(0)
# sheet.ncols
# for i in range(1,sheet.nrows):
#     rows = sheet.row_values(i)  # 得到指定行的内容，列表形式返回
#     celvalue = sheet.cell(0,0).value
#     print(celvalue)


set1 = {1,2,3}

set2 = set1.copy()

print(set2)