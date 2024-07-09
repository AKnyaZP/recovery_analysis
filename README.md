# recovery_analysis

# Backend

## Структура JSON
```json lines
[
    {
        "age": 4,
        "sex": "м",
        "before": {
            "lf_hf": 0.58,
            "vlf_percent": 29.1,
            "lf_percent": 25.9,
            "hf_percent": 45
        },
        "after": {
            "lf_hf": 0.74,
            "vlf_percent": 68,
            "lf_percent": 13.6,
            "hf_percent": 18.4
        }
    },
    ...
]
```

### database.py
```
db_init(filename)  # Функция для инициализации БД
    filename - Название файла с базой данных (по умолчанию "db.sqlite3")

write(json_data, filename)  # Функция для записи одной или нескольких 
                            # строк данных в БД
    json_data - Входные данные в формате JSON-строки
    filename - Название файла с базой данных (по умолчанию "db.sqlite3")

get_all(filename) -> JSON-строка  # Функция, которая возвращает все 
                                  # строки данных в БД в формате JSON-строки
    filename - Название файла с базой данных (по умолчанию "db.sqlite3")
```

### serializers.py
```
excel_serializer(filename)  # Функция для преобразования xlsx файла в JSON-строку
    filename - Название xlsx файла
```