import json

import pandas as pd


def excel_serializer(filename: str) -> str:
    dataframe = pd.read_excel(filename, skiprows=1)

    data = []
    for index, row in dataframe.iterrows():
        data.append({
            "age": row["В"],
            "sex": row["П"],
            "before": {
                "lf_hf": row["LF/HF"],
                "vlf_percent": row["%VLF"],
                "lf_percent": row["%LF"],
                "hf_percent": row["%HF"]
            },
            "after": {
                "lf_hf": row["LF/HF.1"],
                "vlf_percent": row["%VLF.1"],
                "lf_percent": row["%LF.1"],
                "hf_percent": row["%HF.1"]
            }
        })
    json_data = json.dumps(data, ensure_ascii=False)

    return json_data
