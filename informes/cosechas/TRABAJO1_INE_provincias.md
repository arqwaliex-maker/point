# TRABAJO 1 · INE — mapa provincial de 52 apellidos (primer apellido)

## 0. Fuente, método y control

| Campo | Valor |
|---|---|
| Fuente | INE, «Frecuencias de apellidos», consulta «Apellidos por provincia de residencia» (`www.ine.es/apellidos/formGeneralresult.do?vista=1`). Censo anual de población a 01/01/2025 |
| Cita | «Elaboración propia con datos extraídos del sitio web del INE: www.ine.es». Licencia CC BY 4.0 |
| robots.txt | www.ine.es prohíbe /cgi-bin/, /buscar/, /Test/, /Admin/, /testin/. `/apellidos/` está permitido |
| Automatización | Un formulario HTML (POST) con el apellido y las 53 opciones de provincia (Total y 52 provincias). No exige JavaScript, sesión ni captcha. Una consulta por apellido, con 5 s de pausa |
| Grafía | Sin tildes ni diéresis y con Ñ (ACUÑA, AGUERO, CACERES…) |
| Secreto estadístico | En esta consulta el INE marca con «.» (un punto) las celdas ocultas. Se copian tal cual y nunca se convierten en cero. Nota del INE: «Por secreto estadístico sólo se muestran los apellidos cuya frecuencia es mayor que 5 en alguno de los dos apellidos para el total nacional. Para las provincias seleccionadas se exige además una frecuencia de al menos 5 en alguno de los dos apellidos.» |
| Puesto | **La consulta no da el puesto.** Sale del archivo `apellidos_frecuencia.xls` (columna «Orden») bajado en la cosecha anterior |
| **Control MOLINA** | Consulta: total 125.316; top 3 Granada 9,202 ‰, Jaén 8,527 ‰, Córdoba 6,336 ‰. Archivo: puesto 30. Esperado: puesto 30, 125.316, Granada 9,20 · Jaén 8,53 · Córdoba 6,34 → **PASÓ** |

## 1. Resumen: total, puesto y top 3 por mil

| # | Apellido | Clave | Total 1.er ap. (consulta) | Total (archivo) | ¿Coincide? | Puesto (archivo) | Prov. con dato | Prov. con «.» | TOP 1 | TOP 2 | TOP 3 | Antes (cosecha 1) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Quiroga | QUIROGA | 7.272 | 7.272 | sí | 755 | 50 | 0 | Lugo · 622 · 1,908 ‰ | Ourense · 249 · 0,816 ‰ | León · 259 · 0,578 ‰ | — |
| 2 | Carrizo | CARRIZO | 2.006 | 2.006 | sí | 2415 | 42 | 2 | León · 179 · 0,400 ‰ | Albacete · 58 · 0,148 ‰ | Cuenca · 20 · 0,100 ‰ | — |
| 3 | Coronel | CORONEL | 5.190 | 5.190 | sí | 1025 | 48 | 0 | Huelva · 800 · 1,485 ‰ | Ciudad Real · 112 · 0,226 ‰ | Madrid · 1.233 · 0,173 ‰ | — |
| 4 | Cáceres | CACERES | 21.211 | 21.211 | sí | 253 | 52 | 0 | Badajoz · 990 · 1,488 ‰ | Huelva · 770 · 1,429 ‰ | Cáceres · 485 · 1,249 ‰ | — |
| 5 | Córdoba | CORDOBA | 19.176 | 19.176 | sí | 283 | 52 | 0 | Córdoba · 1.970 · 2,548 ‰ | Ciudad Real · 733 · 1,481 ‰ | Cuenca · 240 · 1,201 ‰ | — |
| 6 | Godoy | GODOY | 14.634 | 14.634 | sí | 367 | 50 | 2 | Palmas, Las · 1.868 · 1,594 ‰ | Badajoz · 520 · 0,782 ‰ | Málaga · 1.258 · 0,702 ‰ | — |
| 7 | Ledesma | LEDESMA | 9.685 | 9.685 | sí | 575 | 51 | 0 | Badajoz · 568 · 0,854 ‰ | Santa Cruz de Tenerife · 836 · 0,769 ‰ | Salamanca · 217 · 0,661 ‰ | — |
| 8 | Villalba | VILLALBA | 21.382 | 21.382 | sí | 249 | 52 | 0 | Teruel · 182 · 1,337 ‰ | Málaga · 2.120 · 1,184 ‰ | Cuenca · 228 · 1,141 ‰ | — |
| 9 | Correa | CORREA | 21.600 | 21.600 | sí | 246 | 52 | 0 | Santa Cruz de Tenerife · 2.304 · 2,119 ‰ | Huelva · 730 · 1,355 ‰ | Granada · 1.166 · 1,233 ‰ | — |
| 10 | Duarte | DUARTE | 16.303 | 16.303 | sí | 327 | 52 | 0 | Ceuta · 69 · 0,826 ‰ | Cádiz · 917 · 0,727 ‰ | Málaga · 1.278 · 0,713 ‰ | — |
| 11 | Escobar | ESCOBAR | 31.493 | 31.493 | sí | 158 | 52 | 0 | Badajoz · 883 · 1,328 ‰ | Almería · 998 · 1,295 ‰ | Huelva · 680 · 1,262 ‰ | — |
| 12 | Figueroa | FIGUEROA | 15.009 | 15.009 | sí | 355 | 52 | 0 | Pontevedra · 1.610 · 1,699 ‰ | Santa Cruz de Tenerife · 807 · 0,742 ‰ | Coruña, A · 777 · 0,684 ‰ | — |
| 13 | Guzmán | GUZMAN | 34.302 | 34.302 | sí | 141 | 52 | 0 | Málaga · 2.776 · 1,550 ‰ | Jaén · 876 · 1,417 ‰ | Toledo · 1.037 · 1,373 ‰ | — |
| 14 | Juárez | JUAREZ | 18.185 | 18.185 | sí | 296 | 51 | 1 | Zamora · 201 · 1,214 ‰ | Albacete · 430 · 1,100 ‰ | Toledo · 809 · 1,071 ‰ | — |
| 15 | Peralta | PERALTA | 15.652 | 15.652 | sí | 338 | 52 | 0 | Huesca · 271 · 1,178 ‰ | Teruel · 143 · 1,051 ‰ | Cádiz · 859 · 0,681 ‰ | — |
| 16 | Mansilla | MANSILLA | 6.134 | 6.134 | sí | 889 | 48 | 0 | Ciudad Real · 324 · 0,655 ‰ | Badajoz · 402 · 0,604 ‰ | Albacete · 160 · 0,409 ‰ | — |
| 17 | Ayala | AYALA | 19.260 | 19.260 | sí | 282 | 52 | 0 | Murcia · 2.158 · 1,360 ‰ | Burgos · 316 · 0,871 ‰ | Almería · 590 · 0,766 ‰ | — |
| 18 | Barrios | BARRIOS | 19.061 | 19.061 | sí | 284 | 52 | 0 | Zamora · 405 · 2,446 ‰ | Santa Cruz de Tenerife · 1.180 · 1,085 ‰ | Salamanca · 287 · 0,874 ‰ | — |
| 19 | Acuña | ACUÑA | 8.444 | 8.444 | sí | 657 | 49 | 1 | Pontevedra · 1.503 · 1,586 ‰ | Sevilla · 801 · 0,405 ‰ | Cádiz · 430 · 0,341 ‰ | — |
| 20 | Agüero | AGUERO | 4.358 | 4.358 | sí | 1210 | 45 | 3 | Cantabria · 401 · 0,676 ‰ | Toledo · 336 · 0,445 ‰ | Segovia · 39 · 0,246 ‰ | — |
| 21 | Chávez | CHAVEZ | 14.307 | 14.307 | sí | 380 | 50 | 0 | Santa Cruz de Tenerife · 1.375 · 1,265 ‰ | Badajoz · 545 · 0,819 ‰ | Madrid · 3.416 · 0,480 ‰ | — |
| 22 | Farías | FARIAS | 2.507 | 2.507 | sí | 2004 | 45 | 1 | Palmas, Las · 245 · 0,209 ‰ | Santa Cruz de Tenerife · 105 · 0,097 ‰ | Ourense · 27 · 0,088 ‰ | — |
| 23 | Cardozo | CARDOZO | 3.364 | 3.364 | sí | 1530 | 48 | 1 | Balears, Illes · 163 · 0,130 ‰ | Madrid · 810 · 0,114 ‰ | Málaga · 193 · 0,108 ‰ | — |
| 24 | Pereyra | PEREYRA | 2.206 | 2.206 | sí | 2225 | 36 | 2 | Balears, Illes · 183 · 0,146 ‰ | Santa Cruz de Tenerife · 127 · 0,117 ‰ | Girona · 63 · 0,076 ‰ | — |
| 25 | Romano | ROMANO | 4.368 | 4.368 | sí | 1207 | 48 | 2 | Segovia · 103 · 0,651 ‰ | Cantabria · 192 · 0,323 ‰ | Navarra · 204 · 0,298 ‰ | — |
| 26 | Lucatti | LUCATTI | NO SE PUDO LEER:  | | | | | | | | | |
| 27 | Bianchi | BIANCHI | 1.024 | 1.024 | sí | 4333 | 26 | 0 | Cádiz · 88 · 0,070 ‰ | Balears, Illes · 65 · 0,052 ‰ | Santa Cruz de Tenerife · 57 · 0,052 ‰ | — |
| 28 | Colombo | COLOMBO | 934 | 934 | sí | 4702 | 27 | 1 | Cáceres · 49 · 0,126 ‰ | Balears, Illes · 55 · 0,044 ‰ | Palmas, Las · 48 · 0,041 ‰ | — |
| 29 | Esposito | ESPOSITO | 890 | 890 | sí | 4907 | 19 | 1 | Santa Cruz de Tenerife · 106 · 0,097 ‰ | Balears, Illes · 86 · 0,069 ‰ | Málaga · 71 · 0,040 ‰ | — |
| 30 | Ferrari | FERRARI | 1.532 | 1.532 | sí | 3049 | 30 | 1 | Balears, Illes · 125 · 0,100 ‰ | Santa Cruz de Tenerife · 75 · 0,069 ‰ | Sevilla · 119 · 0,060 ‰ | — |
| 31 | Ferreyra | FERREYRA | 1.023 | 1.023 | sí | 4337 | 29 | 3 | Balears, Illes · 106 · 0,085 ‰ | Soria · 7 · 0,078 ‰ | Málaga · 88 · 0,049 ‰ | — |
| 32 | Rossi | ROSSI | 2.378 | 2.378 | sí | 2085 | 37 | 4 | Cádiz · 201 · 0,159 ‰ | Balears, Illes · 131 · 0,105 ‰ | Santa Cruz de Tenerife · 111 · 0,102 ‰ | — |
| 33 | Russo | RUSSO | 1.469 | 1.469 | sí | 3153 | 27 | 3 | Santa Cruz de Tenerife · 154 · 0,142 ‰ | Balears, Illes · 122 · 0,098 ‰ | Palmas, Las · 90 · 0,077 ‰ | — |
| 34 | Schmidt | SCHMIDT | 1.366 | 1.366 | sí | 3371 | 26 | 0 | Balears, Illes · 181 · 0,145 ‰ | Santa Cruz de Tenerife · 148 · 0,136 ‰ | Alicante/Alacant · 135 · 0,066 ‰ | — |
| 35 | Acosta | ACOSTA | 35.656 | 35.656 | sí | 136 | 52 | 0 | Santa Cruz de Tenerife · 6.325 · 5,817 ‰ | Palmas, Las · 3.414 · 2,914 ‰ | Huelva · 957 · 1,776 ‰ | Santa Cruz De Tenerife |
| 36 | Aguirre | AGUIRRE | 23.200 | 23.200 | sí | 224 | 52 | 0 | Gipuzkoa · 2.512 · 3,426 ‰ | Araba/Álava · 898 · 2,626 ‰ | Bizkaia · 2.921 · 2,502 ‰ | Gipuzkoa; Araba/Álava; Bizkaia |
| 37 | Flores | FLORES | 79.715 | 79.715 | sí | 49 | 52 | 0 | Badajoz · 2.770 · 4,164 ‰ | Cáceres · 1.264 · 3,256 ‰ | Huelva · 1.713 · 3,179 ‰ | Badajoz; Cáceres; Huelva |
| 38 | Luna | LUNA | 27.638 | 27.638 | sí | 188 | 52 | 0 | Córdoba · 2.843 · 3,677 ‰ | Sevilla · 2.636 · 1,333 ‰ | Cádiz · 1.457 · 1,155 ‰ | Córdoba |
| 39 | Maldonado | MALDONADO | 27.769 | 27.769 | sí | 184 | 52 | 0 | Granada · 3.323 · 3,513 ‰ | Almería · 2.517 · 3,266 ‰ | Málaga · 2.350 · 1,312 ‰ | Granada; Almería |
| 40 | Mendoza | MENDOZA | 47.342 | 47.342 | sí | 95 | 52 | 0 | Palmas, Las · 3.846 · 3,283 ‰ | Santa Cruz de Tenerife · 2.723 · 2,504 ‰ | Ávila · 317 · 1,972 ‰ | Avila |
| 41 | Miranda | MIRANDA | 35.726 | 35.726 | sí | 135 | 52 | 0 | Palmas, Las · 2.251 · 1,921 ‰ | Badajoz · 1.174 · 1,765 ‰ | Soria · 142 · 1,575 ‰ | Asturias |
| 42 | Ojeda | OJEDA | 21.033 | 21.033 | sí | 258 | 51 | 1 | Palmas, Las · 5.510 · 4,703 ‰ | Huelva · 696 · 1,292 ‰ | Sevilla · 2.372 · 1,199 ‰ | Palmas, Las |
| 43 | Paz | PAZ | 21.928 | 21.928 | sí | 240 | 52 | 0 | Coruña, A · 3.539 · 3,116 ‰ | Lugo · 972 · 2,981 ‰ | Pontevedra · 2.573 · 2,715 ‰ | Coruña, A; Lugo; Pontevedra |
| 44 | Ponce | PONCE | 25.492 | 25.492 | sí | 207 | 52 | 0 | Huelva · 1.560 · 2,895 ‰ | Cuenca · 333 · 1,666 ‰ | Sevilla · 2.705 · 1,368 ‰ | Huelva |
| 45 | Rivero | RIVERO | 32.669 | 32.669 | sí | 152 | 52 | 0 | Palmas, Las · 5.699 · 4,865 ‰ | Santa Cruz de Tenerife · 3.110 · 2,860 ‰ | Ourense · 614 · 2,011 ‰ | Palmas, Las; Santa Cruz De Tenerife |
| 46 | Rojas | ROJAS | 59.298 | 59.298 | sí | 72 | 52 | 0 | Cádiz · 3.010 · 2,386 ‰ | Córdoba · 1.748 · 2,261 ‰ | Toledo · 1.630 · 2,159 ‰ | Toledo; Málaga |
| 47 | Roldán | ROLDAN | 33.892 | 33.892 | sí | 144 | 52 | 0 | Córdoba · 3.165 · 4,094 ‰ | Sevilla · 4.410 · 2,230 ‰ | Granada · 1.994 · 2,108 ‰ | Córdoba |
| 48 | Ríos | RIOS | 44.087 | 44.087 | sí | 104 | 52 | 0 | Ceuta · 188 · 2,250 ‰ | Cádiz · 2.832 · 2,245 ‰ | Málaga · 3.868 · 2,159 ‰ | Ceuta; Málaga |
| 49 | Silva | SILVA | 48.968 | 48.968 | sí | 91 | 52 | 0 | Pontevedra · 3.451 · 3,641 ‰ | Badajoz · 2.280 · 3,428 ‰ | Ourense · 774 · 2,535 ‰ | Pontevedra; Badajoz; Ourense |
| 50 | Sosa | SOSA | 22.032 | 22.032 | sí | 237 | 52 | 0 | Palmas, Las · 7.059 · 6,025 ‰ | Santa Cruz de Tenerife · 1.816 · 1,670 ‰ | Badajoz · 822 · 1,236 ‰ | Palmas, Las |
| 51 | Vargas | VARGAS | 63.921 | 63.921 | sí | 67 | 52 | 0 | Almería · 2.905 · 3,770 ‰ | Cáceres · 1.116 · 2,875 ‰ | Sevilla · 5.507 · 2,785 ‰ | Almería; Cáceres; Sevilla |
| 52 | Vera | VERA | 43.255 | 43.255 | sí | 108 | 52 | 0 | Murcia · 4.093 · 2,579 ‰ | Santa Cruz de Tenerife · 2.600 · 2,391 ‰ | Palmas, Las · 2.514 · 2,146 ‰ | Murcia |

