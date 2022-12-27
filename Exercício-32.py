from datetime import datetime
data = input('Digite a data no formato dd-mm-aaaa: ')



formDate = datetime.strptime(data, "%d-%m-%Y")
dateForm = formDate.strftime("%d-%m-%Y")



print(f'A data informada é valida {dateForm}.')
