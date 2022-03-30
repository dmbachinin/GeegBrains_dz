from requests import get, utils

def currency_rares(*currency_list):

    ''' Функция составляет словарь, содержащий валюты и выводит нужные значения '''

    res = get("http://www.cbr.ru/scripts/XML_daily.asp").text.split("</Valute>")
    res.pop()
    date_slice = res[0].find('Date="')+len('Date="')
    date = res[0][date_slice:date_slice+10] # получение даты ответа сервера
    res = res[1:]
    currency= {"date":date}
    for val in res: # получение информации по валютам
        cur_key = val[val.find("<CharCode>")+len("<CharCode>"):val.find("</CharCode>")]
        cur_val = val[val.find("<Value>")+len("<Value>"):val.find("</Value>")]
        cur_name = val[val.find("<Name>")+len("<Name>"):val.find("</Name>")]
        cur_nominal = val[val.find("<Nominal>") + len("<Nominal>"):val.find("</Nominal>")]
        currency[cur_key] = {"ru_name": cur_name, "value": cur_val,"nominal": cur_nominal}
    for key in currency_list:
        key = key.upper()
        if key in currency:
            print(f'{currency[key]["nominal"]} {currency[key]["ru_name"]} = {currency[key]["value"]} руб. ({currency["date"]})')
        else:
            print(f'Валюта "{key}" не найдена')
if __name__ == "__main__":
    currency_rares("CZK","CHF","ZAR")