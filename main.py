import datetime as dt



class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class Calculator:
    def __init__(self, limit):
        self.records = []
        self.limit = limit
        self.today = dt.date.today()
        self.week = self.today - dt.timedelta(7)


    def add_record(self, record):
        self.records.append(record)
        print(record)

    def get_today_stats(self):
        today_stats = sum(record.amount for record in self.records
                          if record.date == self.today)
        return today_stats

    def get_week_stats(self):
        week_stats = sum(record.amount for record in self.records
                         if self.week <= record.date <= self.today)
        return week_stats


    def get_today_limit(self):
        today_limit = self.limit - self.get_today_stats()
        return today_limit


class CalloryCalc(Calculator):
    def get_remain_callories(self):
        callory_ballance = self.get_today_limit
        if callory_ballance > 0:
            msg= f'Жри, но осталось {callory_ballance}ккал'
        else:
            msg = 'Не жри'

        return msg



class CashCalc(Calculator):
    USD_RATE = 0.55
    EUR_RATE = 0.75
    RUB_RATE = 1

    def get_today_cash_limit(self, currency='rub'):
        currencies = {
            'usd': ("USD", CashCalc.USD_RATE),
            'eur': ("EUR", CashCalc.EUR_RATE),
            'rub': ("RUB", CashCalc.RUB_RATE)
        }
        cash_remain = self.get_today_limit()
        if cash_remain == 0:
            return "Пора печатать новые"
        if currency not in currencies:
            return f'{currency} еще не поддерживается'
        cur,rate = currencies[currency]
        cash_remain = round(cash_remain / rate, 2)
        if cash_remain > 0:
            msg = f'Осталось {cash_remain}{cur}'
        else:
            cash_remain = abs(cash_remain)
            msg = f'Денег нет. Долг - {cash_remain}{cur}'
        return  msg