Columnas TOP: provincia · personas · tasa por mil habitantes, como primer apellido. «Antes» = las provincias que daba el top-50 provincial de la cosecha anterior (parcial).

## 2. Todas las provincias, por apellido (primer apellido: personas y ‰)

Las filas marcadas ★ son las tres de mayor tasa. «.» = dato oculto por secreto estadístico (INE).

### Quiroga (QUIROGA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 20 | 0,051 | Jaén | 9 | 0,015 |
| Alicante/Alacant | 209 | 0,103 | ★ León | 259 | 0,578 |
| Almería | 62 | 0,080 | Lleida | 63 | 0,137 |
| Araba/Álava | 36 | 0,105 | ★ Lugo | 622 | 1,908 |
| Asturias | 225 | 0,222 | Madrid | 1.393 | 0,196 |
| Ávila | 53 | 0,330 | Málaga | 193 | 0,108 |
| Badajoz | 33 | 0,050 | Murcia | 111 | 0,070 |
| Balears, Illes | 201 | 0,161 | Navarra | 66 | 0,097 |
| Barcelona | 973 | 0,163 | ★ Ourense | 249 | 0,816 |
| Bizkaia | 194 | 0,166 | Palencia | 14 | 0,088 |
| Burgos | 32 | 0,088 | Palmas, Las | 116 | 0,099 |
| Cáceres | 35 | 0,090 | Pontevedra | 253 | 0,267 |
| Cádiz | 50 | 0,040 | Rioja, La | 46 | 0,141 |
| Cantabria | 52 | 0,088 | Salamanca | 29 | 0,088 |
| Castellón/Castelló | 53 | 0,084 | Santa Cruz de Tenerife | 82 | 0,075 |
| Ciudad Real | 28 | 0,057 | Segovia | 11 | 0,070 |
| Córdoba | 24 | 0,031 | Sevilla | 150 | 0,076 |
| Coruña, A | 373 | 0,328 | Soria | 5 | 0,055 |
| Cuenca | 9 | 0,045 | Tarragona | 109 | 0,124 |
| Gipuzkoa | 71 | 0,097 | Teruel | 12 | 0,088 |
| Girona | 72 | 0,087 | Toledo | 83 | 0,110 |
| Granada | 113 | 0,119 | Valencia/València | 260 | 0,094 |
| Guadalajara | 30 | 0,105 | Valladolid | 75 | 0,142 |
| Huelva | 37 | 0,069 | Zamora | 23 | 0,139 |
| Huesca | 6 | 0,026 | Zaragoza | 43 | 0,043 |

### Carrizo (CARRIZO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| ★ Albacete | 58 | 0,148 | Huelva | 11 | 0,020 |
| Alicante/Alacant | 129 | 0,063 | Jaén | 9 | 0,015 |
| Almería | 34 | 0,044 | ★ León | 179 | 0,400 |
| Araba/Álava | 11 | 0,032 | Madrid | 356 | 0,050 |
| Asturias | 89 | 0,088 | Málaga | 64 | 0,036 |
| Badajoz | 34 | 0,051 | Murcia | 35 | 0,022 |
| Balears, Illes | 88 | 0,070 | Navarra | 12 | 0,018 |
| Barcelona | 231 | 0,039 | Ourense | 13 | 0,043 |
| Bizkaia | 45 | 0,039 | Palencia | . | . |
| Burgos | 17 | 0,047 | Palmas, Las | 14 | 0,012 |
| Cáceres | 25 | 0,064 | Pontevedra | 30 | 0,032 |
| Cádiz | 8 | 0,006 | Rioja, La | 7 | 0,021 |
| Cantabria | 8 | 0,013 | Salamanca | 13 | 0,040 |
| Castellón/Castelló | 11 | 0,018 | Santa Cruz de Tenerife | 30 | 0,028 |
| Ciudad Real | 23 | 0,046 | Segovia | 5 | 0,032 |
| Córdoba | 16 | 0,021 | Sevilla | 14 | 0,007 |
| Coruña, A | 13 | 0,011 | Tarragona | 45 | 0,051 |
| ★ Cuenca | 20 | 0,100 | Toledo | 46 | 0,061 |
| Gipuzkoa | 60 | 0,082 | Valencia/València | 80 | 0,029 |
| Girona | 32 | 0,039 | Valladolid | 7 | 0,013 |
| Granada | 22 | 0,023 | Zaragoza | 35 | 0,035 |
| Guadalajara | . | . | Melilla | 7 | 0,080 |

### Coronel (CORONEL)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 23 | 0,059 | Huesca | 6 | 0,026 |
| Alicante/Alacant | 201 | 0,099 | Jaén | 29 | 0,047 |
| Almería | 59 | 0,077 | León | 12 | 0,027 |
| Araba/Álava | 33 | 0,097 | Lleida | 8 | 0,017 |
| Asturias | 45 | 0,044 | ★ Madrid | 1.233 | 0,173 |
| Ávila | 10 | 0,062 | Málaga | 181 | 0,101 |
| Badajoz | 76 | 0,114 | Murcia | 220 | 0,139 |
| Balears, Illes | 131 | 0,105 | Navarra | 53 | 0,078 |
| Barcelona | 649 | 0,109 | Ourense | 11 | 0,036 |
| Bizkaia | 63 | 0,054 | Palencia | 12 | 0,076 |
| Burgos | 11 | 0,030 | Palmas, Las | 53 | 0,045 |
| Cáceres | 8 | 0,021 | Pontevedra | 59 | 0,062 |
| Cádiz | 83 | 0,066 | Rioja, La | 13 | 0,040 |
| Cantabria | 24 | 0,040 | Salamanca | 10 | 0,030 |
| Castellón/Castelló | 33 | 0,053 | Santa Cruz de Tenerife | 57 | 0,052 |
| ★ Ciudad Real | 112 | 0,226 | Segovia | 9 | 0,057 |
| Córdoba | 41 | 0,053 | Sevilla | 256 | 0,129 |
| Coruña, A | 30 | 0,026 | Soria | 6 | 0,067 |
| Cuenca | 11 | 0,055 | Tarragona | 46 | 0,053 |
| Gipuzkoa | 23 | 0,031 | Toledo | 62 | 0,082 |
| Girona | 56 | 0,067 | Valencia/València | 194 | 0,070 |
| Granada | 31 | 0,033 | Valladolid | 11 | 0,021 |
| Guadalajara | 31 | 0,108 | Zamora | 6 | 0,036 |
| ★ Huelva | 800 | 1,485 | Zaragoza | 52 | 0,052 |

### Cáceres (CACERES)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 71 | 0,182 | León | 42 | 0,094 |
| Alicante/Alacant | 537 | 0,264 | Lleida | 73 | 0,159 |
| Almería | 279 | 0,362 | Lugo | 24 | 0,074 |
| Araba/Álava | 73 | 0,213 | Madrid | 3.757 | 0,528 |
| Asturias | 168 | 0,165 | Málaga | 785 | 0,438 |
| Ávila | 43 | 0,268 | Murcia | 452 | 0,285 |
| ★ Badajoz | 990 | 1,488 | Navarra | 147 | 0,215 |
| Balears, Illes | 582 | 0,466 | Ourense | 23 | 0,075 |
| Barcelona | 2.567 | 0,431 | Palencia | 21 | 0,132 |
| Bizkaia | 412 | 0,353 | Palmas, Las | 1.106 | 0,944 |
| Burgos | 86 | 0,237 | Pontevedra | 126 | 0,133 |
| ★ Cáceres | 485 | 1,249 | Rioja, La | 75 | 0,229 |
| Cádiz | 567 | 0,449 | Salamanca | 168 | 0,511 |
| Cantabria | 95 | 0,160 | Santa Cruz de Tenerife | 854 | 0,785 |
| Castellón/Castelló | 115 | 0,183 | Segovia | 123 | 0,777 |
| Ciudad Real | 98 | 0,198 | Sevilla | 1.384 | 0,700 |
| Córdoba | 550 | 0,711 | Soria | 19 | 0,211 |
| Coruña, A | 108 | 0,095 | Tarragona | 208 | 0,238 |
| Cuenca | 32 | 0,160 | Teruel | 14 | 0,103 |
| Gipuzkoa | 276 | 0,376 | Toledo | 426 | 0,564 |
| Girona | 487 | 0,586 | Valencia/València | 620 | 0,224 |
| Granada | 591 | 0,625 | Valladolid | 221 | 0,418 |
| Guadalajara | 122 | 0,427 | Zamora | 14 | 0,085 |
| ★ Huelva | 770 | 1,429 | Zaragoza | 214 | 0,214 |
| Huesca | 71 | 0,309 | Ceuta | 15 | 0,179 |
| Jaén | 118 | 0,191 | Melilla | 7 | 0,080 |

### Córdoba (CORDOBA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 456 | 1,167 | León | 84 | 0,187 |
| Alicante/Alacant | 1.061 | 0,522 | Lleida | 66 | 0,144 |
| Almería | 217 | 0,282 | Lugo | 20 | 0,061 |
| Araba/Álava | 67 | 0,196 | Madrid | 2.551 | 0,359 |
| Asturias | 138 | 0,136 | Málaga | 1.468 | 0,820 |
| Ávila | 24 | 0,149 | Murcia | 652 | 0,411 |
| Badajoz | 164 | 0,247 | Navarra | 186 | 0,272 |
| Balears, Illes | 437 | 0,350 | Ourense | 20 | 0,066 |
| Barcelona | 2.093 | 0,351 | Palencia | 7 | 0,044 |
| Bizkaia | 264 | 0,226 | Palmas, Las | 189 | 0,161 |
| Burgos | 93 | 0,256 | Pontevedra | 88 | 0,093 |
| Cáceres | 63 | 0,162 | Rioja, La | 77 | 0,236 |
| Cádiz | 613 | 0,486 | Salamanca | 20 | 0,061 |
| Cantabria | 83 | 0,140 | Santa Cruz de Tenerife | 272 | 0,250 |
| Castellón/Castelló | 123 | 0,196 | Segovia | 19 | 0,120 |
| ★ Ciudad Real | 733 | 1,481 | Sevilla | 627 | 0,317 |
| ★ Córdoba | 1.970 | 2,548 | Soria | 15 | 0,166 |
| Coruña, A | 65 | 0,057 | Tarragona | 295 | 0,337 |
| ★ Cuenca | 240 | 1,201 | Teruel | 30 | 0,220 |
| Gipuzkoa | 125 | 0,170 | Toledo | 208 | 0,275 |
| Girona | 319 | 0,384 | Valencia/València | 1.097 | 0,397 |
| Granada | 962 | 1,017 | Valladolid | 51 | 0,096 |
| Guadalajara | 114 | 0,399 | Zamora | 12 | 0,072 |
| Huelva | 66 | 0,122 | Zaragoza | 159 | 0,159 |
| Huesca | 37 | 0,161 | Ceuta | 34 | 0,407 |
| Jaén | 384 | 0,621 | Melilla | 18 | 0,207 |

### Godoy (GODOY)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 51 | 0,131 | León | 17 | 0,038 |
| Alicante/Alacant | 345 | 0,170 | Lleida | 119 | 0,260 |
| Almería | 486 | 0,631 | Lugo | 7 | 0,021 |
| Araba/Álava | 70 | 0,205 | Madrid | 2.190 | 0,308 |
| Asturias | 85 | 0,084 | ★ Málaga | 1.258 | 0,702 |
| Ávila | 15 | 0,093 | Murcia | 205 | 0,129 |
| ★ Badajoz | 520 | 0,782 | Navarra | 81 | 0,118 |
| Balears, Illes | 391 | 0,313 | Ourense | 54 | 0,177 |
| Barcelona | 1.762 | 0,296 | Palencia | 20 | 0,126 |
| Bizkaia | 334 | 0,286 | ★ Palmas, Las | 1.868 | 1,594 |
| Burgos | 36 | 0,099 | Pontevedra | 151 | 0,159 |
| Cáceres | 123 | 0,317 | Rioja, La | 45 | 0,138 |
| Cádiz | 346 | 0,274 | Salamanca | 35 | 0,107 |
| Cantabria | 46 | 0,077 | Santa Cruz de Tenerife | 182 | 0,167 |
| Castellón/Castelló | 108 | 0,172 | Segovia | 6 | 0,038 |
| Ciudad Real | 80 | 0,162 | Sevilla | 584 | 0,295 |
| Córdoba | 330 | 0,427 | Soria | 5 | 0,055 |
| Coruña, A | 107 | 0,094 | Tarragona | 181 | 0,207 |
| Cuenca | 57 | 0,285 | Teruel | 15 | 0,110 |
| Gipuzkoa | 304 | 0,415 | Toledo | 163 | 0,216 |
| Girona | 291 | 0,350 | Valencia/València | 571 | 0,207 |
| Granada | 210 | 0,222 | Valladolid | 46 | 0,087 |
| Guadalajara | 45 | 0,157 | Zamora | . | . |
| Huelva | 99 | 0,184 | Zaragoza | 147 | 0,147 |
| Huesca | 9 | 0,039 | Ceuta | 20 | 0,239 |
| Jaén | 407 | 0,658 | Melilla | . | . |

