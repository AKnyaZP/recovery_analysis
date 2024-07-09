from serializers import excel_serializer
from database import db_init, write, get_all


if __name__ == "__main__":
    db_init()  # Создаётся база данных, если её нет
    excel_data = excel_serializer("practise_data.xlsx")  # Читаю данные из таблицы
    write(excel_data)  # Записываю их в бд
    print(get_all())
