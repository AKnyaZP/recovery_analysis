import pandas as pd
import numpy as np

def generate_data(n):
    '''
    Функция для генерации данных
    @param: n - количество семплов данных, которое нужно сгенерировать 
    '''
    data = []
    for _ in range(n):
        V = np.random.randint(low=3, high=11)  # В
        P = np.random.choice(['м', 'ж']) # П
        LF_HF = np.random.uniform(0, 2)  # LF/HF
        VLF = np.random.uniform(0, 100)  # %VLF
        LF = np.random.uniform(0, 100)  # %LF
        HF = np.random.uniform(0, 100)  # %HF
        LF_HF_2 = np.random.uniform(0, 2)  # LF/HF
        VLF_2 = np.random.uniform(0, 100)  # %VLF
        LF_2 = np.random.uniform(0, 100)  # %LF
        HF_2 = np.random.uniform(0, 100)  # %HF

        row = {
            'В': V,
            'П': P,
            'LF/HF': LF_HF,
            '%VLF': VLF,
            '%LF': LF,
            '%HF': HF,
            'LF/HF 2': LF_HF_2,
            '%VLF 2': VLF_2,
            '%LF 2': LF_2,
            '%HF 2': HF_2
        }

        data.append(row)

    df = pd.DataFrame(data)
    
    return df


def main():
    n = int(input('введите количество семплов датасета: '))
    path = 'C:/recovery_analysis/data/generated_data.xlsx' # путь, куда надо сохранить файл с нагенерированными данными

    df_generated = generate_data(n)
    df_generated = df_generated.round(2)
    
    df_generated.to_excel(path, index=False)

    print(df_generated.head(3))


if __name__ == '__main__':
    main()
