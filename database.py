import json
import sqlite3


def db_init(filename: str = "db.sqlite3") -> None:
    db = None
    try:
        with sqlite3.connect(filename) as db:
            cursor = db.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS analysis(
                              id INTEGER PRIMARY KEY,
                              age INTEGER,
                              sex CHAR(1),
                              lf_hf_before REAL,
                              vlf_percent_before REAL,
                              lf_percent_before REAL,
                              hf_percent_before REAL,
                              lf_hf_after REAL,
                              vlf_percent_after REAL,
                              lf_percent_after REAL,
                              hf_percent_after REAL
            );''')
            db.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if db:
            db.close()


def write(json_data: str, filename: str = "db.sqlite3") -> None:
    db = None
    try:
        with sqlite3.connect(filename) as db:
            cursor = db.cursor()
            data = json.loads(json_data)
            for row in data:
                cursor.execute(f'''INSERT INTO analysis (age, sex, lf_hf_before, vlf_percent_before, lf_percent_before, hf_percent_before, lf_hf_after, vlf_percent_after, lf_percent_after, hf_percent_after)
                VALUES ({row["age"]}, '{row["sex"]}', {row["before"]["lf_hf"]}, {row["before"]["vlf_percent"]}, {row["before"]["lf_percent"]}, {row["before"]["hf_percent"]}, {row["after"]["lf_hf"]}, {row["after"]["vlf_percent"]}, {row["after"]["lf_percent"]}, {row["after"]["hf_percent"]});''')
            db.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if db:
            db.close()


def get_all(filename: str = "db.sqlite3") -> str:
    db = None
    json_data = ""
    try:
        with sqlite3.connect(filename) as db:
            cursor = db.cursor()
            cursor.execute('''SELECT * FROM analysis''')
            result = cursor.fetchall()
            data = []
            for row in result:
                data.append({
                    "age": row[1],
                    "sex": row[2],
                    "before": {
                        "lf_hf": row[3],
                        "vlf_percent": row[4],
                        "lf_percent": row[5],
                        "hf_percent": row[6]
                    },
                    "after": {
                        "lf_hf": row[7],
                        "vlf_percent": row[8],
                        "lf_percent": row[9],
                        "hf_percent": row[10]
                    }
                })
            json_data = json.dumps(data, ensure_ascii=False)
    except sqlite3.Error as e:
        print(e)
    finally:
        if db:
            db.close()
    return json_data
