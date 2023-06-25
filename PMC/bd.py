import mysql.connector
from config import read_config

# Подключение к БД
db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Pa$$w0rd",
  database="BNR"
)

# Функция для просмотра данных с фильтрацией
def view_logs(filter_ip=None, filter_start_date=None, filter_end_date=None):
    cursor = db.cursor()
    sql = "SELECT * FROM access_logs"
    conditions = []

    if filter_ip:
        conditions.append("ip = %s")
    if filter_start_date:
        conditions.append("date >= %s")
    if filter_end_date:
        conditions.append("date <= %s")

    if conditions:
        sql += " WHERE " + " AND ".join(conditions)

    values = []
    if filter_ip:
        values.append(filter_ip)
    if filter_start_date:
        values.append(filter_start_date)
    if filter_end_date:
        values.append(filter_end_date)

    cursor.execute(sql, tuple(values))
    result = cursor.fetchall()

    for row in result:
        print(row)

# Примеры вызова функции для просмотра данных с различными фильтрами
# Фильтрация по IP адресу
view_logs(filter_ip='127.0.0.1')

# Фильтрация по промежутку дат
view_logs(filter_start_date='2023-01-01', filter_end_date='2023-12-31')

# Фильтрация по IP адресу и промежутку дат
view_logs(filter_ip='127.0.0.1', filter_start_date='2023-01-01', filter_end_date='2023-12-31')

# Чтение настроек из файла
log_path, log_file_mask = read_config('config.ini')

db.close()