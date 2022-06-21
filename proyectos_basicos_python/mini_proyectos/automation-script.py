import calendar
from pathlib import Path


mese_anio =list(calendar.month_name[1:])
dia_semana = ['Dia 1', 'Dia 10', 'Dia 20', 'Dia 30']

for i, mes in enumerate(mese_anio):
    for dia in dia_semana:
        Path(f'2022/{i+1}.{mes}/{dia}').mkdir(parents=True, exist_ok=True)
