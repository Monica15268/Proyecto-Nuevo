# LUDOPATH - Sistema de reservas para una sala de juego

Ludopath es una aplicacion desarrollada en python y con JSON como base de datos que se encarga de controlar las reservas para permitir que cada cliente tenga su espacio asegurado, incluso con posibilidad de sugerir en algun horario desde ese dia hasta los proximos 30 dias, en dependencia de los huecos libres en el horario.
-----------------------------------------------------------
## ✨ Características principales
* **Gestion de 5 salas únicas:** Cada una con diferentes capacidades y recursos (consolas, juegos de mesa, comida).
* **Motor de Validacion:** Controla que no haya choques de horarios, que las reservas sean en días laborales y dentro del horario permitido (08:00 - 17:00).
* **Busqueda Inteligente de Huecos:** Si una sala está ocupada, el sistema sugiere automáticamente los próximos 15 horarios disponibles.
* **Persistencia de Datos:** Las reservas se guardan automáticamente en un archivo `guardador.json`.
* **Comprobacion de recursos:** Se permite si a cierta hora los recursos estan disponibles
* **RECURSOS:** 
1 - Comida
2 - PS3, PS4, PS5
3 - Licores
4- Bocinas
5 - Juegos de Mesa
* **COMBINACIONES** :
Comida puede mezclarse con cualquiera menos con las consola.
Por otra parte, las consolas deben ir obligado con las bocinas, y
con los juegos de mesa debe haber comida 

PARA CORRER ESTE PROYECTO SOLO DEBE CLONARLO EN GIT HUB Y CORRER EL ARCHIVO CONSOLA.PY, CONTENIDO EN LA CARPETA SRC

* **Disfrutelo**
---