### Ledesma (LEDESMA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 33 | 0,084 | León | 42 | 0,094 |
| Alicante/Alacant | 180 | 0,089 | Lleida | 56 | 0,122 |
| Almería | 119 | 0,154 | Lugo | 17 | 0,052 |
| Araba/Álava | 35 | 0,102 | Madrid | 1.668 | 0,234 |
| Asturias | 97 | 0,096 | Málaga | 656 | 0,366 |
| Ávila | 6 | 0,037 | Murcia | 68 | 0,043 |
| ★ Badajoz | 568 | 0,854 | Navarra | 70 | 0,102 |
| Balears, Illes | 328 | 0,262 | Ourense | 13 | 0,043 |
| Barcelona | 964 | 0,162 | Palencia | 7 | 0,044 |
| Bizkaia | 302 | 0,259 | Palmas, Las | 85 | 0,073 |
| Burgos | 34 | 0,094 | Pontevedra | 31 | 0,033 |
| Cáceres | 43 | 0,111 | Rioja, La | 87 | 0,266 |
| Cádiz | 271 | 0,215 | ★ Salamanca | 217 | 0,661 |
| Cantabria | 29 | 0,049 | ★ Santa Cruz de Tenerife | 836 | 0,769 |
| Castellón/Castelló | 47 | 0,075 | Segovia | 17 | 0,107 |
| Ciudad Real | 77 | 0,156 | Sevilla | 780 | 0,394 |
| Córdoba | 224 | 0,290 | Soria | 49 | 0,543 |
| Coruña, A | 42 | 0,037 | Tarragona | 119 | 0,136 |
| Cuenca | 8 | 0,040 | Teruel | 12 | 0,088 |
| Gipuzkoa | 104 | 0,142 | Toledo | 194 | 0,257 |
| Girona | 118 | 0,142 | Valencia/València | 228 | 0,082 |
| Granada | 125 | 0,132 | Valladolid | 70 | 0,132 |
| Guadalajara | 50 | 0,175 | Zamora | 81 | 0,489 |
| Huelva | 35 | 0,065 | Zaragoza | 333 | 0,334 |
| Huesca | 15 | 0,065 | Ceuta | 5 | 0,060 |
| Jaén | 88 | 0,142 |  |  |  |

### Villalba (VILLALBA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 183 | 0,468 | León | 65 | 0,145 |
| Alicante/Alacant | 595 | 0,293 | Lleida | 102 | 0,223 |
| Almería | 137 | 0,178 | Lugo | 75 | 0,230 |
| Araba/Álava | 96 | 0,281 | Madrid | 3.701 | 0,520 |
| Asturias | 174 | 0,171 | ★ Málaga | 2.120 | 1,184 |
| Ávila | 17 | 0,106 | Murcia | 570 | 0,359 |
| Badajoz | 292 | 0,439 | Navarra | 92 | 0,135 |
| Balears, Illes | 413 | 0,330 | Ourense | 11 | 0,036 |
| Barcelona | 2.193 | 0,368 | Palencia | 158 | 0,996 |
| Bizkaia | 419 | 0,359 | Palmas, Las | 413 | 0,353 |
| Burgos | 45 | 0,124 | Pontevedra | 101 | 0,107 |
| Cáceres | 97 | 0,250 | Rioja, La | 43 | 0,132 |
| Cádiz | 972 | 0,771 | Salamanca | 23 | 0,070 |
| Cantabria | 125 | 0,211 | Santa Cruz de Tenerife | 266 | 0,245 |
| Castellón/Castelló | 396 | 0,631 | Segovia | 29 | 0,183 |
| Ciudad Real | 107 | 0,216 | Sevilla | 1.384 | 0,700 |
| Córdoba | 606 | 0,784 | Soria | 21 | 0,233 |
| Coruña, A | 115 | 0,101 | Tarragona | 379 | 0,433 |
| ★ Cuenca | 228 | 1,141 | ★ Teruel | 182 | 1,337 |
| Gipuzkoa | 99 | 0,135 | Toledo | 461 | 0,611 |
| Girona | 216 | 0,260 | Valencia/València | 1.928 | 0,698 |
| Granada | 332 | 0,351 | Valladolid | 216 | 0,409 |
| Guadalajara | 192 | 0,672 | Zamora | 62 | 0,374 |
| Huelva | 111 | 0,206 | Zaragoza | 613 | 0,614 |
| Huesca | 61 | 0,265 | Ceuta | 30 | 0,359 |
| Jaén | 99 | 0,160 | Melilla | 17 | 0,195 |

### Correa (CORREA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 137 | 0,351 | León | 73 | 0,163 |
| Alicante/Alacant | 636 | 0,313 | Lleida | 95 | 0,207 |
| Almería | 230 | 0,298 | Lugo | 75 | 0,230 |
| Araba/Álava | 99 | 0,290 | Madrid | 3.008 | 0,423 |
| Asturias | 204 | 0,201 | Málaga | 734 | 0,410 |
| Ávila | 40 | 0,249 | Murcia | 441 | 0,278 |
| Badajoz | 715 | 1,075 | Navarra | 229 | 0,335 |
| Balears, Illes | 599 | 0,479 | Ourense | 142 | 0,465 |
| Barcelona | 2.299 | 0,386 | Palencia | 26 | 0,164 |
| Bizkaia | 454 | 0,389 | Palmas, Las | 830 | 0,708 |
| Burgos | 80 | 0,221 | Pontevedra | 884 | 0,933 |
| Cáceres | 160 | 0,412 | Rioja, La | 96 | 0,294 |
| Cádiz | 509 | 0,404 | Salamanca | 58 | 0,177 |
| Cantabria | 180 | 0,303 | ★ Santa Cruz de Tenerife | 2.304 | 2,119 |
| Castellón/Castelló | 156 | 0,249 | Segovia | 51 | 0,322 |
| Ciudad Real | 73 | 0,148 | Sevilla | 1.085 | 0,549 |
| Córdoba | 78 | 0,101 | Soria | 13 | 0,144 |
| Coruña, A | 327 | 0,288 | Tarragona | 255 | 0,291 |
| Cuenca | 38 | 0,190 | Teruel | 35 | 0,257 |
| Gipuzkoa | 183 | 0,250 | Toledo | 230 | 0,305 |
| Girona | 260 | 0,313 | Valencia/València | 917 | 0,332 |
| ★ Granada | 1.166 | 1,233 | Valladolid | 159 | 0,301 |
| Guadalajara | 100 | 0,350 | Zamora | 61 | 0,368 |
| ★ Huelva | 730 | 1,355 | Zaragoza | 230 | 0,230 |
| Huesca | 42 | 0,183 | Ceuta | 13 | 0,156 |
| Jaén | 42 | 0,068 | Melilla | 19 | 0,218 |

### Duarte (DUARTE)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 61 | 0,156 | León | 118 | 0,263 |
| Alicante/Alacant | 404 | 0,199 | Lleida | 78 | 0,170 |
| Almería | 271 | 0,352 | Lugo | 118 | 0,362 |
| Araba/Álava | 122 | 0,357 | Madrid | 2.483 | 0,349 |
| Asturias | 415 | 0,409 | ★ Málaga | 1.278 | 0,713 |
| Ávila | 65 | 0,404 | Murcia | 333 | 0,210 |
| Badajoz | 331 | 0,498 | Navarra | 128 | 0,187 |
| Balears, Illes | 383 | 0,306 | Ourense | 88 | 0,288 |
| Barcelona | 2.109 | 0,354 | Palencia | 31 | 0,195 |
| Bizkaia | 340 | 0,291 | Palmas, Las | 486 | 0,415 |
| Burgos | 86 | 0,237 | Pontevedra | 570 | 0,601 |
| Cáceres | 226 | 0,582 | Rioja, La | 93 | 0,285 |
| ★ Cádiz | 917 | 0,727 | Salamanca | 99 | 0,301 |
| Cantabria | 119 | 0,200 | Santa Cruz de Tenerife | 250 | 0,230 |
| Castellón/Castelló | 91 | 0,145 | Segovia | 30 | 0,190 |
| Ciudad Real | 72 | 0,145 | Sevilla | 903 | 0,457 |
| Córdoba | 191 | 0,247 | Soria | 14 | 0,155 |
| Coruña, A | 426 | 0,375 | Tarragona | 220 | 0,251 |
| Cuenca | 33 | 0,165 | Teruel | 18 | 0,132 |
| Gipuzkoa | 186 | 0,254 | Toledo | 168 | 0,222 |
| Girona | 201 | 0,242 | Valencia/València | 514 | 0,186 |
| Granada | 308 | 0,326 | Valladolid | 54 | 0,102 |
| Guadalajara | 80 | 0,280 | Zamora | 17 | 0,103 |
| Huelva | 204 | 0,379 | Zaragoza | 377 | 0,378 |
| Huesca | 63 | 0,274 | ★ Ceuta | 69 | 0,826 |
| Jaén | 51 | 0,083 | Melilla | 11 | 0,126 |

### Escobar (ESCOBAR)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 462 | 1,182 | León | 143 | 0,319 |
| Alicante/Alacant | 974 | 0,479 | Lleida | 120 | 0,262 |
| ★ Almería | 998 | 1,295 | Lugo | 58 | 0,178 |
| Araba/Álava | 129 | 0,377 | Madrid | 6.001 | 0,844 |
| Asturias | 364 | 0,359 | Málaga | 1.866 | 1,042 |
| Ávila | 51 | 0,317 | Murcia | 671 | 0,423 |
| ★ Badajoz | 883 | 1,328 | Navarra | 255 | 0,373 |
| Balears, Illes | 875 | 0,700 | Ourense | 68 | 0,223 |
| Barcelona | 3.745 | 0,628 | Palencia | 72 | 0,454 |
| Bizkaia | 538 | 0,461 | Palmas, Las | 447 | 0,382 |
| Burgos | 101 | 0,278 | Pontevedra | 162 | 0,171 |
| Cáceres | 131 | 0,337 | Rioja, La | 111 | 0,340 |
| Cádiz | 811 | 0,643 | Salamanca | 89 | 0,271 |
| Cantabria | 179 | 0,302 | Santa Cruz de Tenerife | 912 | 0,839 |
| Castellón/Castelló | 251 | 0,400 | Segovia | 149 | 0,942 |
| Ciudad Real | 584 | 1,180 | Sevilla | 1.815 | 0,918 |
| Córdoba | 558 | 0,722 | Soria | 37 | 0,410 |
| Coruña, A | 165 | 0,145 | Tarragona | 457 | 0,522 |
| Cuenca | 210 | 1,051 | Teruel | 49 | 0,360 |
| Gipuzkoa | 208 | 0,284 | Toledo | 921 | 1,220 |
| Girona | 403 | 0,485 | Valencia/València | 1.728 | 0,625 |
| Granada | 940 | 0,994 | Valladolid | 152 | 0,288 |
| Guadalajara | 172 | 0,602 | Zamora | 43 | 0,260 |
| ★ Huelva | 680 | 1,262 | Zaragoza | 329 | 0,330 |
| Huesca | 113 | 0,491 | Ceuta | 14 | 0,168 |
| Jaén | 220 | 0,356 | Melilla | 79 | 0,907 |

### Figueroa (FIGUEROA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 43 | 0,110 | León | 48 | 0,107 |
| Alicante/Alacant | 352 | 0,173 | Lleida | 62 | 0,135 |
| Almería | 208 | 0,270 | Lugo | 137 | 0,420 |
| Araba/Álava | 46 | 0,135 | Madrid | 2.682 | 0,377 |
| Asturias | 137 | 0,135 | Málaga | 400 | 0,223 |
| Ávila | 20 | 0,124 | Murcia | 203 | 0,128 |
| Badajoz | 108 | 0,162 | Navarra | 164 | 0,240 |
| Balears, Illes | 354 | 0,283 | Ourense | 59 | 0,193 |
| Barcelona | 1.751 | 0,294 | Palencia | 12 | 0,076 |
| Bizkaia | 150 | 0,129 | Palmas, Las | 791 | 0,675 |
| Burgos | 41 | 0,113 | ★ Pontevedra | 1.610 | 1,699 |
| Cáceres | 56 | 0,144 | Rioja, La | 44 | 0,135 |
| Cádiz | 385 | 0,305 | Salamanca | 30 | 0,091 |
| Cantabria | 81 | 0,136 | ★ Santa Cruz de Tenerife | 807 | 0,742 |
| Castellón/Castelló | 100 | 0,159 | Segovia | 40 | 0,253 |
| Ciudad Real | 77 | 0,156 | Sevilla | 750 | 0,379 |
| Córdoba | 161 | 0,208 | Soria | 16 | 0,177 |
| ★ Coruña, A | 777 | 0,684 | Tarragona | 161 | 0,184 |
| Cuenca | 36 | 0,180 | Teruel | 12 | 0,088 |
| Gipuzkoa | 206 | 0,281 | Toledo | 254 | 0,336 |
| Girona | 209 | 0,252 | Valencia/València | 563 | 0,204 |
| Granada | 228 | 0,241 | Valladolid | 113 | 0,214 |
| Guadalajara | 70 | 0,245 | Zamora | 37 | 0,223 |
| Huelva | 71 | 0,132 | Zaragoza | 165 | 0,165 |
| Huesca | 28 | 0,122 | Ceuta | 28 | 0,335 |
| Jaén | 120 | 0,194 | Melilla | 6 | 0,069 |

### Guzmán (GUZMAN)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 129 | 0,330 | León | 145 | 0,324 |
| Alicante/Alacant | 973 | 0,478 | Lleida | 160 | 0,349 |
| Almería | 396 | 0,514 | Lugo | 105 | 0,322 |
| Araba/Álava | 185 | 0,541 | Madrid | 6.487 | 0,912 |
| Asturias | 282 | 0,278 | ★ Málaga | 2.776 | 1,550 |
| Ávila | 108 | 0,672 | Murcia | 949 | 0,598 |
| Badajoz | 383 | 0,576 | Navarra | 294 | 0,430 |
| Balears, Illes | 775 | 0,620 | Ourense | 164 | 0,537 |
| Barcelona | 4.284 | 0,719 | Palencia | 74 | 0,466 |
| Bizkaia | 643 | 0,551 | Palmas, Las | 782 | 0,667 |
| Burgos | 139 | 0,383 | Pontevedra | 287 | 0,303 |
| Cáceres | 244 | 0,629 | Rioja, La | 102 | 0,312 |
| Cádiz | 1.260 | 0,999 | Salamanca | 108 | 0,329 |
| Cantabria | 223 | 0,376 | Santa Cruz de Tenerife | 765 | 0,704 |
| Castellón/Castelló | 451 | 0,719 | Segovia | 68 | 0,430 |
| Ciudad Real | 439 | 0,887 | Sevilla | 1.740 | 0,880 |
| Córdoba | 604 | 0,781 | Soria | 33 | 0,366 |
| Coruña, A | 399 | 0,351 | Tarragona | 541 | 0,618 |
| Cuenca | 47 | 0,235 | Teruel | 40 | 0,294 |
| Gipuzkoa | 268 | 0,366 | ★ Toledo | 1.037 | 1,373 |
| Girona | 423 | 0,509 | Valencia/València | 1.719 | 0,622 |
| Granada | 912 | 0,964 | Valladolid | 194 | 0,367 |
| Guadalajara | 202 | 0,707 | Zamora | 23 | 0,139 |
| Huelva | 449 | 0,833 | Zaragoza | 453 | 0,454 |
| Huesca | 73 | 0,317 | Ceuta | 55 | 0,658 |
| ★ Jaén | 876 | 1,417 | Melilla | 34 | 0,391 |

