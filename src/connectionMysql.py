'''
@coding: #-*- coding: utf-8 -*-
@Descripttion: 
@version: 
@Author: mumu
@Date: 2019-09-29 12:59:44
@LastEditors: mumu
@LastEditTime: 2019-09-29 18:38:43
'''
import xlrd
import pymysql
class connect():
    def __init__(self,data_base):
        self.data_base = data_base

    # 使用pymysql连接数据库
    def get_sqlconn(self):
        Conn=pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='1234',
            db=self.data_base,
            charset='utf8'
        )
        return Conn
    # 把数据从excel导入到数据库中
    def insert_excel(self,book_name):
        # 构造sql insert 语句
        query = 'insert into weibo(uid,name,gender,text)values(%s,%s,%s,%s)'
        # 打开数据所在的路径表名
        book = xlrd.open_workbook(book_name)
        # 这个是表里的sheet名称
        sheet = book.sheet_by_name('Sheet1')
        conn = self.get_sqlconn()
        cur = conn.cursor()
        for r in range(1, sheet.nrows):
            # (r, 0)表示第二行的0就是表里的A1:A1
            uid = sheet.cell(r, 6).value
            name = sheet.cell(r, 7).value
            gender = sheet.cell(r, 11).value
            text = sheet.cell(r, 2).value
            values = (uid, name, gender,text)
            #执行sql语句
            cur.execute(query, values)
            
        # close关闭文档
        cur.close()
        # commit 提交
        conn.commit()
        # 关闭MySQL链接
        conn.close()
        # 显示导入多少列
        columns = str(sheet.ncols)
        # 显示导入多少行
        rows = str(sheet.nrows)
        print('导入'+columns+'列'+rows+'行数据到MySQL数据库!')
    def read_weibo(self,name):
        f = open ('data/test.txt','w',encoding="utf-8")
        # 构造sql slect 语句
        query = "select text from weibo \
             where name = '%s'" %(name)
        conn = self.get_sqlconn()
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        for row in results:
            text = row[0]
            f.write(text+'\n')

            #print(text)
         # close关闭文档
        cur.close()
        # commit 提交
        conn.commit()
        # 关闭MySQL链接
        conn.close()
        f.close()
if __name__ == '__main__':
    data_base = 'test'
    conn = connect(data_base)
    person_name = '篮球之声'
    conn.read_weibo(person_name)
    # conn.insert_excel('data/微博数据.xlsx')
    