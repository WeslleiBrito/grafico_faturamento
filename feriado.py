import datetime as dt
from valores_padroes import data_inicial_padrao
from workadays import workdays


def feriados(country, state, data_inicial, data_final):
    dias = 0
    d = 0
    for date in workdays.get_holidays(country=country, state=state, years=range(data_inicial, data_final)):
        date = str(date)
        ano = int(date[0:4])
        mes = int(date[5:7])
        dia = int(date[8:])
        indice_semana = dt.date(year=ano, month=mes, day=dia).weekday()
        d += 1
        if -1 < indice_semana < 5:
            dias += 1

    return dias


if __name__ == '__main__':
    print(feriados(country='BR', state='BA', data_inicial=data_inicial_padrao().year,
                   data_final=dt.datetime.today().year + 1))
