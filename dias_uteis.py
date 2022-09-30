from datetime import timedelta
from valores_padroes import data_inicial_padrao

# started from the code of Casey Webster at
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/ddd39a02644540b7

# Define the weekday mnemonics to match the date.weekday function
(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)
# Define default weekends, but allow this to be overridden at the function level
# in case someone only, for example, only has a 4-day workweek.
default_weekends = (SAT, SUN)


def networkdays(start_date, end_date, holidays=[], weekends=default_weekends):
    delta_days = (end_date - start_date).days + 1
    full_weeks, extra_days = divmod(delta_days, 7)
    # num_workdays = how many days/week you work * total # of weeks
    num_workdays = (full_weeks + 1) * (7 - len(weekends))
    # subtract out any working days that fall in the 'shortened week'
    for d in range(1, 8 - extra_days):
        if (end_date + timedelta(d)).weekday() not in weekends:
            num_workdays -= 1
    # skip holidays that fall on weekends
    holidays = [x for x in holidays if x.weekday() not in weekends]
    # subtract out any holidays
    for d in holidays:
        if start_date <= d <= end_date:
            num_workdays -= 1
    return num_workdays


if __name__ == '__main__':
    from datetime import date

    print(networkdays(start_date=data_inicial_padrao(), end_date=date.today()))
