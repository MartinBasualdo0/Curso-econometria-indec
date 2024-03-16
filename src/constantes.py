import numpy as np
columnas_relevantes_eph = [
 "ANO4",
 "TRIMESTRE",
 #Información sobre el/la encuestado/a
 "AGLOMERADO",
 "CH04",
 "CH06",
 "CH15",
 #Educación
 "CH09",
 "CH10",
 "CH11",
 "CH12",
 "CH13",
 "CH14", #Demasiados NaNs
 "NIVEL_ED",
 #Ocupación
 "INTENSI",
#  "ESTADO",
 "CAT_OCUP",
 "PP3E_TOT",
 "PP04A",
 "PP04D_COD",
#  "PP07A", #n_años último trabajo
 "P21"
]

anios_educacion_nivel_ed = {
    #Toma los "NIVEL_ED" y le asigna un valor
    1: (0+6)/2, #primario incompleto y educación especial
    2: 6, #primario completo
    3: (6+12)/2, #Secundario incompleto
    4: 12, #Secundario completo
    5: (12+17)/2, #Universitario incompleto
    6: 17, #Universitario completo
    7: 0, #Sin instrucción
}

anios_educacion_CH12 = {
    #Toma los "CH12" y le asigna un valor
    #El primero es el terminado, el segundo es la media (en caso de incompleto)
    #El tercero es el inicial (en caso de respuesta de CH14)
    #[Anios si termino, anios si no termino, anios si responde cual anio aprobo]
    #El round 0 es para evitar el decimal.
    1: [0, 0, np.nan],#Jardín/preescolar. NaN para que no sume CH14
    2: [6, 6/2, 0],#Primario
    3: [9, 9/2, 0],#EGB
    4: [12, round((6+12)/2,0), 6],#Secundario
    5: [12, round((6+12)/2,0), 6],#Polimodal
    6: [15, round((12+15)/2,0), 12],#Terciario
    7: [17, round((17+12)/2,0), 12],#Universitario
    8: [19, round((19+17)/2,0), 17],#Posgrado universitario
    9: [0,0, np.nan],#Educación especial (discapacitado)
}