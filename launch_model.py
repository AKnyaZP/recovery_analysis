from joblib import load
import torch
import openpyxl
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np
import torch.nn as nn
from architecture_of_model.arch_model_2 import SimpleNet

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")




class LaunchModel:
    def __init__(self):
        pass
        
    def launch_model_1(self, X):
        model_path = 'models/simple_net_model_full.pth'
        try:
            model = torch.load(model_path, map_location=device)
        except Exception as e:
            print(f"Ошибка при загрузке модели: {e}")
            raise
        model.eval()  # Set model to evaluation mode if it's a PyTorch model
        with torch.no_grad():  # Disable gradient calculation
            predictions = model(X.to(device))
        predictions = (predictions> 0.5).float()
        return predictions.cpu().numpy()

    def launch_model_2(self, X):
        model_path = 'models/rhinosurgical_model.pth'
        try:
            model = torch.load(model_path, map_location=device)
        except Exception as e:
            print(f"Ошибка при загрузке модели: {e}")
            raise
        predictions = model.predict(X.to(device))
        return predictions.cpu().numpy()

    def processing_data_file(self, file: str):
        '''
        :param file: путь до файла 
        Данные, которые ожидаются: age  gender  LF/HF   %VLF   %LF   %HF   LF/HF.1  %VLF.1  %LF.1  %HF.1
        '''
        try: 
            data = pd.read_excel(file)
        except FileNotFoundError:
            print('файл не найден')
            raise FileNotFoundError("Файл не найден")
        except Exception as e:
            print(f'Произошла ошибка при чтении файла: {e}')
            raise

        scaler = StandardScaler()
        label_encoder = LabelEncoder()

        data = data.fillna("-1")
        data['П'] = label_encoder.fit_transform(data['П'].values)

        X = scaler.fit_transform(data)
        X_tensor = torch.tensor(X, dtype=torch.float32)

        return X_tensor

    def processing_data_manually(self, age: int, gender: str, LFHF: float, VLF: float, LF: float, HF: float, LFHF_1: float, VLF_1: float, LF_1: float, HF_1: float):
        pass

#пример того, как надо запускать модель на предсказания
def main():
    path_to_data = 'data/generated_data.xlsx' # Путь до файла передаётся пользователем
    lm = LaunchModel() # определяем экземпляр класса
    data = lm.processing_data_file(path_to_data) # обработка данных и получения тензора 
    predictions = lm.launch_model_1(X=data) # предсказания ввиде массива numpy
    print(predictions)

if __name__ == '__main__':
    main()