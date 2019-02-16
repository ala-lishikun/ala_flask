from flask import Flask,render_template,request,session,redirect,url_for
from datetime import datetime
import config,math
app = Flask(__name__)
app.config.from_object(config)

@app.route('/',methods=['GET','POST'])
def days():
    if request.method == 'POST':
        input_date = request.form.get('date')
        input_date_year = datetime.strptime(input_date, "%Y-%m-%d")
        year = input_date_year.year
        month = input_date_year.month
        day = input_date_year.day
        # #元组
        # month_days = (31,28,31,30,31,30,31,31,30,31,30,31)
        # days = sum(month_days[:month-1]) + day
        # #判断是否为闰年
        # if month > 2 and is_leap_year(year):
        #         days += 1
        # 列表
        # month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # if is_leap_year(year):
        #     month_days[1]=29
        # days = sum(month_days[:month-1]) + day
        # 集合
        # days = 0
        # _30_days = {4,6,9,11}
        # _31_days = {1,3,5,7,8,10,12}
        # for i in range(month):
        #     if i in _30_days:
        #         days += 30
        #     elif i in _31_days:
        #         days += 31
        #     else:
        #         days += 28
        # if month > 2 and is_leap_year(year):
        #     days += 1
        # 字典
        dict_days = {1: 31,
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
        days += day
        for i in range(1, month):
            days += dict_days[i]
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if month > 2 :
                days += 1
        return render_template('date.html',date=input_date,year=year,message=days)
    else:
        return render_template('date.html')


@app.route('/survive',methods=['GET','POST'])
def life():
    if request.method == 'POST':
        input_birthday = request.form.get('date')
        birthday = datetime.strptime(input_birthday, '%Y-%m-%d')
        birthday_year = birthday.year
        birthday_month = birthday.month
        birthday_day = birthday.day

        today = datetime.strptime(str(datetime.today().date()), '%Y-%m-%d')
        today_year = today.year
        today_month = today.month
        today_day = today.day

        year_dict_days = {1: 366,
                          2: 365}

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
        if today_year - birthday_year >= 2:
            for i in range(1, today_year - birthday_year):
                year = birthday_year + i
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    days += year_dict_days[1]
                else:
                    days += year_dict_days[2]
            for k in range(1, today_month):
                days += month_dict_days[k]
            days = days + today_day
            for j in range(birthday_month + 1, 13):
                days += month_dict_days[j]
            days = days + month_dict_days[birthday_month] - birthday_day + 1

        elif today_year == birthday_year:
            if birthday_month == today_month:
                days = month_dict_days[birthday_month] - birthday_day
            elif today_month - birthday_month >= 2:
                for k in range(birthday_month + 1, today_month):
                    days += month_dict_days[k]
                days = days + today_day + month_dict_days[birthday_month] - birthday_day + 1
            elif 1 <= today_month - birthday_month < 2:
                days = days + today_day + month_dict_days[birthday_month] - birthday_day + 1
        elif 1 <= today_year - birthday_year < 2:
            for k in range(1, today_month):
                days += month_dict_days[k]
            days = days + today_day
            print(days)
            for j in range(birthday_month + 1, 13):
                days += month_dict_days[j]
            days = days + month_dict_days[birthday_month] - birthday_day + 1
            print(days)
        else:
            print('出生日期有误')
        return render_template('life.html',days=days,birthday=input_birthday)
    else:
        return render_template('life.html')

@app.route('/money',methods=['GET','POST'])
def save_money():
    if request.method == 'POST':
        input_weeks = int(request.form.get('weeks')) #一共多少周
        basic_money = int(request.form.get('money_per_week')) #每周的存款数
        money_increase = request.form.get('increase_money')#每周递增的钱数
        money_list_sum = [] # 每周存款数的总数
        money_list=[]
        for i in range(input_weeks):
            money_list.append(basic_money)
            saving = math.fsum(money_list)
            money_list_sum.append(saving)
            basic_money += int(money_increase)
        money_list_sum.append(saving)
        return render_template('money.html', basic_money=money_list[0], increase_money=money_increase,money=money_list_sum[-1],week=input_weeks)
    else:
        return render_template('money.html')





if __name__ == '__main__':
    app.run()