### Juárez (JUAREZ)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| ★ Albacete | 430 | 1,100 | León | 319 | 0,712 |
| Alicante/Alacant | 1.201 | 0,591 | Lleida | 147 | 0,321 |
| Almería | 531 | 0,689 | Lugo | 20 | 0,061 |
| Araba/Álava | 59 | 0,173 | Madrid | 3.443 | 0,484 |
| Asturias | 120 | 0,118 | Málaga | 472 | 0,264 |
| Ávila | 100 | 0,622 | Murcia | 727 | 0,458 |
| Badajoz | 149 | 0,224 | Navarra | 135 | 0,197 |
| Balears, Illes | 336 | 0,269 | Ourense | 8 | 0,026 |
| Barcelona | 2.329 | 0,391 | Palencia | 123 | 0,775 |
| Bizkaia | 302 | 0,259 | Palmas, Las | 97 | 0,083 |
| Burgos | 140 | 0,386 | Pontevedra | 81 | 0,085 |
| Cáceres | 133 | 0,343 | Rioja, La | 62 | 0,190 |
| Cádiz | 169 | 0,134 | Salamanca | 67 | 0,204 |
| Cantabria | 215 | 0,362 | Santa Cruz de Tenerife | 76 | 0,070 |
| Castellón/Castelló | 405 | 0,645 | Segovia | 61 | 0,385 |
| Ciudad Real | 376 | 0,760 | Sevilla | 318 | 0,161 |
| Córdoba | 274 | 0,354 | Soria | . | . |
| Coruña, A | 61 | 0,054 | Tarragona | 230 | 0,263 |
| Cuenca | 30 | 0,150 | Teruel | 33 | 0,242 |
| Gipuzkoa | 148 | 0,202 | ★ Toledo | 809 | 1,071 |
| Girona | 249 | 0,300 | Valencia/València | 959 | 0,347 |
| Granada | 617 | 0,652 | Valladolid | 424 | 0,802 |
| Guadalajara | 137 | 0,479 | ★ Zamora | 201 | 1,214 |
| Huelva | 34 | 0,063 | Zaragoza | 194 | 0,194 |
| Huesca | 60 | 0,261 | Ceuta | 14 | 0,168 |
| Jaén | 540 | 0,874 | Melilla | 17 | 0,195 |

### Peralta (PERALTA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 124 | 0,317 | León | 46 | 0,103 |
| Alicante/Alacant | 374 | 0,184 | Lleida | 177 | 0,386 |
| Almería | 412 | 0,535 | Lugo | 43 | 0,132 |
| Araba/Álava | 39 | 0,114 | Madrid | 2.645 | 0,372 |
| Asturias | 167 | 0,165 | Málaga | 860 | 0,480 |
| Ávila | 63 | 0,392 | Murcia | 383 | 0,241 |
| Badajoz | 83 | 0,125 | Navarra | 266 | 0,389 |
| Balears, Illes | 519 | 0,415 | Ourense | 42 | 0,138 |
| Barcelona | 2.350 | 0,394 | Palencia | 13 | 0,082 |
| Bizkaia | 295 | 0,253 | Palmas, Las | 225 | 0,192 |
| Burgos | 68 | 0,188 | Pontevedra | 63 | 0,066 |
| Cáceres | 32 | 0,082 | Rioja, La | 81 | 0,248 |
| ★ Cádiz | 859 | 0,681 | Salamanca | 109 | 0,332 |
| Cantabria | 137 | 0,231 | Santa Cruz de Tenerife | 94 | 0,086 |
| Castellón/Castelló | 192 | 0,306 | Segovia | 38 | 0,240 |
| Ciudad Real | 258 | 0,521 | Sevilla | 460 | 0,233 |
| Córdoba | 133 | 0,172 | Soria | 18 | 0,200 |
| Coruña, A | 113 | 0,100 | Tarragona | 252 | 0,288 |
| Cuenca | 122 | 0,610 | ★ Teruel | 143 | 1,051 |
| Gipuzkoa | 144 | 0,196 | Toledo | 168 | 0,222 |
| Girona | 281 | 0,338 | Valencia/València | 729 | 0,264 |
| Granada | 558 | 0,590 | Valladolid | 96 | 0,182 |
| Guadalajara | 72 | 0,252 | Zamora | 70 | 0,423 |
| Huelva | 36 | 0,067 | Zaragoza | 556 | 0,557 |
| ★ Huesca | 271 | 1,178 | Ceuta | 24 | 0,287 |
| Jaén | 341 | 0,552 | Melilla | 8 | 0,092 |

### Mansilla (MANSILLA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| ★ Albacete | 160 | 0,409 | Huesca | 21 | 0,091 |
| Alicante/Alacant | 174 | 0,086 | Jaén | 86 | 0,139 |
| Almería | 32 | 0,042 | León | 115 | 0,257 |
| Araba/Álava | 35 | 0,102 | Lleida | 42 | 0,092 |
| Asturias | 84 | 0,083 | Lugo | 5 | 0,015 |
| Ávila | 7 | 0,044 | Madrid | 1.470 | 0,207 |
| ★ Badajoz | 402 | 0,604 | Málaga | 113 | 0,063 |
| Balears, Illes | 172 | 0,138 | Murcia | 80 | 0,050 |
| Barcelona | 812 | 0,136 | Navarra | 29 | 0,042 |
| Bizkaia | 97 | 0,083 | Palencia | 16 | 0,101 |
| Burgos | 77 | 0,212 | Palmas, Las | 31 | 0,026 |
| Cáceres | 14 | 0,036 | Pontevedra | 34 | 0,036 |
| Cádiz | 43 | 0,034 | Rioja, La | 22 | 0,067 |
| Cantabria | 40 | 0,067 | Salamanca | 10 | 0,030 |
| Castellón/Castelló | 56 | 0,089 | Santa Cruz de Tenerife | 37 | 0,034 |
| ★ Ciudad Real | 324 | 0,655 | Sevilla | 79 | 0,040 |
| Córdoba | 239 | 0,309 | Tarragona | 127 | 0,145 |
| Coruña, A | 106 | 0,093 | Teruel | 30 | 0,220 |
| Cuenca | 51 | 0,255 | Toledo | 112 | 0,148 |
| Gipuzkoa | 43 | 0,059 | Valencia/València | 293 | 0,106 |
| Girona | 35 | 0,042 | Valladolid | 96 | 0,182 |
| Granada | 91 | 0,096 | Zamora | 19 | 0,115 |
| Guadalajara | 66 | 0,231 | Zaragoza | 61 | 0,061 |
| Huelva | 33 | 0,061 | Melilla | 9 | 0,103 |

### Ayala (AYALA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 96 | 0,246 | León | 56 | 0,125 |
| Alicante/Alacant | 696 | 0,342 | Lleida | 149 | 0,325 |
| ★ Almería | 590 | 0,766 | Lugo | 26 | 0,080 |
| Araba/Álava | 217 | 0,635 | Madrid | 3.225 | 0,453 |
| Asturias | 190 | 0,187 | Málaga | 858 | 0,479 |
| Ávila | 34 | 0,212 | ★ Murcia | 2.158 | 1,360 |
| Badajoz | 73 | 0,110 | Navarra | 370 | 0,541 |
| Balears, Illes | 478 | 0,382 | Ourense | 28 | 0,092 |
| Barcelona | 2.753 | 0,462 | Palencia | 14 | 0,088 |
| Bizkaia | 513 | 0,440 | Palmas, Las | 300 | 0,256 |
| ★ Burgos | 316 | 0,871 | Pontevedra | 73 | 0,077 |
| Cáceres | 80 | 0,206 | Rioja, La | 213 | 0,652 |
| Cádiz | 517 | 0,410 | Salamanca | 37 | 0,113 |
| Cantabria | 101 | 0,170 | Santa Cruz de Tenerife | 282 | 0,259 |
| Castellón/Castelló | 125 | 0,199 | Segovia | 20 | 0,126 |
| Ciudad Real | 123 | 0,249 | Sevilla | 1.006 | 0,509 |
| Córdoba | 406 | 0,525 | Soria | 24 | 0,266 |
| Coruña, A | 120 | 0,106 | Tarragona | 276 | 0,315 |
| Cuenca | 71 | 0,355 | Teruel | 25 | 0,184 |
| Gipuzkoa | 194 | 0,265 | Toledo | 203 | 0,269 |
| Girona | 249 | 0,300 | Valencia/València | 782 | 0,283 |
| Granada | 305 | 0,322 | Valladolid | 175 | 0,331 |
| Guadalajara | 81 | 0,283 | Zamora | 5 | 0,030 |
| Huelva | 72 | 0,134 | Zaragoza | 282 | 0,282 |
| Huesca | 71 | 0,309 | Ceuta | 49 | 0,586 |
| Jaén | 119 | 0,193 | Melilla | 34 | 0,391 |

### Barrios (BARRIOS)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 47 | 0,120 | León | 254 | 0,567 |
| Alicante/Alacant | 388 | 0,191 | Lleida | 63 | 0,137 |
| Almería | 146 | 0,189 | Lugo | 48 | 0,147 |
| Araba/Álava | 88 | 0,257 | Madrid | 3.826 | 0,538 |
| Asturias | 254 | 0,250 | Málaga | 528 | 0,295 |
| Ávila | 51 | 0,317 | Murcia | 196 | 0,124 |
| Badajoz | 256 | 0,385 | Navarra | 133 | 0,194 |
| Balears, Illes | 387 | 0,310 | Ourense | 50 | 0,164 |
| Barcelona | 1.645 | 0,276 | Palencia | 45 | 0,284 |
| Bizkaia | 476 | 0,408 | Palmas, Las | 980 | 0,837 |
| Burgos | 181 | 0,499 | Pontevedra | 117 | 0,123 |
| Cáceres | 226 | 0,582 | Rioja, La | 203 | 0,621 |
| Cádiz | 1.091 | 0,865 | ★ Salamanca | 287 | 0,874 |
| Cantabria | 99 | 0,167 | ★ Santa Cruz de Tenerife | 1.180 | 1,085 |
| Castellón/Castelló | 138 | 0,220 | Segovia | 42 | 0,265 |
| Ciudad Real | 160 | 0,323 | Sevilla | 1.220 | 0,617 |
| Córdoba | 302 | 0,391 | Soria | 49 | 0,543 |
| Coruña, A | 138 | 0,122 | Tarragona | 217 | 0,248 |
| Cuenca | 109 | 0,545 | Teruel | 22 | 0,162 |
| Gipuzkoa | 136 | 0,186 | Toledo | 504 | 0,667 |
| Girona | 161 | 0,194 | Valencia/València | 688 | 0,249 |
| Granada | 216 | 0,228 | Valladolid | 327 | 0,619 |
| Guadalajara | 111 | 0,388 | ★ Zamora | 405 | 2,446 |
| Huelva | 244 | 0,453 | Zaragoza | 352 | 0,353 |
| Huesca | 50 | 0,217 | Ceuta | 19 | 0,227 |
| Jaén | 200 | 0,324 | Melilla | 6 | 0,069 |

### Acuña (ACUÑA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 13 | 0,033 | Jaén | 40 | 0,065 |
| Alicante/Alacant | 194 | 0,095 | León | 13 | 0,029 |
| Almería | 62 | 0,080 | Lleida | 50 | 0,109 |
| Araba/Álava | 38 | 0,111 | Lugo | 26 | 0,080 |
| Asturias | 190 | 0,187 | Madrid | 1.193 | 0,168 |
| Ávila | 5 | 0,031 | Málaga | 297 | 0,166 |
| Badajoz | 86 | 0,129 | Murcia | 123 | 0,078 |
| Balears, Illes | 209 | 0,167 | Navarra | 72 | 0,105 |
| Barcelona | 813 | 0,136 | Ourense | 58 | 0,190 |
| Bizkaia | 134 | 0,115 | Palencia | 26 | 0,164 |
| Burgos | 9 | 0,025 | Palmas, Las | 266 | 0,227 |
| Cáceres | 95 | 0,245 | ★ Pontevedra | 1.503 | 1,586 |
| ★ Cádiz | 430 | 0,341 | Rioja, La | 7 | 0,021 |
| Cantabria | 48 | 0,081 | Salamanca | 28 | 0,085 |
| Castellón/Castelló | 31 | 0,049 | Santa Cruz de Tenerife | 239 | 0,220 |
| Ciudad Real | 26 | 0,053 | Segovia | 11 | 0,070 |
| Córdoba | 29 | 0,038 | ★ Sevilla | 801 | 0,405 |
| Coruña, A | 196 | 0,173 | Soria | . | . |
| Cuenca | 20 | 0,100 | Tarragona | 93 | 0,106 |
| Gipuzkoa | 138 | 0,188 | Teruel | 18 | 0,132 |
| Girona | 73 | 0,088 | Toledo | 72 | 0,095 |
| Granada | 58 | 0,061 | Valencia/València | 194 | 0,070 |
| Guadalajara | 40 | 0,140 | Valladolid | 120 | 0,227 |
| Huelva | 132 | 0,245 | Zamora | 6 | 0,036 |
| Huesca | 28 | 0,122 | Zaragoza | 81 | 0,081 |

### Agüero (AGUERO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 9 | 0,023 | Huesca | . | . |
| Alicante/Alacant | 129 | 0,063 | Jaén | 6 | 0,010 |
| Almería | 170 | 0,221 | León | 21 | 0,047 |
| Araba/Álava | 48 | 0,140 | Lleida | . | . |
| Asturias | 61 | 0,060 | Lugo | 10 | 0,031 |
| Ávila | 27 | 0,168 | Madrid | 1.119 | 0,157 |
| Badajoz | 12 | 0,018 | Málaga | 138 | 0,077 |
| Balears, Illes | 93 | 0,074 | Murcia | 36 | 0,023 |
| Barcelona | 490 | 0,082 | Navarra | 41 | 0,060 |
| Bizkaia | 165 | 0,141 | Ourense | 15 | 0,049 |
| Burgos | 76 | 0,210 | Palencia | 8 | 0,050 |
| Cáceres | 5 | 0,013 | Palmas, Las | 56 | 0,048 |
| Cádiz | 29 | 0,023 | Pontevedra | 30 | 0,032 |
| ★ Cantabria | 401 | 0,676 | Rioja, La | 34 | 0,104 |
| Castellón/Castelló | 20 | 0,032 | Salamanca | 19 | 0,058 |
| Ciudad Real | 29 | 0,059 | Santa Cruz de Tenerife | 79 | 0,073 |
| Córdoba | 26 | 0,034 | ★ Segovia | 39 | 0,246 |
| Coruña, A | 56 | 0,049 | Sevilla | 96 | 0,049 |
| Cuenca | . | . | Soria | 6 | 0,067 |
| Gipuzkoa | 66 | 0,090 | Tarragona | 57 | 0,065 |
| Girona | 42 | 0,051 | ★ Toledo | 336 | 0,445 |
| Granada | 28 | 0,030 | Valencia/València | 79 | 0,029 |
| Guadalajara | 34 | 0,119 | Valladolid | 39 | 0,074 |
| Huelva | 12 | 0,022 | Zaragoza | 47 | 0,047 |

