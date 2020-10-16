import xlwt, xlrd
from xlrd.timemachine import xrange

def main():
    filename = 'C:\\Users\\Vcvc\\Desktop\\aw.xlsx'
    rdata = xlrd.open_workbook(filename)
    """
    print(type(data))
    
    print('sheets nums:',rdata.nsheets)
    
    print('sheets names:', rdata.sheet_names())
    
    #行列nums
    sheet1 = rdata.sheet_by_index(0)
    print('rows:', sheet1.nrows)
    print('clos', sheet1.ncols)
    """

    # 显示内容 row行 col列
    sh1 = rdata.sheet_by_index(0)
    """
    print(sh1.row(0))
    print(sh1.row_values(1))
    
    print(sh1.col(0))
    print(sh1.col_values(0))
    #切片访问 第一列 1-3行
    print(sh1.col_values(0)[0:3])
    print(sh1.col_values(0, 0, 3))
    """

    """
    #获取单元格cell内容
    (
    
    XL_CELL_EMPTY,
    
    XL_CELL_TEXT,
    
    XL_CELL_NUMBER,
    
    XL_CELL_DATE,
    
    XL_CELL_BOOLEAN,
    
    XL_CELL_ERROR,
    
    XL_CELL_BLANK, # for use in debugging, gathering stats, etc
    
    ) = range(7)

    cell_0_0 = sh1.cell(0, 0)
    print(cell_0_0)
    print(cell_0_0.ctype)
    print(cell_0_0.value)

    cell_3_0 = sh1.cell(3, 0)
    print(cell_3_0)
    print(cell_3_0.ctype)
    print(cell_3_0.value)

    cell_7_0 = sh1.cell(4, 0)
    print(cell_7_0)
    print(cell_7_0.ctype)
    print(cell_7_0.value)
    """

    #写数据进表格
    wbook = xlwt.Workbook()
    wsheet = wbook.add_sheet('sh1')
    style = xlwt.easyxf('align: vertical center, horizontal center')

    wsheet.write(0, 0, u'A', style)
    wsheet.write(0, 1, u'B', style)
    wsheet.write(0, 2, u'C', style)
    wsheet.write(0, 3, u'D', style)
    wsheet.write(0, 4, u'总分', style)

    nc = sh1.ncols
    no = 4
    for row in xrange(1, 4):
        total = sum(sh1.col_values(row, 4))
        sh1.put_cell(row, no, xlrd.XL_CELL_NUMBER, total, None)

    wsheet.write(4, 4,sh1.cell_value(4, 4), style)

    try:
       wbook.save('C:\\Users\\Vcvc\\Desktop\\' + 'awz.xlsx')
    except:
        print("Save error")
    else:
        print('write excel file successful')
        
    #https://www.jianshu.com/p/ae01855198fb

if __name__ == '__main__':
    main()
