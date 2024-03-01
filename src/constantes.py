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
 "P21"
]

anios_educacion_nivel_ed = {
    #Toma los "NIVEL_ED" y le asigna un valor
    1: (0+7)/2, #primario incompleto y educación especial
    2: 7, #primario completo
    3: (7+12)/2, #Secundario incompleto
    4: 12, #Secundario completo
    5: (12+18)/2, #Universitario incompleto
    6: 18, #Universitario completo
    7: 0, #Sin instrucción
}