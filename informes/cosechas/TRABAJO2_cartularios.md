# TRABAJO 2 · Cartularios medievales: qué hay en digital y qué se puede bajar

Fecha de las comprobaciones: 27/09/2026. «Abierta y leída» = página bajada con script y leída. **[RESUMIDOR]** = dato que solo viene del resumen de un buscador: no está verificado y no se puede imprimir.

## PASO A · Reconocimiento

| Corpus | ¿Edición digital abierta? | Institución / edición | ¿Texto descargable entero? | robots.txt | Estado de la verificación |
|---|---|---|---|---|---|
| **Colección diplomática de Sahagún** | **No encontrada** | Mínguez Fernández y otros, Centro de Estudios e Investigación «San Isidoro», col. *Fuentes y Estudios de Historia Leonesa*, varios volúmenes (vol. de siglos IX-X: 1976, n.º 17 de la colección, 505 págs.) | No | bibliocele.es: `Allow: /`, `Crawl-delay: 3` | La ficha de bibliocele.es (Bibliografía de Estudios Leoneses) fue abierta y leída: es un registro bibliográfico **sin texto**. En la búsqueda no apareció ninguna copia digital abierta. **Busqué y no encontré; no comprobé que no exista** |
| **Becerro Gótico de Valpuesta** | Solo un **facsímil del manuscrito** | archive.org, ítem `becerro-gotico-de-santa-maria-de-valpuesta`, subido por un usuario particular (no por una institución), marcado «Public Domain Mark 1.0» | Hay un PDF de imágenes (33,6 MB) y un OCR automático (tesseract). **El OCR es ilegible** (letra visigótica): no sirve para buscar | archive.org: solo prohíbe /control/ y /report/ | Metadatos y OCR abiertos y leídos: primeras líneas del OCR: «po A Enfení ¿ugicuas A / ¿dnde lc: ce…». **No es una edición** |
| **Becerros Gótico y Galicano de Valpuesta (edición)** | No encontrada abierta | Ruiz Asencio, Ruiz Albi y Herrero Jiménez, Instituto Castellano y Leonés de la Lengua / RAE, 2010, 2 vols. [RESUMIDOR] | No encontrado | — | Datos de edición solo del resumen del buscador **[RESUMIDOR]** |
| **Becerro Galicano de Valpuesta (manuscrito)** | ¿Imágenes en PARES? | Archivo Histórico Nacional, CODICES, L.1167 (según el título del resultado de búsqueda) | — | pares.mcu.es: sin robots.txt (404) | **No se pudo abrir**: error de certificado TLS en pares.mcu.es. No lo rodeé |
| **Otero de las Dueñas** | **No encontrada** | Fernández Flórez y Herrero de la Fuente, Centro «San Isidoro», vol. I (854-1108) 1999, vol. II 2005 [RESUMIDOR] | No | — | Solo aparecieron fichas de libro impreso (Dialnet, una librería). **Busqué y no encontré** |
| **San Pedro de Cardeña** | **No encontrada** | Martínez Díez, *Colección documental del monasterio de San Pedro de Cardeña*, Burgos, 1998; 382 documentos de 899-1085, clasificados como auténticos, falsos o dudosos [RESUMIDOR] | No | — | Solo fichas bibliográficas. Un resultado apuntaba a toponhisp.org: **no se abrió** (prohibido). **Busqué y no encontré** |
| **Tumbos de Samos, Sobrado y Celanova** | **Sí**, dentro de **CODOLGA** | Centro Ramón Piñeiro (Xunta de Galicia), `corpus.cirp.gal/codolga`, versión 22 (2025), 21.392 documentos de los siglos VI-XV. Ediciones de base según su página «Edicións»: Lucas, *Tumbo de San Julián de Samos* (1986); Loscertales, *Tumbos del Monasterio de Sobrado*; Andrade, *O tombo de Celanova* (1995) | **No entero.** Solo los resultados de cada búsqueda (texto separado por tabulaciones, según sus preguntas frecuentes) | Sin robots.txt (404 en corpus.cirp.gal) | Páginas abiertas y leídas (inicio, «Edicións», preguntas frecuentes). No encontré ahí una licencia explícita de uso comercial: **falta confirmarla** |
| **CODOLHISP** (`codolhisp.imf.csic.es`) | Desconocido | CSIC, Institució Milà i Fontanals (red de corpus documentales latinos hispánicos) | Desconocido | **No se pudo leer** | **No conecta.** Por http responde 302 a https, y la pasarela de red de este entorno rechaza la conexión HTTPS a `codolhisp.imf.csic.es` y a `www.imf.csic.es` (502 en CONNECT: la política de red del entorno o una falla del servidor). No es un bloqueo por robots |
| **CODEA+ 2022** (otro corpus encontrado) | Sí, **solo consulta** | GITHE, Universidad de Alcalá, `corpuscodea.es`. 4.023 documentos, de los orígenes a 1900; fuentes de archivo (AHN, Simancas, archivos de Toledo y Guadalajara…) | **No.** No encontré ninguna descarga | Sin robots.txt (404) | Página abierta y leída. **Licencia CC BY-NC-ND.** Texto literal: «No ser permite un uso comercial del corpus… queda prohibida… la reproducción total o parcial y la difusión del corpus o de documentos del corpus con fines comerciales… Los materiales de CODEA podrán ser citados, pero no reutilizados.» **Ojo: el libro es comercial.** Se puede citar un documento puntual, no usar el corpus como base |
| **Corpus CHARTA** (`corpuscharta.es`) | **No disponible** | Red CHARTA (enlazada desde CODEA) | No | — | El dominio muestra la página de OVH «Site en construction»: el corpus no está en línea en esa dirección |
| **Hosts no tocados, por prohibición** | — | toponhisp.org, eusko-ikaskuntza.eus, dle.rae.es | — | Prohíben agentes de IA o tienen desafío anti-bots | No se abrieron |
| **produccioncientifica.usal.es** | — | Portal de la Universidad de Salamanca (apareció en la búsqueda de Sahagún) | — | **Prohíbe a GPTBot y a ClaudeBot** (`Disallow: /`) | **No se entró** |