### Chávez (CHAVEZ)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 67 | 0,171 | Jaén | 40 | 0,065 |
| Alicante/Alacant | 347 | 0,171 | León | 67 | 0,150 |
| Almería | 110 | 0,143 | Lleida | 96 | 0,210 |
| Araba/Álava | 59 | 0,173 | Lugo | 45 | 0,138 |
| Asturias | 148 | 0,146 | ★ Madrid | 3.416 | 0,480 |
| Ávila | 22 | 0,137 | Málaga | 276 | 0,154 |
| ★ Badajoz | 545 | 0,819 | Murcia | 394 | 0,248 |
| Balears, Illes | 380 | 0,304 | Navarra | 191 | 0,279 |
| Barcelona | 2.517 | 0,422 | Ourense | 37 | 0,121 |
| Bizkaia | 239 | 0,205 | Palencia | 17 | 0,107 |
| Burgos | 67 | 0,185 | Palmas, Las | 275 | 0,235 |
| Cáceres | 60 | 0,155 | Pontevedra | 102 | 0,108 |
| Cádiz | 96 | 0,076 | Rioja, La | 73 | 0,223 |
| Cantabria | 109 | 0,184 | Salamanca | 63 | 0,192 |
| Castellón/Castelló | 82 | 0,131 | ★ Santa Cruz de Tenerife | 1.375 | 1,265 |
| Ciudad Real | 54 | 0,109 | Segovia | 38 | 0,240 |
| Córdoba | 108 | 0,140 | Sevilla | 472 | 0,239 |
| Coruña, A | 106 | 0,093 | Soria | 34 | 0,377 |
| Cuenca | 40 | 0,200 | Tarragona | 194 | 0,222 |
| Gipuzkoa | 153 | 0,209 | Teruel | 20 | 0,147 |
| Girona | 203 | 0,244 | Toledo | 265 | 0,351 |
| Granada | 98 | 0,104 | Valencia/València | 705 | 0,255 |
| Guadalajara | 78 | 0,273 | Valladolid | 68 | 0,129 |
| Huelva | 105 | 0,195 | Zamora | 14 | 0,085 |
| Huesca | 22 | 0,096 | Zaragoza | 212 | 0,212 |

### Farías (FARIAS)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Alicante/Alacant | 92 | 0,045 | Huesca | 5 | 0,022 |
| Almería | 22 | 0,029 | Jaén | 19 | 0,031 |
| Araba/Álava | 5 | 0,015 | León | 14 | 0,031 |
| Asturias | 46 | 0,045 | Lleida | 8 | 0,017 |
| Ávila | 7 | 0,044 | Lugo | 18 | 0,055 |
| Badajoz | 48 | 0,072 | Madrid | 505 | 0,071 |
| Balears, Illes | 90 | 0,072 | Málaga | 83 | 0,046 |
| Barcelona | 368 | 0,062 | Murcia | 58 | 0,037 |
| Bizkaia | 30 | 0,026 | Navarra | 16 | 0,023 |
| Burgos | 5 | 0,014 | ★ Ourense | 27 | 0,088 |
| Cáceres | 10 | 0,026 | Palencia | 6 | 0,038 |
| Cádiz | 17 | 0,013 | ★ Palmas, Las | 245 | 0,209 |
| Cantabria | 18 | 0,030 | Pontevedra | 44 | 0,046 |
| Castellón/Castelló | 15 | 0,024 | Rioja, La | . | . |
| Ciudad Real | 6 | 0,012 | Salamanca | 27 | 0,082 |
| Córdoba | 21 | 0,027 | ★ Santa Cruz de Tenerife | 105 | 0,097 |
| Coruña, A | 79 | 0,070 | Segovia | 10 | 0,063 |
| Cuenca | 13 | 0,065 | Sevilla | 36 | 0,018 |
| Gipuzkoa | 27 | 0,037 | Tarragona | 65 | 0,074 |
| Girona | 45 | 0,054 | Toledo | 24 | 0,032 |
| Granada | 32 | 0,034 | Valencia/València | 130 | 0,047 |
| Guadalajara | 10 | 0,035 | Valladolid | 11 | 0,021 |
| Huelva | 20 | 0,037 | Zaragoza | 17 | 0,017 |

### Cardozo (CARDOZO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 21 | 0,054 | Jaén | 14 | 0,023 |
| Alicante/Alacant | 174 | 0,086 | León | 13 | 0,029 |
| Almería | 40 | 0,052 | Lleida | 16 | 0,035 |
| Araba/Álava | 22 | 0,064 | Lugo | 10 | 0,031 |
| Asturias | 64 | 0,063 | ★ Madrid | 810 | 0,114 |
| Ávila | . | . | ★ Málaga | 193 | 0,108 |
| Badajoz | 17 | 0,026 | Murcia | 84 | 0,053 |
| ★ Balears, Illes | 163 | 0,130 | Navarra | 38 | 0,056 |
| Barcelona | 591 | 0,099 | Ourense | 7 | 0,023 |
| Bizkaia | 108 | 0,093 | Palencia | 8 | 0,050 |
| Burgos | 15 | 0,041 | Palmas, Las | 81 | 0,069 |
| Cáceres | 6 | 0,015 | Pontevedra | 41 | 0,043 |
| Cádiz | 16 | 0,013 | Rioja, La | 23 | 0,070 |
| Cantabria | 36 | 0,061 | Salamanca | 11 | 0,033 |
| Castellón/Castelló | 37 | 0,059 | Santa Cruz de Tenerife | 63 | 0,058 |
| Ciudad Real | 14 | 0,028 | Segovia | 7 | 0,044 |
| Córdoba | 10 | 0,013 | Sevilla | 51 | 0,026 |
| Coruña, A | 53 | 0,047 | Soria | 6 | 0,067 |
| Cuenca | 10 | 0,050 | Tarragona | 59 | 0,067 |
| Gipuzkoa | 14 | 0,019 | Teruel | 7 | 0,051 |
| Girona | 69 | 0,083 | Toledo | 36 | 0,048 |
| Granada | 25 | 0,026 | Valencia/València | 207 | 0,075 |
| Guadalajara | 13 | 0,045 | Valladolid | 19 | 0,036 |
| Huelva | 8 | 0,015 | Zaragoza | 20 | 0,020 |
| Huesca | 5 | 0,022 |  |  |  |

### Pereyra (PEREYRA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 16 | 0,041 | Guadalajara | 13 | 0,045 |
| Alicante/Alacant | 120 | 0,059 | Huesca | 6 | 0,026 |
| Almería | 52 | 0,067 | León | 6 | 0,013 |
| Araba/Álava | 9 | 0,026 | Lleida | 12 | 0,026 |
| Asturias | 25 | 0,025 | Lugo | 6 | 0,018 |
| ★ Balears, Illes | 183 | 0,146 | Madrid | 386 | 0,054 |
| Barcelona | 365 | 0,061 | Málaga | 105 | 0,059 |
| Bizkaia | 26 | 0,022 | Murcia | 44 | 0,028 |
| Burgos | . | . | Navarra | 30 | 0,044 |
| Cáceres | 5 | 0,013 | Ourense | 7 | 0,023 |
| Cádiz | 39 | 0,031 | Palmas, Las | 64 | 0,055 |
| Cantabria | 16 | 0,027 | Pontevedra | 38 | 0,040 |
| Castellón/Castelló | 23 | 0,037 | Rioja, La | 16 | 0,049 |
| Ciudad Real | 7 | 0,014 | ★ Santa Cruz de Tenerife | 127 | 0,117 |
| Córdoba | . | . | Sevilla | 83 | 0,042 |
| Coruña, A | 48 | 0,042 | Tarragona | 44 | 0,050 |
| Gipuzkoa | 25 | 0,034 | Toledo | 12 | 0,016 |
| ★ Girona | 63 | 0,076 | Valencia/València | 114 | 0,041 |
| Granada | 22 | 0,023 | Zaragoza | 18 | 0,018 |

### Romano (ROMANO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 9 | 0,023 | León | 9 | 0,020 |
| Alicante/Alacant | 98 | 0,048 | Lleida | 6 | 0,013 |
| Almería | 18 | 0,023 | Madrid | 600 | 0,084 |
| Araba/Álava | 37 | 0,108 | Málaga | 117 | 0,065 |
| Asturias | 162 | 0,160 | Murcia | 14 | 0,009 |
| Ávila | 11 | 0,068 | ★ Navarra | 204 | 0,298 |
| Badajoz | 179 | 0,269 | Ourense | 17 | 0,056 |
| Balears, Illes | 153 | 0,122 | Palencia | 8 | 0,050 |
| Barcelona | 547 | 0,092 | Palmas, Las | 286 | 0,244 |
| Bizkaia | 76 | 0,065 | Pontevedra | 40 | 0,042 |
| Burgos | 11 | 0,030 | Rioja, La | 47 | 0,144 |
| Cáceres | 21 | 0,054 | Salamanca | 10 | 0,030 |
| Cádiz | 253 | 0,201 | Santa Cruz de Tenerife | 74 | 0,068 |
| ★ Cantabria | 192 | 0,323 | ★ Segovia | 103 | 0,651 |
| Castellón/Castelló | 24 | 0,038 | Sevilla | 344 | 0,174 |
| Ciudad Real | 34 | 0,069 | Soria | 25 | 0,277 |
| Córdoba | 9 | 0,012 | Tarragona | 52 | 0,059 |
| Coruña, A | 106 | 0,093 | Teruel | 6 | 0,044 |
| Gipuzkoa | 63 | 0,086 | Toledo | 56 | 0,074 |
| Girona | 47 | 0,057 | Valencia/València | 94 | 0,034 |
| Granada | 38 | 0,040 | Valladolid | 15 | 0,028 |
| Guadalajara | 13 | 0,045 | Zamora | 6 | 0,036 |
| Huelva | 15 | 0,028 | Zaragoza | 101 | 0,101 |
| Huesca | . | . | Ceuta | 5 | 0,060 |
| Jaén | . | . | Melilla | 6 | 0,069 |

### Bianchi (BIANCHI)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Alicante/Alacant | 41 | 0,020 | Lleida | 8 | 0,017 |
| Almería | 8 | 0,010 | Lugo | 5 | 0,015 |
| Asturias | 6 | 0,006 | Madrid | 138 | 0,019 |
| ★ Balears, Illes | 65 | 0,052 | Málaga | 82 | 0,046 |
| Barcelona | 192 | 0,032 | Murcia | 10 | 0,006 |
| Bizkaia | 8 | 0,007 | Navarra | 9 | 0,013 |
| ★ Cádiz | 88 | 0,070 | Palmas, Las | 55 | 0,047 |
| Cantabria | 7 | 0,012 | Pontevedra | 24 | 0,025 |
| Castellón/Castelló | 9 | 0,014 | ★ Santa Cruz de Tenerife | 57 | 0,052 |
| Coruña, A | 11 | 0,010 | Sevilla | 20 | 0,010 |
| Gipuzkoa | 37 | 0,050 | Tarragona | 11 | 0,013 |
| Girona | 20 | 0,024 | Toledo | 6 | 0,008 |
| Granada | 16 | 0,017 | Valencia/València | 46 | 0,017 |

### Colombo (COLOMBO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Alicante/Alacant | 34 | 0,017 | Huelva | 7 | 0,013 |
| Almería | 7 | 0,009 | Huesca | 5 | 0,022 |
| Asturias | 11 | 0,011 | Lleida | 6 | 0,013 |
| Badajoz | 5 | 0,008 | Madrid | 162 | 0,023 |
| ★ Balears, Illes | 55 | 0,044 | Málaga | 51 | 0,028 |
| Barcelona | 176 | 0,030 | Murcia | 6 | 0,004 |
| Bizkaia | 5 | 0,004 | ★ Palmas, Las | 48 | 0,041 |
| ★ Cáceres | 49 | 0,126 | Pontevedra | 17 | 0,018 |
| Cádiz | 48 | 0,038 | Salamanca | . | . |
| Castellón/Castelló | 9 | 0,014 | Santa Cruz de Tenerife | 33 | 0,030 |
| Coruña, A | 11 | 0,010 | Sevilla | 14 | 0,007 |
| Gipuzkoa | 19 | 0,026 | Tarragona | 28 | 0,032 |
| Girona | 7 | 0,008 | Valencia/València | 61 | 0,022 |
| Granada | 23 | 0,024 | Zaragoza | 6 | 0,006 |

### Esposito (ESPOSITO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Alicante/Alacant | 63 | 0,031 | Girona | 9 | 0,011 |
| Almería | 6 | 0,008 | Granada | 11 | 0,012 |
| Asturias | 6 | 0,006 | Madrid | 108 | 0,015 |
| ★ Balears, Illes | 86 | 0,069 | ★ Málaga | 71 | 0,040 |
| Barcelona | 190 | 0,032 | Palmas, Las | 42 | 0,036 |
| Bizkaia | . | . | Pontevedra | 14 | 0,015 |
| Cádiz | 16 | 0,013 | ★ Santa Cruz de Tenerife | 106 | 0,097 |
| Cantabria | 5 | 0,008 | Sevilla | 24 | 0,012 |
| Coruña, A | 9 | 0,008 | Tarragona | 10 | 0,011 |
| Gipuzkoa | 5 | 0,007 | Valencia/València | 66 | 0,024 |

### Ferrari (FERRARI)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Alicante/Alacant | 57 | 0,028 | Guadalajara | 6 | 0,021 |
| Almería | 9 | 0,012 | Madrid | 274 | 0,039 |
| Asturias | 8 | 0,008 | Málaga | 80 | 0,045 |
| ★ Balears, Illes | 125 | 0,100 | Murcia | 30 | 0,019 |
| Barcelona | 285 | 0,048 | Navarra | 9 | 0,013 |
| Bizkaia | 10 | 0,009 | Palmas, Las | 69 | 0,059 |
| Burgos | 6 | 0,017 | Pontevedra | 30 | 0,032 |
| Cádiz | 44 | 0,035 | Rioja, La | 7 | 0,021 |
| Cantabria | 15 | 0,025 | ★ Santa Cruz de Tenerife | 75 | 0,069 |
| Castellón/Castelló | 29 | 0,046 | ★ Sevilla | 119 | 0,060 |
| Ciudad Real | 8 | 0,016 | Tarragona | 17 | 0,019 |
| Córdoba | 23 | 0,030 | Toledo | 8 | 0,011 |
| Coruña, A | 20 | 0,018 | Valencia/València | 82 | 0,030 |
| Gipuzkoa | 6 | 0,008 | Valladolid | 10 | 0,019 |
| Girona | 27 | 0,033 | Zaragoza | . | . |
| Granada | 9 | 0,010 |  |  |  |

### Ferreyra (FERREYRA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 6 | 0,015 | Huelva | 6 | 0,011 |
| Alicante/Alacant | 58 | 0,029 | Huesca | 6 | 0,026 |
| Almería | 12 | 0,016 | Madrid | 170 | 0,024 |
| Asturias | 16 | 0,016 | ★ Málaga | 88 | 0,049 |
| ★ Balears, Illes | 106 | 0,085 | Murcia | . | . |
| Barcelona | 182 | 0,031 | Navarra | . | . |
| Bizkaia | 8 | 0,007 | Ourense | 7 | 0,023 |
| Burgos | 10 | 0,028 | Palmas, Las | 25 | 0,021 |
| Cádiz | 17 | 0,013 | Pontevedra | 14 | 0,015 |
| Cantabria | 18 | 0,030 | Santa Cruz de Tenerife | 22 | 0,020 |
| Castellón/Castelló | 12 | 0,019 | Sevilla | 13 | 0,007 |
| Ciudad Real | 6 | 0,012 | ★ Soria | 7 | 0,078 |
| Coruña, A | 21 | 0,018 | Tarragona | 19 | 0,022 |
| Gipuzkoa | . | . | Toledo | 6 | 0,008 |
| Girona | 29 | 0,035 | Valencia/València | 74 | 0,027 |
| Granada | 14 | 0,015 | Zaragoza | 9 | 0,009 |

