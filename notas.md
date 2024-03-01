# Idea

La idea de la parte práctica es hacer ejercicios sencillos y rápidos, que minimice la frustración. Tiene que combinar el análisis descriptivo (gráficos) y cuantitativo (tests) para darle una perspectiva intuitiva al contenido teórico.

# Fuente

* [Encuesta Permanente de Hogares](https://www.indec.gob.ar/indec/web/Institucional-Indec-BasesDeDatos). Tercer trimestre 2023 (último publicado al día de la fecha).
* [Descripciones columnas EPH](https://www.indec.gob.ar/ftp/cuadros/menusuperior/eahu/EPH_tot_urbano_estructura_bases_2023.pdf).

# Base a trabajar

Descargo la base de datos en formato `.txt` en la carpeta "datos-eph", luego descomprimo los archivos. Me quedo exclusivamente con el archivo `usu_indivdual_....txt` para poder hacer el análisis de brecha salarial al nivel que corresponde (no nos interesan los hogares).

## Columnas relevantes

1. ANO4: Año de relevamiento (YYYY)
2. TRIMESTRE: trimestre
   **Información sobre el/la encuestado/a**
3. AGLOMERADO: grandes aglomerados urbanos.
4. CH04: Sexo.
5. CH06: edad.
6. CH15: ¿Dónde nació? (para ver si es inmigrante)
   **Educación**
7. CH09: ¿Sabe leer y escribir?
8. CH10: ¿Asiste o asistió a algún establecimiento educativo? (colegio, escuela,
   universidad)
9. CH11: Ese establecimiento educativo es público / privado?
10. CH12: nivel más alto que cursó
11. CH13: ¿Finalizó ese nivel?
12. CH14: ¿Cuál fue el último año que aprobó?
13. NIVEL_ED: Nivel educativo
    **Ocupación**
14. INTENSI: intensidad de la ocupación.
15. CAT_OCUP: Categoría ocupacional
16. PP3E_TOT: Total de horas que trabajó en la semana en la ocupación principal
17. PP04A: ¿El negocio/empresa/institución/actividad en la que trabaja es... (se refiere al que trabaja más horas semanales) Estatal / privada
18. PP04D_COD: Código de ocupación (Ver Clasificador Nacional de Ocupaciones, CNO, versión 2001)
19. P21: Monto de ingreso de la ocupación principal.

### Columnas calculadas

1. Años de educación (elimina todo relacionado a lo de educación)
2. Salario horario.

### Tratamiento de outliers / filtros aplicados

* `INTENSI = 2` para filtrar por "ocupados plenos". NO LO SACO POR AHORA PORQUE REDUCE LA MUESTRA.
* La columna `P21 > 0`, el "-9" es para no respuesta. No nos interesan los que no tienen ingresos.
* `CAT_OCUP = 3` para filtrar por "Obrero o empleado".
* `PP3E_TOT > 0 y < 999`, hay gente que reporta ingresos pero no trabajó en la semana, y hay otros que directamente reporta una locura.