## PASO B · Barrido

**No se hizo.** Ninguno de los corpus revisados cumple la condición de poder bajarse entero como edición:

| Motivo | Corpus |
|---|---|
| Solo edición impresa (no encontré versión digital abierta) | Sahagún, Otero de las Dueñas, Cardeña, Becerros de Valpuesta (edición 2010) |
| Facsímil sin texto utilizable | Becerro Gótico de Valpuesta en archive.org |
| Solo consulta o descarga por búsqueda | CODOLGA (Samos, Sobrado, Celanova), CODEA+ 2022 |
| No se pudo conectar | CODOLHISP, PARES |
| Fuera de línea | CHARTA |

**En consecuencia, los 35 apellidos sin huella en el Becerro Galicano siguen sin huella documentada.** La búsqueda se hizo en el Becerro Galicano (773 documentos), con las formas declaradas en la Cosecha 1. Los demás cartularios **no se pudieron barrer**, así que para ellos no hay resultado, ni positivo ni negativo: «no se buscó» no equivale a «no está».

## Opciones para decidir (no ejecutadas)

| Opción | Qué haría | Límite |
|---|---|---|
| CODOLGA por búsqueda | Una búsqueda por forma antigua de cada uno de los 35 apellidos, bajando la tabla de resultados que ofrece el sitio | No es un barrido del corpus entero: es una consulta por forma. Hay que confirmar antes la licencia de uso. Solo cubre Galicia |
| CODOLHISP | Habilitar `codolhisp.imf.csic.es` en el acceso de red del entorno (menú del entorno en la barra de título de la sesión → Editar → Acceso de red) y reintentar | No sé todavía qué ofrece: ni la descarga ni la licencia están verificadas |
| Ediciones impresas (Sahagún, Otero, Cardeña, Valpuesta) | Consulta en biblioteca | Fuera del alcance de un script |