### Rossi (ROSSI)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 9 | 0,023 | Lleida | 23 | 0,050 |
| Alicante/Alacant | 107 | 0,053 | Lugo | 8 | 0,025 |
| Almería | 12 | 0,016 | Madrid | 394 | 0,055 |
| Asturias | 18 | 0,018 | Málaga | 144 | 0,080 |
| ★ Balears, Illes | 131 | 0,105 | Murcia | 17 | 0,011 |
| Barcelona | 437 | 0,073 | Navarra | 9 | 0,013 |
| Bizkaia | 17 | 0,015 | Ourense | . | . |
| Burgos | 5 | 0,014 | Palencia | 15 | 0,095 |
| ★ Cádiz | 201 | 0,159 | Palmas, Las | 118 | 0,101 |
| Cantabria | 14 | 0,024 | Pontevedra | 17 | 0,018 |
| Castellón/Castelló | 21 | 0,033 | Rioja, La | . | . |
| Ciudad Real | 14 | 0,028 | Salamanca | 7 | 0,021 |
| Córdoba | 74 | 0,096 | ★ Santa Cruz de Tenerife | 111 | 0,102 |
| Coruña, A | 14 | 0,012 | Segovia | 6 | 0,038 |
| Gipuzkoa | 19 | 0,026 | Sevilla | 55 | 0,028 |
| Girona | 32 | 0,039 | Tarragona | 33 | 0,038 |
| Granada | 29 | 0,031 | Toledo | 17 | 0,023 |
| Guadalajara | . | . | Valencia/València | 148 | 0,054 |
| Huelva | 21 | 0,039 | Zamora | . | . |
| Huesca | 5 | 0,022 | Zaragoza | 33 | 0,033 |
| León | 15 | 0,033 |  |  |  |

### Russo (RUSSO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Alicante/Alacant | 75 | 0,037 | Madrid | 234 | 0,033 |
| Almería | 8 | 0,010 | Málaga | 98 | 0,055 |
| Asturias | 13 | 0,013 | Murcia | 23 | 0,014 |
| Badajoz | 5 | 0,008 | Navarra | 5 | 0,007 |
| ★ Balears, Illes | 122 | 0,098 | ★ Palmas, Las | 90 | 0,077 |
| Barcelona | 265 | 0,044 | Pontevedra | 17 | 0,018 |
| Bizkaia | 17 | 0,015 | Rioja, La | . | . |
| Cádiz | 34 | 0,027 | Salamanca | . | . |
| Castellón/Castelló | 17 | 0,027 | ★ Santa Cruz de Tenerife | 154 | 0,142 |
| Coruña, A | 9 | 0,008 | Sevilla | 32 | 0,016 |
| Gipuzkoa | 5 | 0,007 | Tarragona | 32 | 0,037 |
| Girona | 11 | 0,013 | Toledo | 7 | 0,009 |
| Granada | 19 | 0,020 | Valencia/València | 115 | 0,042 |
| Huesca | 8 | 0,035 | Valladolid | 5 | 0,009 |
| Lugo | . | . | Zaragoza | 15 | 0,015 |

### Schmidt (SCHMIDT)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| ★ Alicante/Alacant | 135 | 0,066 | Huelva | 7 | 0,013 |
| Almería | 22 | 0,029 | Madrid | 130 | 0,018 |
| Asturias | 15 | 0,015 | Málaga | 94 | 0,052 |
| ★ Balears, Illes | 181 | 0,145 | Murcia | 36 | 0,023 |
| Barcelona | 231 | 0,039 | Navarra | 5 | 0,007 |
| Bizkaia | 9 | 0,008 | Palmas, Las | 77 | 0,066 |
| Cádiz | 31 | 0,025 | Pontevedra | 9 | 0,009 |
| Cantabria | 5 | 0,008 | Salamanca | 6 | 0,018 |
| Castellón/Castelló | 12 | 0,019 | ★ Santa Cruz de Tenerife | 148 | 0,136 |
| Coruña, A | 16 | 0,014 | Sevilla | 15 | 0,008 |
| Gipuzkoa | 8 | 0,011 | Tarragona | 34 | 0,039 |
| Girona | 33 | 0,040 | Valencia/València | 46 | 0,017 |
| Granada | 16 | 0,017 | Zaragoza | 7 | 0,007 |

### Acosta (ACOSTA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 110 | 0,282 | León | 112 | 0,250 |
| Alicante/Alacant | 732 | 0,360 | Lleida | 196 | 0,428 |
| Almería | 490 | 0,636 | Lugo | 64 | 0,196 |
| Araba/Álava | 177 | 0,518 | Madrid | 4.852 | 0,682 |
| Asturias | 255 | 0,251 | Málaga | 1.100 | 0,614 |
| Ávila | 73 | 0,454 | Murcia | 1.311 | 0,826 |
| Badajoz | 380 | 0,571 | Navarra | 269 | 0,393 |
| Balears, Illes | 790 | 0,632 | Ourense | 65 | 0,213 |
| Barcelona | 3.403 | 0,571 | Palencia | 74 | 0,466 |
| Bizkaia | 440 | 0,377 | ★ Palmas, Las | 3.414 | 2,914 |
| Burgos | 104 | 0,287 | Pontevedra | 285 | 0,301 |
| Cáceres | 313 | 0,806 | Rioja, La | 105 | 0,321 |
| Cádiz | 1.382 | 1,096 | Salamanca | 225 | 0,685 |
| Cantabria | 155 | 0,261 | ★ Santa Cruz de Tenerife | 6.325 | 5,817 |
| Castellón/Castelló | 173 | 0,276 | Segovia | 70 | 0,442 |
| Ciudad Real | 214 | 0,432 | Sevilla | 2.392 | 1,210 |
| Córdoba | 294 | 0,380 | Soria | 43 | 0,477 |
| Coruña, A | 338 | 0,298 | Tarragona | 403 | 0,460 |
| Cuenca | 35 | 0,175 | Teruel | 29 | 0,213 |
| Gipuzkoa | 347 | 0,473 | Toledo | 353 | 0,467 |
| Girona | 316 | 0,381 | Valencia/València | 984 | 0,356 |
| Granada | 543 | 0,574 | Valladolid | 157 | 0,297 |
| Guadalajara | 132 | 0,462 | Zamora | 51 | 0,308 |
| ★ Huelva | 957 | 1,776 | Zaragoza | 287 | 0,287 |
| Huesca | 62 | 0,269 | Ceuta | 22 | 0,263 |
| Jaén | 243 | 0,393 | Melilla | 10 | 0,115 |

### Aguirre (AGUIRRE)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 58 | 0,148 | León | 72 | 0,161 |
| Alicante/Alacant | 693 | 0,341 | Lleida | 85 | 0,185 |
| Almería | 306 | 0,397 | Lugo | 58 | 0,178 |
| ★ Araba/Álava | 898 | 2,626 | Madrid | 4.147 | 0,583 |
| Asturias | 412 | 0,406 | Málaga | 433 | 0,242 |
| Ávila | 43 | 0,268 | Murcia | 458 | 0,289 |
| Badajoz | 75 | 0,113 | Navarra | 1.570 | 2,296 |
| Balears, Illes | 420 | 0,336 | Ourense | 48 | 0,157 |
| Barcelona | 1.966 | 0,330 | Palencia | 30 | 0,189 |
| ★ Bizkaia | 2.921 | 2,502 | Palmas, Las | 244 | 0,208 |
| Burgos | 137 | 0,378 | Pontevedra | 148 | 0,156 |
| Cáceres | 43 | 0,111 | Rioja, La | 354 | 1,083 |
| Cádiz | 320 | 0,254 | Salamanca | 32 | 0,097 |
| Cantabria | 576 | 0,970 | Santa Cruz de Tenerife | 197 | 0,181 |
| Castellón/Castelló | 134 | 0,214 | Segovia | 50 | 0,316 |
| Ciudad Real | 229 | 0,463 | Sevilla | 378 | 0,191 |
| Córdoba | 109 | 0,141 | Soria | 35 | 0,388 |
| Coruña, A | 141 | 0,124 | Tarragona | 261 | 0,298 |
| Cuenca | 53 | 0,265 | Teruel | 63 | 0,463 |
| ★ Gipuzkoa | 2.512 | 3,426 | Toledo | 256 | 0,339 |
| Girona | 199 | 0,240 | Valencia/València | 844 | 0,305 |
| Granada | 192 | 0,203 | Valladolid | 100 | 0,189 |
| Guadalajara | 167 | 0,584 | Zamora | 35 | 0,211 |
| Huelva | 88 | 0,163 | Zaragoza | 381 | 0,382 |
| Huesca | 58 | 0,252 | Ceuta | 9 | 0,108 |
| Jaén | 146 | 0,236 | Melilla | 16 | 0,184 |

### Flores (FLORES)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 813 | 2,081 | León | 162 | 0,362 |
| Alicante/Alacant | 2.231 | 1,097 | Lleida | 350 | 0,764 |
| Almería | 1.846 | 2,396 | Lugo | 305 | 0,936 |
| Araba/Álava | 349 | 1,021 | Madrid | 13.838 | 1,945 |
| Asturias | 474 | 0,467 | Málaga | 2.955 | 1,650 |
| Ávila | 178 | 1,107 | Murcia | 2.221 | 1,400 |
| ★ Badajoz | 2.770 | 4,164 | Navarra | 782 | 1,144 |
| Balears, Illes | 1.402 | 1,122 | Ourense | 96 | 0,314 |
| Barcelona | 12.690 | 2,129 | Palencia | 123 | 0,775 |
| Bizkaia | 1.552 | 1,330 | Palmas, Las | 949 | 0,810 |
| Burgos | 232 | 0,640 | Pontevedra | 434 | 0,458 |
| ★ Cáceres | 1.264 | 3,256 | Rioja, La | 248 | 0,759 |
| Cádiz | 3.583 | 2,840 | Salamanca | 609 | 1,854 |
| Cantabria | 390 | 0,657 | Santa Cruz de Tenerife | 1.306 | 1,201 |
| Castellón/Castelló | 816 | 1,300 | Segovia | 89 | 0,562 |
| Ciudad Real | 1.263 | 2,552 | Sevilla | 5.107 | 2,582 |
| Córdoba | 2.261 | 2,924 | Soria | 122 | 1,353 |
| Coruña, A | 495 | 0,436 | Tarragona | 1.054 | 1,204 |
| Cuenca | 173 | 0,866 | Teruel | 69 | 0,507 |
| Gipuzkoa | 976 | 1,331 | Toledo | 1.510 | 2,000 |
| Girona | 1.471 | 1,771 | Valencia/València | 3.364 | 1,217 |
| Granada | 1.129 | 1,194 | Valladolid | 442 | 0,836 |
| Guadalajara | 451 | 1,578 | Zamora | 104 | 0,628 |
| ★ Huelva | 1.713 | 3,179 | Zaragoza | 977 | 0,979 |
| Huesca | 163 | 0,708 | Ceuta | 48 | 0,574 |
| Jaén | 1.697 | 2,745 | Melilla | 69 | 0,792 |

### Luna (LUNA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 47 | 0,120 | León | 228 | 0,509 |
| Alicante/Alacant | 794 | 0,390 | Lleida | 145 | 0,316 |
| Almería | 158 | 0,205 | Lugo | 95 | 0,291 |
| Araba/Álava | 73 | 0,213 | Madrid | 4.082 | 0,574 |
| Asturias | 254 | 0,250 | Málaga | 1.627 | 0,908 |
| Ávila | 34 | 0,212 | Murcia | 775 | 0,488 |
| Badajoz | 428 | 0,643 | Navarra | 239 | 0,349 |
| Balears, Illes | 544 | 0,435 | Ourense | 28 | 0,092 |
| Barcelona | 3.871 | 0,650 | Palencia | 29 | 0,183 |
| Bizkaia | 260 | 0,223 | Palmas, Las | 298 | 0,254 |
| Burgos | 45 | 0,124 | Pontevedra | 257 | 0,271 |
| Cáceres | 149 | 0,384 | Rioja, La | 43 | 0,132 |
| ★ Cádiz | 1.457 | 1,155 | Salamanca | 49 | 0,149 |
| Cantabria | 101 | 0,170 | Santa Cruz de Tenerife | 224 | 0,206 |
| Castellón/Castelló | 227 | 0,362 | Segovia | 32 | 0,202 |
| Ciudad Real | 465 | 0,940 | ★ Sevilla | 2.636 | 1,333 |
| ★ Córdoba | 2.843 | 3,677 | Soria | 12 | 0,133 |
| Coruña, A | 171 | 0,151 | Tarragona | 484 | 0,553 |
| Cuenca | 70 | 0,350 | Teruel | 74 | 0,544 |
| Gipuzkoa | 191 | 0,261 | Toledo | 375 | 0,497 |
| Girona | 358 | 0,431 | Valencia/València | 1.073 | 0,388 |
| Granada | 331 | 0,350 | Valladolid | 85 | 0,161 |
| Guadalajara | 156 | 0,546 | Zamora | 19 | 0,115 |
| Huelva | 348 | 0,646 | Zaragoza | 844 | 0,845 |
| Huesca | 169 | 0,735 | Ceuta | 23 | 0,275 |
| Jaén | 280 | 0,453 | Melilla | 38 | 0,436 |

### Maldonado (MALDONADO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 81 | 0,207 | León | 44 | 0,098 |
| Alicante/Alacant | 769 | 0,378 | Lleida | 157 | 0,343 |
| ★ Almería | 2.517 | 3,266 | Lugo | 27 | 0,083 |
| Araba/Álava | 99 | 0,290 | Madrid | 4.169 | 0,586 |
| Asturias | 192 | 0,189 | ★ Málaga | 2.350 | 1,312 |
| Ávila | 18 | 0,112 | Murcia | 643 | 0,405 |
| Badajoz | 453 | 0,681 | Navarra | 197 | 0,288 |
| Balears, Illes | 620 | 0,496 | Ourense | 37 | 0,121 |
| Barcelona | 3.498 | 0,587 | Palencia | 68 | 0,428 |
| Bizkaia | 334 | 0,286 | Palmas, Las | 241 | 0,206 |
| Burgos | 109 | 0,301 | Pontevedra | 68 | 0,072 |
| Cáceres | 126 | 0,325 | Rioja, La | 45 | 0,138 |
| Cádiz | 473 | 0,375 | Salamanca | 140 | 0,426 |
| Cantabria | 131 | 0,221 | Santa Cruz de Tenerife | 285 | 0,262 |
| Castellón/Castelló | 135 | 0,215 | Segovia | 23 | 0,145 |
| Ciudad Real | 390 | 0,788 | Sevilla | 1.600 | 0,809 |
| Córdoba | 434 | 0,561 | Soria | 20 | 0,222 |
| Coruña, A | 130 | 0,114 | Tarragona | 349 | 0,399 |
| Cuenca | 28 | 0,140 | Teruel | 37 | 0,272 |
| Gipuzkoa | 187 | 0,255 | Toledo | 385 | 0,510 |
| Girona | 315 | 0,379 | Valencia/València | 1.103 | 0,399 |
| ★ Granada | 3.323 | 3,513 | Valladolid | 190 | 0,359 |
| Guadalajara | 122 | 0,427 | Zamora | 32 | 0,193 |
| Huelva | 262 | 0,486 | Zaragoza | 323 | 0,324 |
| Huesca | 47 | 0,204 | Ceuta | 32 | 0,383 |
| Jaén | 386 | 0,624 | Melilla | 25 | 0,287 |

