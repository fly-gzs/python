import gspread
from pprint import pprint

gc = gspread.service_account(filename='./google/projektsulipy-f9eed1f76c3d.json')

sheet1 = gc.open('diakok').worksheet('Munkalap1')


print(sheet1.acell('A2').value)
print(sheet1.cell(3, 2).value)

# Az API kérések száma korlátozott,
# ezért érdemes tömeges adatlekérését választani.
print(sheet1.get('A1:B4'))
print(sheet1.get_all_records())

sheet2 = gc.open('diakok').worksheet('Munkalap2')
print(sheet2.get_all_values)
print(sheet2.get_all_records())
sheet2.update_cell(1, 2, 'alma')

