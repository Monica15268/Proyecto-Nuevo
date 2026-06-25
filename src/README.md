# LUDOPATH - Sistema de reservas para una sala de juego


Ludopath es una innovadora aplicación diseñada para facilitar la gestión de reservas en espacios de entretenimiento, desarrollada en el versátil lenguaje de programación Python. Utilizando JSON como su base de datos, Ludopath se encarga de controlar las reservas de manera eficiente, asegurando que cada cliente tenga su espacio garantizado. Esta aplicación no solo permite realizar reservas en tiempo real, sino que también ofrece la posibilidad de sugerir horarios disponibles desde el mismo día hasta los próximos 30 días, dependiendo de los espacios libres en el horario establecido. Este enfoque flexible y dinámico hace que Ludopath sea una herramienta invaluable para la administración de espacios recreativos. 

La motivacion para crear este proyecto comenzo desde mi visita al centro recreativo LudoTerra, ubicado en La Habana, ya que este se manejaba las reservas por horas y cantidad de personas, y en caso de que este se expandiera aun mas, podria llegar a necesitar un programa como este. 
-----------------------------------------------------------
Informacion de que contiene cada archivo
1- En Funciones Especificas se encuentra todo lo relacionado a reservar, seleccion de recursos y eliminacion de reservas. 

2-En el archivo bueno(mi motivacion para ello es porque se encarga de darle el visto bueno a la reserva), en este se comprueba si es dia laborable, si el horario se encuentra en el rango y si los recursos pueden ser reservados. 

3-En el archivo consola tengo como se va a ver el proyecto desde la consola y todo lo que tiene que pasar para que sea intuitivo para cualquier usuario, sin importar su edad o conocimientos en tecnologia. 
-----------------------------------------------------------
## ✨ Características principales
* Gestion de 5 salas únicas: Una de las características más interesantes de Ludopath es su capacidad para gestionar cinco salas únicas. Cada sala está diseñada con diferentes capacidades y recursos, lo que permite a los clientes elegir el espacio que mejor se adapte a sus necesidades. Las salas están equipadas con diversas opciones de entretenimiento, incluyendo consolas de videojuegos, juegos de mesa y opciones de comida. Esto no solo proporciona una experiencia personalizada a los clientes, sino que también maximiza el uso eficiente del espacio disponible. 

*  Motor de Validación 

El motor de validación es una de las funcionalidades clave que distingue a Ludopath. Este motor se encarga de controlar que no haya choques de horarios al momento de realizar una reserva. Además, garantiza que las reservas se efectúen únicamente en días laborales y dentro del horario permitido, que está establecido entre las 08:00 y las 17:00 horas. Esta característica es fundamental para mantener un flujo ordenado y eficiente en la gestión del espacio, evitando conflictos y asegurando que todos los clientes tengan acceso a las instalaciones según lo programado. 

* Búsqueda Inteligente de Huecos 

Ludopath incorpora un sistema inteligente de búsqueda de huecos que mejora significativamente la experiencia del usuario. Si una sala está ocupada en un horario solicitado, el sistema sugiere automáticamente los próximos 15 horarios disponibles. Esta funcionalidad reduce el tiempo que los clientes pasan buscando un espacio adecuado y facilita la planificación de sus actividades. La búsqueda inteligente no solo ahorra tiempo, sino que también aumenta la satisfacción del cliente al ofrecer soluciones rápidas y efectivas.
Ludopath es una aplicacion desarrollada en python y con JSON como base de datos que se encarga de controlar las reservas para permitir que cada cliente tenga su espacio asegurado, incluso con posibilidad de sugerir en algun horario desde ese dia hasta los proximos 30 dias, en dependencia de los huecos libres en el horario.
-----------------------------------------------------------

* Persistencia de datos
 La persistencia de datos es otro aspecto crucial en la funcionalidad de Ludopath. Todas las reservas se guardan automáticamente en un archivo llamado guardador.json. Este archivo actúa como una base de datos donde se registran todas las transacciones realizadas por los usuarios. La utilización de JSON como formato para almacenar información permite una fácil manipulación y recuperación de datos, lo que es esencial para el funcionamiento continuo de la aplicación. Además, esta característica asegura que no se pierda ninguna información importante sobre las reservas realizadas.

* Comprobación de Recursos

Ludopath también incluye un sistema para comprobar la disponibilidad de recursos en tiempo real. Esto significa que antes de confirmar una reserva, el sistema verifica si los recursos necesarios están disponibles para el horario solicitado. Los recursos disponibles incluyen:

• Comida
• Consolas (PS3, PS4, PS5)
• Licores
• Bocinas
• Juegos de mesa

Esta verificación es vital para garantizar que los clientes tengan acceso a todos los recursos que desean durante su estancia en las instalaciones.

* Combinaciones de Recursos

Ludopath permite ciertas combinaciones entre los recursos disponibles, lo cual añade un nivel adicional de personalización a las reservas. A continuación se detallan las combinaciones permitidas:

• Comida puede mezclarse con cualquiera de los recursos mencionados, excepto con las consolas.
• Las consolas deben ir obligatoriamente acompañadas por bocinas.
• Con los juegos de mesa, debe haber siempre comida disponible para complementar la experiencia.

Estas combinaciones no solo enriquecen la experiencia del usuario, sino que también fomentan un ambiente más social y entretenido para aquellos que utilizan las instalaciones.

* Cómo Correr el Proyecto

