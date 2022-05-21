import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import psycopg2
from app.settings import DATABASES
from datetime import datetime
from pycbrf.toolbox import ExchangeRates
import os


def import_google_sheet():

    # Файл, полученный в Google Developer Console
    CREDENTIALS_FILE = os.path.abspath("creds.json")
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1A8OF5IHgQWSC6dnZLm8WObFCUCW8-_2SJbdcTn2SpPw'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    # Чтение google таблицы
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A2:E100',
        majorDimension='ROWS'
    ).execute()

    # Подкоючение к БД
    con = psycopg2.connect(
        database=DATABASES['default']['NAME'],
        user=DATABASES['default']['USER'],
        password=DATABASES['default']['PASSWORD'],
        host=DATABASES['default']['HOST'],
        port=DATABASES['default']['PORT']
    )

    # Удаление всех данных из БД
    cur = con.cursor()
    cur.execute(
        "DELETE FROM sheet_sheet WHERE number IS NOT NULL;"
    )

    # Курс доллара на текущий день
    rates = ExchangeRates(datetime.now().date())

    # Переносим данные из google sheet в БД через цикл
    for i in values['values']:
        # Записываем только существующие значения
        if i:
            number = i[0]
            order_number = i[1]
            price_usd = i[2]
            delivery_time = i[3]
            price_rur = str(int(i[2]) * round(rates['USD'][4], 2))
            cur.execute(
                "INSERT INTO sheet_sheet(number,order_number,price_usd,delivery_time,price_rur) VALUES (%s, %s, %s, %s, %s)",
                [number, order_number, price_usd, delivery_time, price_rur]
            )

    # Записываем транзакцию
    con.commit()

    # Закрываем соединение с БД
    con.close()

