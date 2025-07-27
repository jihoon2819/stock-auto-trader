import pandas as pd
## csv 파일 불러 오고 저장하기
data_csv=pd.read_csv('https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv')
print(data_csv)
data_csv.to_csv('data.csv')
## 엑셀파일 불러 오고 저장 하기
data_excel=pd.read_excel('https://github.com/hyunyulhenry/quant_py/raw/main/kospi.xlsx',sheet_name='kospi')
data_excel.to_excel('data.xlsx')