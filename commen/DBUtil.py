# coding=utf-8

import pymysql
import traceback
from dddd.commen.sys_config import *
'''
cursor():   这个是光标，用来执行mysql语句的，用完后需要关闭
excute():   这个是执行语句，执行参数的mysql语句
fetchone(): 这个是查看执行语句后的一条数据
fetchall():  这个是查看所有数据
charset():  这个是编码方式，要和你数据库的编码方式一致，要不会连接失败
'''
class DBUtils():
    def _get_connection(self):      # 私有方法
        conn = pymysql.connect(host=ip,user=username,password=password,db=dbname,port=port)    #数据库连接信息
        return conn   #返回

    def excute_sql(self,sql):     # 增删改执行sql
        is_success = True    # 默认成功，
        conn = self._get_connection()    # 连接数据库
        cur = conn.cursor()       # 获取一个操作数据库的句柄
        try:                 # 如果成功
            cur.execute(sql)    # 执行参数的mysql语句，保存到内存
            conn.commit()      # 提交，增加数据，所以需要提交事务，这就需要用到此方法来进行提交，在增加数据后，如果不提交
        except Exception as e:    # 如果失败
            conn.rollback()     # 数据库回滚，撤销前面的数据库操作
            is_success = False     # 置为失败
        finally:
            self._close_connection(conn)    # 关闭数据库连接，释放连接资源
        return is_success

    def excute_query_sql(self,sql):    # 执行查询操作，并返回操作结果
        conn = self._get_connection()     # 连接数据库
        cur = conn.cursor()     # 获取一个操作数据库的句柄
        result = ""
        try:
            cur.execute(sql)    # 执行参数的mysql语句
            result = cur.fetchall()    # 返回所有查询结果
        except Exception:
            print(traceback.format_exc())    # 打印错误堆栈信息
        finally:
            self._close_connection(conn)    # 关闭数据库连接，释放连接资源
        print("result = ",result)
        return result

    def _close_connection(self,conn):
        conn.close()