Para aquellos interesados en implementar o experimentar con Ludopath, el proceso es bastante sencillo. Solo es necesario clonar el repositorio desde GitHub y ejecutar el archivo consola.py, que se encuentra en la carpeta principal del proyecto src. Este archivo actúa como el punto de entrada a la aplicación y permite interactuar con todas sus funcionalidades desde la consola.

Además, es importante mencionar que el proyecto está diseñado para ser fácilmente extensible. Los desarrolladores pueden añadir nuevas características o modificar las existentes sin complicaciones significativas. Esto se logra gracias a la estructura modular del código y a la documentación clara que acompaña al repositorio

## Futuras Mejoras

A medida que Ludopath continúa evolucionando, hay varias áreas donde se pueden implementar mejoras adicionales. Por ejemplo, integrar un sistema de notificaciones podría alertar a los usuarios sobre cambios en sus reservas o nuevas ofertas disponibles. También se podría considerar la implementación de un sistema de puntuación o comentarios que permita a los usuarios calificar su experiencia y proporcionar retroalimentación valiosa.

Además, se podría explorar la posibilidad de integrar métodos de pago directamente en la aplicación, lo que facilitaría aún más el proceso para los usuarios. Esto no solo aumentaría la comodidad para los clientes, sino que también podría abrir nuevas oportunidades comerciales al permitir promociones o descuentos exclusivos.


## Tecnologias y lenguajes utilizados 

1. Python: El lenguaje principal utilizado para desarrollar Ludopath, conocido por su simplicidad y legibilidad.
2. Librerías de Python: Incluyendo Collections, DateTime, y otras que facilitan la manipulación de datos y la gestión del tiempo.

La elección de Python como lenguaje principal no es casual; este lenguaje es ampliamente utilizado en el desarrollo de aplicaciones debido a su versatilidad y a la gran cantidad de bibliotecas disponibles que permiten realizar tareas complejas con poco código.


## Ventajas principales de utilizar el proyecto 
Mayor Control de Reservas: Se permite un mayor control de las reservas y los recursos para evitar confusiones o faltantes, asegurando así que el visitante tenga una mejor experiencia
 
Cumplimiento de Medidas Sanitarias:

Ludopath no solo se preocupa por facilitar la gestión de reservas, sino que también juega un papel crucial en la promoción del cumplimiento de las medidas sanitarias establecidas en los espacios recreativos. En un mundo donde la salud pública se ha convertido en una prioridad innegable, la aplicación permite a los usuarios gestionar el aforo de manera efectiva, asegurando que se respeten las normas de distanciamiento social y otras directrices sanitarias. Esto no solo protege a los clientes, sino que también brinda tranquilidad a los propietarios de los negocios, quienes pueden operar con confianza sabiendo que están haciendo todo lo posible para mantener un ambiente seguro y saludable. Además, la aplicación ofrece recordatorios sobre las medidas sanitarias vigentes, lo que ayuda a mantener a todos informados y comprometidos con su cumplimiento.

Protección de Bienes Materiales:

Otra característica destacada de Ludopath es su diseño orientado a la protección de los bienes materiales del lugar. Al permitir reservas solo a personas que se comprometen a cuidar el espacio y sus instalaciones, se minimiza el riesgo de daños o mal uso. Esto es especialmente importante en lugares donde los equipos son costosos o delicados. Al fomentar una cultura de responsabilidad entre los usuarios, la aplicación contribuye a la preservación del patrimonio del negocio, asegurando que cada cliente valore y respete el espacio que está utilizando. Además, la plataforma incluye un sistema de evaluación donde los usuarios pueden calificar su experiencia, lo que ayuda a identificar comportamientos inadecuados y promueve un uso más consciente del entorno.

Fomento a Reservas Anticipadas:

La funcionalidad de fomento a reservas anticipadas es vital para la planificación eficiente de eventos y actividades. Alentar a los clientes a realizar sus reservas con antelación no solo mejora la organización del negocio, sino que también permite a los usuarios planificar sus días especiales sin el estrés de posibles contratiempos. Con la posibilidad de prever la demanda y ajustar la oferta en consecuencia, los propietarios pueden optimizar sus recursos y maximizar su rentabilidad. Esta estrategia también permite ofrecer promociones especiales para quienes reserven con anticipación, incentivando así un mayor flujo de clientes.

Intuitividad:

La interfaz de Ludopath ha sido diseñada con un enfoque en la usabilidad, lo que permite que personas de todas las edades y niveles tecnológicos puedan navegar por la aplicación sin dificultades. Desde un abuelo de 99 años hasta un niño de 6 años que sepa leer, todos pueden realizar reservas de manera independiente. Esta accesibilidad amplía el alcance del servicio, permitiendo que más personas disfruten de las ventajas que ofrece la aplicación. Además, se han incluido tutoriales interactivos para ayudar a los nuevos usuarios a familiarizarse rápidamente con todas las funciones disponibles.

* Resumen

En conclusión, Ludopath es una aplicación poderosa y versátil diseñada para facilitar la gestión de reservas en espacios recreativos. Con su enfoque en la eficiencia, la personalización y la facilidad de uso, esta herramienta se posiciona como una solución ideal para cualquier negocio que busque optimizar su proceso de reservas. Gracias a sus características avanzadas como el motor de validación, búsqueda inteligente de huecos y comprobación de recursos, Ludopath no solo mejora la experiencia del cliente, sino que también simplifica la administración del espacio. Además, su compromiso con la salud pública, la protección de bienes materiales y la promoción de reservas anticipadas la convierten en una opción indispensable en el mercado actual.

Disfrútelo.