### Mendoza (MENDOZA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 234 | 0,599 | León | 282 | 0,629 |
| Alicante/Alacant | 1.152 | 0,566 | Lleida | 228 | 0,498 |
| Almería | 270 | 0,350 | Lugo | 172 | 0,528 |
| Araba/Álava | 384 | 1,123 | Madrid | 8.574 | 1,205 |
| Asturias | 395 | 0,389 | Málaga | 1.254 | 0,700 |
| ★ Ávila | 317 | 1,972 | Murcia | 1.825 | 1,150 |
| Badajoz | 952 | 1,431 | Navarra | 714 | 1,044 |
| Balears, Illes | 1.051 | 0,841 | Ourense | 86 | 0,282 |
| Barcelona | 5.670 | 0,951 | Palencia | 73 | 0,460 |
| Bizkaia | 822 | 0,704 | ★ Palmas, Las | 3.846 | 3,283 |
| Burgos | 244 | 0,673 | Pontevedra | 317 | 0,334 |
| Cáceres | 282 | 0,726 | Rioja, La | 569 | 1,741 |
| Cádiz | 1.374 | 1,089 | Salamanca | 145 | 0,441 |
| Cantabria | 286 | 0,482 | ★ Santa Cruz de Tenerife | 2.723 | 2,504 |
| Castellón/Castelló | 417 | 0,664 | Segovia | 140 | 0,885 |
| Ciudad Real | 512 | 1,035 | Sevilla | 2.097 | 1,060 |
| Córdoba | 701 | 0,907 | Soria | 49 | 0,543 |
| Coruña, A | 367 | 0,323 | Tarragona | 658 | 0,752 |
| Cuenca | 103 | 0,515 | Teruel | 57 | 0,419 |
| Gipuzkoa | 535 | 0,730 | Toledo | 925 | 1,225 |
| Girona | 582 | 0,701 | Valencia/València | 1.935 | 0,700 |
| Granada | 648 | 0,685 | Valladolid | 496 | 0,938 |
| Guadalajara | 204 | 0,714 | Zamora | 41 | 0,248 |
| Huelva | 749 | 1,390 | Zaragoza | 953 | 0,954 |
| Huesca | 169 | 0,735 | Ceuta | 42 | 0,503 |
| Jaén | 703 | 1,137 | Melilla | 18 | 0,207 |

### Miranda (MIRANDA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 190 | 0,486 | León | 346 | 0,772 |
| Alicante/Alacant | 579 | 0,285 | Lleida | 241 | 0,526 |
| Almería | 400 | 0,519 | Lugo | 240 | 0,736 |
| Araba/Álava | 207 | 0,605 | Madrid | 5.100 | 0,717 |
| Asturias | 1.566 | 1,543 | Málaga | 1.423 | 0,794 |
| Ávila | 123 | 0,765 | Murcia | 514 | 0,324 |
| ★ Badajoz | 1.174 | 1,765 | Navarra | 625 | 0,914 |
| Balears, Illes | 769 | 0,615 | Ourense | 261 | 0,855 |
| Barcelona | 4.002 | 0,671 | Palencia | 71 | 0,447 |
| Bizkaia | 882 | 0,756 | ★ Palmas, Las | 2.251 | 1,921 |
| Burgos | 305 | 0,841 | Pontevedra | 930 | 0,981 |
| Cáceres | 367 | 0,945 | Rioja, La | 409 | 1,252 |
| Cádiz | 853 | 0,676 | Salamanca | 125 | 0,381 |
| Cantabria | 279 | 0,470 | Santa Cruz de Tenerife | 1.265 | 1,163 |
| Castellón/Castelló | 178 | 0,284 | Segovia | 136 | 0,859 |
| Ciudad Real | 94 | 0,190 | Sevilla | 2.046 | 1,035 |
| Córdoba | 827 | 1,070 | ★ Soria | 142 | 1,575 |
| Coruña, A | 985 | 0,867 | Tarragona | 429 | 0,490 |
| Cuenca | 45 | 0,225 | Teruel | 32 | 0,235 |
| Gipuzkoa | 589 | 0,803 | Toledo | 385 | 0,510 |
| Girona | 359 | 0,432 | Valencia/València | 853 | 0,309 |
| Granada | 582 | 0,615 | Valladolid | 306 | 0,579 |
| Guadalajara | 139 | 0,486 | Zamora | 199 | 1,202 |
| Huelva | 222 | 0,412 | Zaragoza | 775 | 0,776 |
| Huesca | 274 | 1,191 | Ceuta | 36 | 0,431 |
| Jaén | 577 | 0,933 | Melilla | 19 | 0,218 |

### Ojeda (OJEDA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 146 | 0,374 | León | 40 | 0,089 |
| Alicante/Alacant | 330 | 0,162 | Lleida | 158 | 0,345 |
| Almería | 481 | 0,624 | Lugo | 25 | 0,077 |
| Araba/Álava | 47 | 0,137 | Madrid | 2.123 | 0,298 |
| Asturias | 244 | 0,240 | Málaga | 742 | 0,414 |
| Ávila | 7 | 0,044 | Murcia | 213 | 0,134 |
| Badajoz | 126 | 0,189 | Navarra | 86 | 0,126 |
| Balears, Illes | 430 | 0,344 | Ourense | 21 | 0,069 |
| Barcelona | 1.685 | 0,283 | Palencia | 15 | 0,095 |
| Bizkaia | 282 | 0,242 | ★ Palmas, Las | 5.510 | 4,703 |
| Burgos | 174 | 0,480 | Pontevedra | 84 | 0,089 |
| Cáceres | 34 | 0,088 | Rioja, La | 265 | 0,811 |
| Cádiz | 800 | 0,634 | Salamanca | 29 | 0,088 |
| Cantabria | 131 | 0,221 | Santa Cruz de Tenerife | 475 | 0,437 |
| Castellón/Castelló | 291 | 0,464 | Segovia | 21 | 0,133 |
| Ciudad Real | 117 | 0,236 | ★ Sevilla | 2.372 | 1,199 |
| Córdoba | 375 | 0,485 | Soria | 8 | 0,089 |
| Coruña, A | 67 | 0,059 | Tarragona | 165 | 0,188 |
| Cuenca | 87 | 0,435 | Teruel | 9 | 0,066 |
| Gipuzkoa | 128 | 0,175 | Toledo | 113 | 0,150 |
| Girona | 174 | 0,210 | Valencia/València | 702 | 0,254 |
| Granada | 208 | 0,220 | Valladolid | 93 | 0,176 |
| Guadalajara | 51 | 0,178 | Zamora | . | . |
| ★ Huelva | 696 | 1,292 | Zaragoza | 153 | 0,153 |
| Huesca | 46 | 0,200 | Ceuta | 17 | 0,203 |
| Jaén | 420 | 0,679 | Melilla | 13 | 0,149 |

### Paz (PAZ)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 49 | 0,125 | León | 158 | 0,353 |
| Alicante/Alacant | 325 | 0,160 | Lleida | 48 | 0,105 |
| Almería | 107 | 0,139 | ★ Lugo | 972 | 2,981 |
| Araba/Álava | 84 | 0,246 | Madrid | 3.035 | 0,427 |
| Asturias | 242 | 0,238 | Málaga | 657 | 0,367 |
| Ávila | 83 | 0,516 | Murcia | 213 | 0,134 |
| Badajoz | 210 | 0,316 | Navarra | 201 | 0,294 |
| Balears, Illes | 243 | 0,194 | Ourense | 692 | 2,267 |
| Barcelona | 1.936 | 0,325 | Palencia | 25 | 0,158 |
| Bizkaia | 415 | 0,356 | Palmas, Las | 447 | 0,382 |
| Burgos | 60 | 0,165 | ★ Pontevedra | 2.573 | 2,715 |
| Cáceres | 258 | 0,665 | Rioja, La | 58 | 0,177 |
| Cádiz | 311 | 0,247 | Salamanca | 120 | 0,365 |
| Cantabria | 216 | 0,364 | Santa Cruz de Tenerife | 879 | 0,808 |
| Castellón/Castelló | 114 | 0,182 | Segovia | 18 | 0,114 |
| Ciudad Real | 314 | 0,635 | Sevilla | 556 | 0,281 |
| Córdoba | 179 | 0,232 | Soria | 24 | 0,266 |
| ★ Coruña, A | 3.539 | 3,116 | Tarragona | 225 | 0,257 |
| Cuenca | 26 | 0,130 | Teruel | 25 | 0,184 |
| Gipuzkoa | 250 | 0,341 | Toledo | 251 | 0,332 |
| Girona | 288 | 0,347 | Valencia/València | 626 | 0,226 |
| Granada | 79 | 0,084 | Valladolid | 157 | 0,297 |
| Guadalajara | 70 | 0,245 | Zamora | 56 | 0,338 |
| Huelva | 88 | 0,163 | Zaragoza | 256 | 0,256 |
| Huesca | 46 | 0,200 | Ceuta | 34 | 0,407 |
| Jaén | 76 | 0,123 | Melilla | 14 | 0,161 |

### Ponce (PONCE)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 294 | 0,752 | León | 45 | 0,100 |
| Alicante/Alacant | 911 | 0,448 | Lleida | 79 | 0,172 |
| Almería | 323 | 0,419 | Lugo | 20 | 0,061 |
| Araba/Álava | 80 | 0,234 | Madrid | 3.017 | 0,424 |
| Asturias | 134 | 0,132 | Málaga | 1.721 | 0,961 |
| Ávila | 26 | 0,162 | Murcia | 1.442 | 0,909 |
| Badajoz | 518 | 0,779 | Navarra | 130 | 0,190 |
| Balears, Illes | 503 | 0,402 | Ourense | 23 | 0,075 |
| Barcelona | 3.030 | 0,508 | Palencia | 14 | 0,088 |
| Bizkaia | 287 | 0,246 | Palmas, Las | 1.002 | 0,855 |
| Burgos | 60 | 0,165 | Pontevedra | 65 | 0,069 |
| Cáceres | 37 | 0,095 | Rioja, La | 26 | 0,080 |
| Cádiz | 1.571 | 1,245 | Salamanca | 62 | 0,189 |
| Cantabria | 112 | 0,189 | Santa Cruz de Tenerife | 231 | 0,212 |
| Castellón/Castelló | 157 | 0,250 | Segovia | 42 | 0,265 |
| Ciudad Real | 306 | 0,618 | ★ Sevilla | 2.705 | 1,368 |
| Córdoba | 181 | 0,234 | Soria | 19 | 0,211 |
| Coruña, A | 271 | 0,239 | Tarragona | 363 | 0,415 |
| ★ Cuenca | 333 | 1,666 | Teruel | 11 | 0,081 |
| Gipuzkoa | 242 | 0,330 | Toledo | 165 | 0,219 |
| Girona | 362 | 0,436 | Valencia/València | 2.149 | 0,777 |
| Granada | 171 | 0,181 | Valladolid | 63 | 0,119 |
| Guadalajara | 100 | 0,350 | Zamora | 46 | 0,278 |
| ★ Huelva | 1.560 | 2,895 | Zaragoza | 198 | 0,198 |
| Huesca | 41 | 0,178 | Ceuta | 45 | 0,538 |
| Jaén | 180 | 0,291 | Melilla | 19 | 0,218 |

### Rivero (RIVERO)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 60 | 0,154 | León | 250 | 0,558 |
| Alicante/Alacant | 456 | 0,224 | Lleida | 82 | 0,179 |
| Almería | 90 | 0,117 | Lugo | 151 | 0,463 |
| Araba/Álava | 104 | 0,304 | Madrid | 4.023 | 0,566 |
| Asturias | 892 | 0,879 | Málaga | 1.140 | 0,636 |
| Ávila | 97 | 0,603 | Murcia | 295 | 0,186 |
| Badajoz | 822 | 1,236 | Navarra | 197 | 0,288 |
| Balears, Illes | 399 | 0,319 | ★ Ourense | 614 | 2,011 |
| Barcelona | 2.250 | 0,378 | Palencia | 46 | 0,290 |
| Bizkaia | 531 | 0,455 | ★ Palmas, Las | 5.699 | 4,865 |
| Burgos | 72 | 0,199 | Pontevedra | 555 | 0,586 |
| Cáceres | 508 | 1,309 | Rioja, La | 96 | 0,294 |
| Cádiz | 1.173 | 0,930 | Salamanca | 324 | 0,986 |
| Cantabria | 780 | 1,314 | ★ Santa Cruz de Tenerife | 3.110 | 2,860 |
| Castellón/Castelló | 115 | 0,183 | Segovia | 57 | 0,360 |
| Ciudad Real | 466 | 0,942 | Sevilla | 2.612 | 1,321 |
| Córdoba | 421 | 0,545 | Soria | 12 | 0,133 |
| Coruña, A | 354 | 0,312 | Tarragona | 273 | 0,312 |
| Cuenca | 32 | 0,160 | Teruel | 47 | 0,345 |
| Gipuzkoa | 368 | 0,502 | Toledo | 343 | 0,454 |
| Girona | 223 | 0,269 | Valencia/València | 717 | 0,259 |
| Granada | 210 | 0,222 | Valladolid | 332 | 0,628 |
| Guadalajara | 125 | 0,437 | Zamora | 71 | 0,429 |
| Huelva | 583 | 1,082 | Zaragoza | 240 | 0,240 |
| Huesca | 52 | 0,226 | Ceuta | 44 | 0,527 |
| Jaén | 144 | 0,233 | Melilla | 12 | 0,138 |

