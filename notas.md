# Idea

La idea de la parte práctica es hacer ejercicios sencillos y rápidos, que minimice la frustración. Tiene que combinar el análisis descriptivo (gráficos) y cuantitativo (tests) para darle una perspectiva intuitiva al contenido teórico. Los datos parten de la encuesta permanente de hogares del tercer trimestre de 2023. 

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
12. CH14: ¿Cuál fue el último año que aprobó? **Se desechó por tener el 65% de no respuesta.**
13. NIVEL_ED: Nivel educativo
    **Ocupación**
14. INTENSI: intensidad de la ocupación.
15. CAT_OCUP: Categoría ocupacional
16. PP3E_TOT: Total de horas que trabajó en la semana en la ocupación principal
17. PP04A: ¿El negocio/empresa/institución/actividad en la que trabaja es... (se refiere al que trabaja más horas semanales) Estatal / privada
18. PP04D_COD: Código de ocupación (Ver Clasificador Nacional de Ocupaciones, CNO, versión 2001)
19. P21: Monto de ingreso de la ocupación principal.

### Columnas calculadas

1. Años de educación (elimina todo relacionado a lo de educación). Se tomó la siguiente relación para la columna "NIVEL_ED":

   1. Sin instrucción: 0.
   2. Primario incompleto: 3,5 años de educación.
   3. Primario completo: 7 años de educación.
   4. Secundario incompleto: 9,5 años de educación.
   5. Secundario completo: 12 años de educación.
   6. Universitario incompleto: 15 años de educación.
   7. Universitario completo: 18 años de educación.

   Idea a mejora: Si es incompleto y la columna CH14 es respuesta, se debería sumar al último nivel completo. El problema está en la alta tasa de no respueta (65%).
2. Salario horario. Resultado de `P21/P3E_TOT`.

### Tratamiento de outliers / filtros aplicados

#### Acción:

* La columna `P21 > 0`, el "-9" es para no respuesta. No nos interesan los que no tienen ingresos.
* `CAT_OCUP = 3` para filtrar por "Obrero o empleado".
* `PP3E_TOT > 0 y < 999`, hay gente que reporta ingresos pero no trabajó en la semana, y hay otros que directamente reporta una locura.

#### Omisión

* `INTENSI` no se filtra dado que reduce la muestra significativamente. El costo de eliminar quedarnos con los plenamente ocupados es mayor al beneficio de quitar los subocupados.
* `P21` presenta un valor atípico de 4,5 millones de pesos. No hay indicios por lo que ello esté mal.
* `Salario horario` presenta valores atípicos. El máximo es de 83 mil pesos argentinos por hora. No hay evidencia para demostrar que tenga que ser eliminado.
