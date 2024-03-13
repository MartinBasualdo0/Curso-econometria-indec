# Idea

La idea de la parte práctica es hacer ejercicios sencillos y rápidos, que minimice la frustración. Tiene que combinar el análisis descriptivo (gráficos) y cuantitativo (tests) para darle una perspectiva intuitiva al contenido teórico. Los datos parten de la ncuesta permanente de hogares del tercer trimestre de 2023.

El dataset final será subido a [Kaggle](https://www.kaggle.com/datasets/martinbasualdo/encuesta-permanente-de-hogares-procesada/settings).

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
12. CH14: ¿Cuál fue el último año que aprobó? **Tiene 65% de no respuesta.**
13. NIVEL_ED: Nivel educativo

**Ocupación**

1. INTENSI: intensidad de la ocupación.
11. CAT_OCUP: Categoría ocupacional
12. PP3E_TOT: Total de horas que trabajó en la semana en la ocupación principal
13. PP04A: ¿El negocio/empresa/institución/actividad en la que trabaja es... (se refiere al que trabaja más horas semanales) Estatal / privada
14. PP04D_COD: Código de ocupación (Ver Clasificador Nacional de Ocupaciones, CNO, versión 2001)
15. P21: Monto de ingreso de la ocupación principal.

### Columnas calculadas

1. Años de educación. Dos alternativas (actualmente se optó por la segunda).

   A. Se tomó la siguiente relación para la columna "NIVEL_ED":

   1. Sin instrucción: 0 años de educación.
   2. Primario incompleto: 3,5 años de educación.
   3. Primario completo: 7 años de educación.
   4. Secundario incompleto: 9,5 años de educación.
   5. Secundario completo: 12 años de educación.
   6. Universitario incompleto: 15 años de educación.
   7. Universitario completo: 18 años de educación.

   B. A partir de las columnas CH12 (último nivel de educación cursado), CH13 (si terminó o no) y CH14 (años avanzados):

   1. Si CH12 es Jardín o educación especial: 0 años de eduación. No importa si completó o no (CH13)
   2. Si CH12 es primario y terminado: 6 años de educación. Si no es terminado, pero contamos información de años avanzados (CH14 distinto a 98, 99 y NaN), se suma 0 + CH14. Si no es terminado y no contamos con información de años avanzados, se toma la media (3).
   3. Si CH12 es EGB: 6 años de educación. Si no es terminado, pero contamos información de años avanzados (CH14 distinto a 98, 99 y NaN), se suma 0 + CH14. Si no es terminado y no contamos con información de años avanzados, se toma la media (4,5).
   4. Si CH12 es secundario: 12 años de educación. Si no es terminado, pero contamos información de años avanzados (CH14 distinto a 98, 99 y NaN), se suma 6 + CH14. Si no es terminado y no contamos con información de años avanzados, se toma la media de los años adicionados (9).
   5. Si CH12 es polimodal: 12 años de educación. Si no es terminado, pero contamos información de años avanzados (CH14 distinto a 98, 99 y NaN), se suma 6 + CH14. Si no es terminado y no contamos con información de años avanzados, se toma la media de los años adicionados (9).
   6. Si CH12 es terciario: 15 años de educación. Si no es terminado, pero contamos información de años avanzados (CH14 distinto a 98, 99 y NaN), se suma 12 + CH14. Si no es terminado y no contamos con información de años avanzados, se toma la media de los años adicionados y se lo redondea a un dígito para evitar el decimal (14).
   7. Si CH12 es universitario: 17 años de educación. Si no es terminado, pero contamos información de años avanzados (CH14 distinto a 98, 99 y NaN), se suma 12 + CH14. Si no es terminado y no contamos con información de años avanzados, se toma la media de los años adicionados y se lo redondea a un dígito para evitar el decimal (15).
   8. Si CH12 es posgrado universitario: 19 años de educación. Si no es terminado, pero contamos información de años avanzados (CH14 distinto a 98, 99 y NaN), se suma 17+ CH14. Si no es terminado y no contamos con información de años avanzados, se toma la media de los años adicionados (18).
2. Salario horario. Resultado de `P21/P3E_TOT`.
3. Años de experiencia: Resultado de `Edad (CH06) - años de educación - 6`. Suponemos que la persona se empieza a educar a los seis años, y una vez que deja de estudiar se pone a trabajar y no para nunca; también se hace el supuesto que mientras estudia no trabaja.

### Tratamiento de outliers / filtros aplicados

#### Acción:

* La columna `P21 > 0`, el "-9" es para no respuesta. No nos interesan los que no tienen ingresos.
* `CAT_OCUP = 3` para filtrar por "Obrero o empleado".
* `PP3E_TOT > 0 y < 999`, hay gente que reporta ingresos pero no trabajó en la semana, y hay otros que directamente reporta una locura.

#### Omisión

* `INTENSI` no se filtra dado que reduce la muestra significativamente. El costo de eliminar quedarnos con los plenamente ocupados es mayor al beneficio de quitar los subocupados.
* `P21` presenta un valor atípico de 4,5 millones de pesos. No hay indicios por lo que ello esté mal.
* `Salario horario` presenta valores atípicos. El máximo es de 83 mil pesos argentinos por hora. No hay evidencia para demostrar que tenga que ser eliminado.