### Rojas (ROJAS)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 272 | 0,696 | León | 183 | 0,408 |
| Alicante/Alacant | 1.689 | 0,831 | Lleida | 287 | 0,626 |
| Almería | 750 | 0,973 | Lugo | 168 | 0,515 |
| Araba/Álava | 324 | 0,947 | Madrid | 11.334 | 1,593 |
| Asturias | 511 | 0,503 | Málaga | 3.750 | 2,094 |
| Ávila | 93 | 0,579 | Murcia | 1.511 | 0,952 |
| Badajoz | 487 | 0,732 | Navarra | 569 | 0,832 |
| Balears, Illes | 1.497 | 1,198 | Ourense | 214 | 0,701 |
| Barcelona | 7.751 | 1,301 | Palencia | 100 | 0,630 |
| Bizkaia | 1.035 | 0,887 | Palmas, Las | 1.453 | 1,240 |
| Burgos | 468 | 1,290 | Pontevedra | 386 | 0,407 |
| Cáceres | 146 | 0,376 | Rioja, La | 370 | 1,132 |
| ★ Cádiz | 3.010 | 2,386 | Salamanca | 176 | 0,536 |
| Cantabria | 460 | 0,775 | Santa Cruz de Tenerife | 1.964 | 1,806 |
| Castellón/Castelló | 444 | 0,707 | Segovia | 94 | 0,594 |
| Ciudad Real | 708 | 1,431 | Sevilla | 3.846 | 1,945 |
| ★ Córdoba | 1.748 | 2,261 | Soria | 85 | 0,943 |
| Coruña, A | 562 | 0,495 | Tarragona | 751 | 0,858 |
| Cuenca | 112 | 0,560 | Teruel | 80 | 0,588 |
| Gipuzkoa | 412 | 0,562 | ★ Toledo | 1.630 | 2,159 |
| Girona | 796 | 0,959 | Valencia/València | 2.451 | 0,887 |
| Granada | 1.598 | 1,690 | Valladolid | 262 | 0,496 |
| Guadalajara | 385 | 1,347 | Zamora | 63 | 0,381 |
| Huelva | 718 | 1,333 | Zaragoza | 691 | 0,692 |
| Huesca | 116 | 0,504 | Ceuta | 67 | 0,802 |
| Jaén | 669 | 1,082 | Melilla | 52 | 0,597 |

### Roldán (ROLDAN)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 787 | 2,014 | León | 127 | 0,283 |
| Alicante/Alacant | 782 | 0,385 | Lleida | 82 | 0,179 |
| Almería | 159 | 0,206 | Lugo | 27 | 0,083 |
| Araba/Álava | 111 | 0,325 | Madrid | 5.000 | 0,703 |
| Asturias | 235 | 0,231 | Málaga | 1.917 | 1,070 |
| Ávila | 56 | 0,348 | Murcia | 450 | 0,284 |
| Badajoz | 178 | 0,268 | Navarra | 466 | 0,681 |
| Balears, Illes | 696 | 0,557 | Ourense | 25 | 0,082 |
| Barcelona | 3.815 | 0,640 | Palencia | 210 | 1,323 |
| Bizkaia | 360 | 0,308 | Palmas, Las | 227 | 0,194 |
| Burgos | 99 | 0,273 | Pontevedra | 90 | 0,095 |
| Cáceres | 78 | 0,201 | Rioja, La | 215 | 0,658 |
| Cádiz | 1.814 | 1,438 | Salamanca | 65 | 0,198 |
| Cantabria | 296 | 0,499 | Santa Cruz de Tenerife | 185 | 0,170 |
| Castellón/Castelló | 302 | 0,481 | Segovia | 141 | 0,891 |
| Ciudad Real | 356 | 0,719 | ★ Sevilla | 4.410 | 2,230 |
| ★ Córdoba | 3.165 | 4,094 | Soria | 21 | 0,233 |
| Coruña, A | 86 | 0,076 | Tarragona | 480 | 0,548 |
| Cuenca | 198 | 0,991 | Teruel | 47 | 0,345 |
| Gipuzkoa | 167 | 0,228 | Toledo | 522 | 0,691 |
| Girona | 245 | 0,295 | Valencia/València | 1.132 | 0,410 |
| ★ Granada | 1.994 | 2,108 | Valladolid | 164 | 0,310 |
| Guadalajara | 142 | 0,497 | Zamora | 56 | 0,338 |
| Huelva | 489 | 0,908 | Zaragoza | 444 | 0,445 |
| Huesca | 94 | 0,409 | Ceuta | 65 | 0,778 |
| Jaén | 548 | 0,887 | Melilla | 72 | 0,827 |

### Ríos (RIOS)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 245 | 0,627 | León | 275 | 0,614 |
| Alicante/Alacant | 1.413 | 0,695 | Lleida | 197 | 0,430 |
| Almería | 360 | 0,467 | Lugo | 241 | 0,739 |
| Araba/Álava | 230 | 0,673 | Madrid | 5.230 | 0,735 |
| Asturias | 528 | 0,520 | ★ Málaga | 3.868 | 2,159 |
| Ávila | 152 | 0,946 | Murcia | 1.968 | 1,240 |
| Badajoz | 392 | 0,589 | Navarra | 387 | 0,566 |
| Balears, Illes | 1.011 | 0,809 | Ourense | 184 | 0,603 |
| Barcelona | 4.604 | 0,772 | Palencia | 104 | 0,655 |
| Bizkaia | 1.011 | 0,866 | Palmas, Las | 795 | 0,679 |
| Burgos | 154 | 0,425 | Pontevedra | 1.560 | 1,646 |
| Cáceres | 207 | 0,533 | Rioja, La | 205 | 0,627 |
| ★ Cádiz | 2.832 | 2,245 | Salamanca | 169 | 0,515 |
| Cantabria | 754 | 1,270 | Santa Cruz de Tenerife | 577 | 0,531 |
| Castellón/Castelló | 424 | 0,676 | Segovia | 64 | 0,404 |
| Ciudad Real | 296 | 0,598 | Sevilla | 3.096 | 1,565 |
| Córdoba | 914 | 1,182 | Soria | 19 | 0,211 |
| Coruña, A | 2.241 | 1,973 | Tarragona | 557 | 0,636 |
| Cuenca | 30 | 0,150 | Teruel | 93 | 0,683 |
| Gipuzkoa | 353 | 0,481 | Toledo | 470 | 0,622 |
| Girona | 372 | 0,448 | Valencia/València | 1.817 | 0,657 |
| Granada | 912 | 0,964 | Valladolid | 325 | 0,615 |
| Guadalajara | 140 | 0,490 | Zamora | 186 | 1,123 |
| Huelva | 589 | 1,093 | Zaragoza | 661 | 0,662 |
| Huesca | 193 | 0,839 | ★ Ceuta | 188 | 2,250 |
| Jaén | 451 | 0,730 | Melilla | 43 | 0,494 |

### Silva (SILVA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 66 | 0,169 | León | 495 | 1,105 |
| Alicante/Alacant | 1.124 | 0,553 | Lleida | 280 | 0,611 |
| Almería | 298 | 0,387 | Lugo | 417 | 1,279 |
| Araba/Álava | 247 | 0,722 | Madrid | 8.775 | 1,234 |
| Asturias | 844 | 0,831 | Málaga | 1.663 | 0,928 |
| Ávila | 58 | 0,361 | Murcia | 573 | 0,361 |
| ★ Badajoz | 2.280 | 3,428 | Navarra | 433 | 0,633 |
| Balears, Illes | 1.138 | 0,911 | ★ Ourense | 774 | 2,535 |
| Barcelona | 5.113 | 0,858 | Palencia | 91 | 0,573 |
| Bizkaia | 1.027 | 0,880 | Palmas, Las | 1.267 | 1,081 |
| Burgos | 237 | 0,653 | ★ Pontevedra | 3.451 | 3,641 |
| Cáceres | 893 | 2,300 | Rioja, La | 220 | 0,673 |
| Cádiz | 1.679 | 1,331 | Salamanca | 265 | 0,807 |
| Cantabria | 372 | 0,627 | Santa Cruz de Tenerife | 773 | 0,711 |
| Castellón/Castelló | 308 | 0,491 | Segovia | 48 | 0,303 |
| Ciudad Real | 214 | 0,432 | Sevilla | 3.372 | 1,705 |
| Córdoba | 391 | 0,506 | Soria | 47 | 0,521 |
| Coruña, A | 2.576 | 2,268 | Tarragona | 635 | 0,725 |
| Cuenca | 61 | 0,305 | Teruel | 43 | 0,316 |
| Gipuzkoa | 510 | 0,696 | Toledo | 677 | 0,897 |
| Girona | 749 | 0,902 | Valencia/València | 1.652 | 0,598 |
| Granada | 219 | 0,232 | Valladolid | 384 | 0,726 |
| Guadalajara | 198 | 0,693 | Zamora | 204 | 1,232 |
| Huelva | 1.032 | 1,915 | Zaragoza | 537 | 0,538 |
| Huesca | 64 | 0,278 | Ceuta | 60 | 0,718 |
| Jaén | 106 | 0,171 | Melilla | 28 | 0,322 |

### Sosa (SOSA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 35 | 0,090 | León | 48 | 0,107 |
| Alicante/Alacant | 389 | 0,191 | Lleida | 61 | 0,133 |
| Almería | 102 | 0,132 | Lugo | 39 | 0,120 |
| Araba/Álava | 49 | 0,143 | Madrid | 2.446 | 0,344 |
| Asturias | 193 | 0,190 | Málaga | 530 | 0,296 |
| Ávila | 18 | 0,112 | Murcia | 295 | 0,186 |
| ★ Badajoz | 822 | 1,236 | Navarra | 104 | 0,152 |
| Balears, Illes | 476 | 0,381 | Ourense | 35 | 0,115 |
| Barcelona | 1.858 | 0,312 | Palencia | 10 | 0,063 |
| Bizkaia | 216 | 0,185 | ★ Palmas, Las | 7.059 | 6,025 |
| Burgos | 29 | 0,080 | Pontevedra | 102 | 0,108 |
| Cáceres | 74 | 0,191 | Rioja, La | 28 | 0,086 |
| Cádiz | 563 | 0,446 | Salamanca | 44 | 0,134 |
| Cantabria | 88 | 0,148 | ★ Santa Cruz de Tenerife | 1.816 | 1,670 |
| Castellón/Castelló | 107 | 0,170 | Segovia | 33 | 0,209 |
| Ciudad Real | 155 | 0,313 | Sevilla | 1.583 | 0,800 |
| Córdoba | 144 | 0,186 | Soria | 15 | 0,166 |
| Coruña, A | 182 | 0,160 | Tarragona | 233 | 0,266 |
| Cuenca | 14 | 0,070 | Teruel | 8 | 0,059 |
| Gipuzkoa | 99 | 0,135 | Toledo | 191 | 0,253 |
| Girona | 266 | 0,320 | Valencia/València | 590 | 0,213 |
| Granada | 82 | 0,087 | Valladolid | 71 | 0,134 |
| Guadalajara | 71 | 0,248 | Zamora | 18 | 0,109 |
| Huelva | 415 | 0,770 | Zaragoza | 145 | 0,145 |
| Huesca | 18 | 0,078 | Ceuta | 17 | 0,203 |
| Jaén | 41 | 0,066 | Melilla | 5 | 0,057 |

### Vargas (VARGAS)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 360 | 0,921 | León | 588 | 1,312 |
| Alicante/Alacant | 1.836 | 0,903 | Lleida | 295 | 0,644 |
| ★ Almería | 2.905 | 3,770 | Lugo | 167 | 0,512 |
| Araba/Álava | 270 | 0,790 | Madrid | 10.598 | 1,490 |
| Asturias | 686 | 0,676 | Málaga | 3.433 | 1,917 |
| Ávila | 68 | 0,423 | Murcia | 1.145 | 0,721 |
| Badajoz | 1.549 | 2,329 | Navarra | 432 | 0,632 |
| Balears, Illes | 1.822 | 1,458 | Ourense | 105 | 0,344 |
| Barcelona | 7.726 | 1,296 | Palencia | 170 | 1,071 |
| Bizkaia | 923 | 0,791 | Palmas, Las | 965 | 0,824 |
| Burgos | 240 | 0,662 | Pontevedra | 291 | 0,307 |
| ★ Cáceres | 1.116 | 2,875 | Rioja, La | 321 | 0,982 |
| Cádiz | 2.839 | 2,251 | Salamanca | 116 | 0,353 |
| Cantabria | 673 | 1,134 | Santa Cruz de Tenerife | 1.793 | 1,649 |
| Castellón/Castelló | 716 | 1,141 | Segovia | 86 | 0,543 |
| Ciudad Real | 487 | 0,984 | ★ Sevilla | 5.507 | 2,785 |
| Córdoba | 986 | 1,275 | Soria | 118 | 1,308 |
| Coruña, A | 519 | 0,457 | Tarragona | 770 | 0,879 |
| Cuenca | 118 | 0,590 | Teruel | 54 | 0,397 |
| Gipuzkoa | 418 | 0,570 | Toledo | 933 | 1,236 |
| Girona | 791 | 0,953 | Valencia/València | 2.992 | 1,082 |
| Granada | 2.147 | 2,270 | Valladolid | 352 | 0,666 |
| Guadalajara | 306 | 1,071 | Zamora | 73 | 0,441 |
| Huelva | 1.137 | 2,110 | Zaragoza | 665 | 0,666 |
| Huesca | 180 | 0,782 | Ceuta | 41 | 0,491 |
| Jaén | 1.012 | 1,637 | Melilla | 81 | 0,930 |

### Vera (VERA)

| Provincia | Personas | ‰ | Provincia | Personas | ‰ |
|---|---|---|---|---|---|
| Albacete | 278 | 0,711 | León | 71 | 0,158 |
| Alicante/Alacant | 2.530 | 1,244 | Lleida | 189 | 0,412 |
| Almería | 327 | 0,424 | Lugo | 40 | 0,123 |
| Araba/Álava | 162 | 0,474 | Madrid | 5.502 | 0,773 |
| Asturias | 238 | 0,234 | Málaga | 3.077 | 1,718 |
| Ávila | 32 | 0,199 | ★ Murcia | 4.093 | 2,579 |
| Badajoz | 635 | 0,955 | Navarra | 494 | 0,722 |
| Balears, Illes | 1.236 | 0,989 | Ourense | 28 | 0,092 |
| Barcelona | 5.427 | 0,911 | Palencia | 33 | 0,208 |
| Bizkaia | 378 | 0,324 | ★ Palmas, Las | 2.514 | 2,146 |
| Burgos | 79 | 0,218 | Pontevedra | 160 | 0,169 |
| Cáceres | 89 | 0,229 | Rioja, La | 139 | 0,425 |
| Cádiz | 1.498 | 1,188 | Salamanca | 107 | 0,326 |
| Cantabria | 107 | 0,180 | ★ Santa Cruz de Tenerife | 2.600 | 2,391 |
| Castellón/Castelló | 340 | 0,542 | Segovia | 78 | 0,493 |
| Ciudad Real | 435 | 0,879 | Sevilla | 2.806 | 1,419 |
| Córdoba | 610 | 0,789 | Soria | 143 | 1,586 |
| Coruña, A | 171 | 0,151 | Tarragona | 539 | 0,616 |
| Cuenca | 158 | 0,791 | Teruel | 55 | 0,404 |
| Gipuzkoa | 162 | 0,221 | Toledo | 432 | 0,572 |
| Girona | 445 | 0,536 | Valencia/València | 1.585 | 0,573 |
| Granada | 837 | 0,885 | Valladolid | 114 | 0,216 |
| Guadalajara | 190 | 0,665 | Zamora | 23 | 0,139 |
| Huelva | 347 | 0,644 | Zaragoza | 942 | 0,943 |
| Huesca | 179 | 0,778 | Ceuta | 64 | 0,766 |
| Jaén | 502 | 0,812 | Melilla | 35 | 0,402 |

