# -*- coding: utf-8 -*-
# @Time    : 2018/12/28 19:59
# @Author  : ala
from datetime import datetime
import time,calendar
# def is_leap_year(year):
#     '''
#     :param year:判断是否为闰年
#     :return: 是返回 True  不是返回False
#     '''
#     is_leap = False
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         is_leap =True
#     return is_leap
# def get_day():
#     input_date = input("请输入日期:（2015/05/05）:")
#     input_date_year = datetime.strptime(input_date,"%Y/%m/%d")
#     year = input_date_year.year
#     month = input_date_year.month
#     day = input_date_year.day
#     # #元组
#     # month_days = (31,28,31,30,31,30,31,31,30,31,30,31)
#     # days = sum(month_days[:month-1]) + day
#     # #判断是否为闰年
#     # if month > 2 and is_leap_year(year):
#     #         days += 1
#     #列表
#     # month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     # if is_leap_year(year):
#     #     month_days[1]=29
#     # days = sum(month_days[:month-1]) + day
#     #集合
#     # days = 0
#     # _30_days = {4,6,9,11}
#     # _31_days = {1,3,5,7,8,10,12}
#     # for i in range(month):
#     #     if i in _30_days:
#     #         days += 30
#     #     elif i in _31_days:
#     #         days += 31
#     #     else:
#     #         days += 28
#     # if month > 2 and is_leap_year(year):
#     #     days += 1
#     #字典
#     dict_days = {1:31,
#                  2:28,
#                  3:31,
#                  4:30,
#                  5:31,
#                  6:30,
#                  7:31,
#                  8:31,
#                  9:30,
#                  10:31,
#                  11:30,
#                  12:31}
#     days = 0
#     days += day
#     for i in range(1,month):
#         days += dict_days[i]
#     if month > 2 and is_leap_year(year):
#         days += 1
#     print("您输入的日期是{}年的第{}天".format(year,days))



'''
today = datetime.strptime(str(datetime.today().date()),'%Y-%m-%d')
today_year = today.year
today_month = today.month
today_day = today.day

birthday = datetime.strptime('2018-12-29','%Y-%m-%d')
birthday_year = birthday.year
birthday_month = birthday.month
birthday_day = birthday.day

year_dict_days = {1:366,
                  2:365}

month_dict_days = {1: 31,
                     2: 28,
                     3: 31,
                     4: 30,
                     5: 31,
                     6: 30,
                     7: 31,
                     8: 31,
                     9: 30,
                     10: 31,
                     11: 30,
                     12: 31}
days = 0
if today_year - birthday_year >=2 :
    for i in range(1,today_year-birthday_year):
        year = birthday_year+i
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            days += year_dict_days[1]
        else:
            days += year_dict_days[2]
    for k in range(1,today_month):
        days += month_dict_days[k]
    days = days + today_day
    for j in range(birthday_month+1, 13):
        days += month_dict_days[j]
    days = days + month_dict_days[birthday_month] - birthday_day +1

elif today_year == birthday_year:
    if birthday_month == today_month:
        days = month_dict_days[birthday_month] - birthday_day + 1
    elif today_month - birthday_month>=2:
        for k in range(birthday_month+1,today_month):
            days += month_dict_days[k]
        days = days +  today_day + month_dict_days[birthday_month] - birthday_day + 1
    elif 1 <= today_month - birthday_month < 2:
        days = days + today_day + month_dict_days[birthday_month] - birthday_day + 1
elif 1 <= today_year - birthday_year < 2:
    for k in range(1,today_month):
        days += month_dict_days[k]
    days = days + today_day
    print(days)
    for j in range(birthday_month+1, 13):
        days += month_dict_days[j]
    days = days + month_dict_days[birthday_month] - birthday_day +1
    print(days)
else:
    print('出生日期有误')



'''

money_per_week = 10     # 每周的存入的金额
i = 1                   # 记录周数
increase_money = 10     # 递增的金额
total_week = 52         # 总共的周数
saving = 0              # 账户累计

while i <= total_week:
    # 存钱操作
    # saving = saving + money_per_week
    saving += money_per_week

    # 输出信息
    print('第{}周，存入{}元，账户累计{}元'.format(i, money_per_week, saving))

    # 更新下一周的存钱金额
    money_per_week += increase_money
    i += 1
print(saving)