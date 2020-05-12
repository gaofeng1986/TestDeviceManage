# coding= utf-8
from dddd.commen.DBUtil import DBUtils


def add_device(code,name):
    '''
    插入一条设备数据
    :param code: 设备编号
    :param name: 设备名称
    :return:
    '''
    # 根据传递的参数拼接sql,然后执行sql
    sql = "INSERT INTO `classify2`.`arrange_device` (`id`, `device_code`, `device_name`, `scenic_code`, `status`, `note`, `creator`, `create_time`, `modifier`, `modify_time`) VALUES (NULL, '{}', '{}', '10003', '1', NULL, 'liptest', NOW(), 'liptest', NOW());".format(code,name)
    db = DBUtils()
    db.excute_sql(sql)

def delete_device(code):
    sql = "DELETE FROM `classify2`.`arrange_device` WHERE device_code = '{}';".format(code)
    db = DBUtils()       # 实例化对象
    db.excute_sql(sql)    #
#
# def add_admin_to_device(device_code,admin_code):
#     pass
#
# def delete_admin_to_device(device_code,admin_code):
#     pass






