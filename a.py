import time
from datetime import date
from datetime import datetime, timedelta


def calcular_edad(fecha_nac):
	diferencia_fechas = datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.strptime(fecha_nac, '%Y-%m-%d') 
	diferencia_fechas_dias = diferencia_fechas.days
	edad_numerica = diferencia_fechas_dias / 365.2425
	edad = int(edad_numerica)
	return edad
	
	
	
fecha_nac = time.strftime("%Y-%m-%d")
print(calcular_edad(fecha_nac))






import time
from datetime import date
from datetime import datetime, timedelta


diferencia_fechas = datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.strptime('1997-02-21', '%Y-%m-%d') 
diferencia_fechas_dias = diferencia_fechas.days
edad_numerica = diferencia_fechas_dias / 365.2425
edad = int(edad_numerica)



