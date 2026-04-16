
from datetime import datetime, timedelta

from Clasessala import one_room, two_room, three_room, four_room, five_room

from FuncionesEspecificas import load_archives, add_reservations, funtion_save, List, verificar_disponibilidad_recursos



class Interfaz :

    def __init__(self):

        self.salas = {

            1 : one_room,

            2 : two_room,

            3 : three_room,

            4 : four_room,

            5 : five_room

        }

        load_archives()


        self.bussiness_hour = datetime.strptime("08:00", "%H:%M").time()

        self.horario_cierre = datetime.strptime("17:00", "%H:%M").time()

        self.dias_laborales = [0,1,2,3,4]

      

    
    def selection_recurses(self):

        
        
        print("\n" + "="*50)
        print("🎮 SELECCIÓN DE RECURSOS")
        print("="*50)
        
        print("\n¿Como deseas seleccionar los recursos?")
        print("1. Seleccion por unidad")
        print("2. Seleccion con cantidades específicas")
        
        option = input("👉 Opcion 1 o 2: ").strip()
        
        if option == "2":
            from FuncionesEspecificas import selection_counter_recurses, obtention_state
            recurses = selection_counter_recurses()
        else:
        
            print("\nCOMBINACIONES NO PERMITIDAS")
            print("LICORES + PS3 + PS5 +PS4")
            print("Comida + PS3 + PS4 + PS5")
            print("Juegos de Mesa + PS3 + PS5 ")

            print("1. Bocina")
            print("2. Juegos de mesa")
            print("3. Comida")
            print("4. Ningun recurso (solo la sala basica)")
            print("5. PS3")
            print("6. PS4")
            print("7. PS5")
            print("8. Licores")
            print("9. Terminar selección")
            
            seleccionated_recurses = []
            mapear_seletion = {
                '7': 'PS5',
                '6': 'PS4',
                '5': 'PS3',
                '3': 'Comida',
                '8': 'Licores',
                '2': 'Juegos de Mesa',
                '1': 'Bocinas'
            }
            
            while True:
                print(f"\nRecursos seleccionados: {', '.join(seleccionated_recurses) if seleccionated_recurses else 'Ninguno'}")
                
                option = input().strip()

                if option == "9":
                    break
                elif option == "4":
                    seleccionated_recurses = []
                    print("✅ Solo sala basica seleccionada")
                    break
                elif option in mapear_seletion:
                    recurso = mapear_seletion[option]
                    if recurso in seleccionated_recurses:
                        seleccionated_recurses.remove(recurso)
                        print(f"❌ {recurso} removido")
                    else:
                        tem_recursos = seleccionated_recurses + [recurso]
                        from Clasessala import Salas
                        valid, message = Salas.compatibility_verification(tem_recursos)

                        if valid:
                            seleccionated_recurses.append(recurso)
                            print(f"✅ {recurso} añadido")
                        else:
                            print(message)
                else:
                    print("Opcion no valida")
            
            recurses = seleccionated_recurses
        
        return recurses


    
    
    def laboral_day(self, fecha_hora):
        if fecha_hora.weekday() in self.dias_laborales:
            return True, "Dia laboral"
        return False, "Solo se pueden hacer reservas de lunes a viernes"

    def duration(self, hours_duration):
        if 1 <= hours_duration <= 7:
            return True, "Duración valida"
        elif hours_duration < 1 :
            return False, "La reserva debe ser con un valor de tiempo valido"
        return False, "La duracion debe ser entre 1 y 7 horas"

    def room_exixtence(self, sala_numero):
        if int(sala_numero) in self.salas:
            return True, "Sala encontrada"
        return False, "La sala no existe"
    

    def date(self, hour_date):
        now = datetime.now()
        if hour_date < now:
            return False, "No se puede reservar en el pasado"
        if hour_date > now + timedelta(days=30):
            return False, "Solo se puede reservar con 30 dias de anticipacion"
       
        return True, "Fecha valida" 
    
   
 

    def verification(self, fecha_hora, sala_numero, hora_fin, recursos_solicitados=None):
        load_archives()
        
        for reserva in List.values():
            if str(reserva.get('Sala')) == str(sala_numero):
                ex_inicio = datetime.strptime(reserva['Inicio'], "%Y-%m-%d %H:%M:%S")
                ex_fin = datetime.strptime(reserva['Fin'], "%Y-%m-%d %H:%M:%S")
                
                if fecha_hora < ex_fin and hora_fin > ex_inicio:
                    
                    duracion = (hora_fin - fecha_hora).total_seconds() / 3600
                    
                   
                    huecos = self.search_disponibles_hours(sala_numero, duracion, fecha_hora)
                    
                    print("\n❌ Horario ocupado.")
                    if huecos:
                        print("💡 Sugerencias:")
                        for h in huecos[:3]:
                            print(f"   • {h['fecha']} a las {h['hora_inicio']}")
                        return False, "Vuelva atras y escoja la reserva que mas se le acomode"
                    
                    
        
        return True, "Disponible"
  
    def verificar_reserva_completa(self, sala_numero, fecha_hora, duracion_horas, recursos_solicitados=None):
        v, m = self.room_exixtence(sala_numero)
        if not v: return False, m

        v, m = self.duration(duracion_horas)
        if not v: return False, m

        v, m = self.laboral_day(fecha_hora)
        if not v: return False, m

        v, m = self.date(fecha_hora)
        if not v: return False, m

        hora_fin = fecha_hora + timedelta(hours=duracion_horas)
        v, m = self.horario_verificacion(fecha_hora, hora_fin)
        if not v: return False, m


        v, m = self.verification(fecha_hora, sala_numero, hora_fin, recursos_solicitados)
        if not v: return False, m

        return True, "Reserva verificada exitosamente"
    def estado_de_salas_en_vivo(self):
        load_archives() 
        resultados = {}
        for num, sala_objeto in self.salas.items():
            from Clasessala import Salas 
            estado = Salas.Obtencion_estado(num, List) 
            resultados[num] = estado
        return resultados
    def horario_verificacion(self,inicio, fin) :
        if inicio.time() >= self.bussiness_hour and fin.time() <= self.horario_cierre :
            return True, "Horario valido"
        return False, "Horario no valido"

        

    def reservar_sala(self, sala_numero, fecha_hora, duracion_horas, descripcion="", usuario=""):

        disponible, mensaje = self.verificar_reserva_completa(sala_numero, fecha_hora, duracion_horas)
       

        if not disponible:

            return False, mensaje, None
        

        try:

            recursos = self.selection_recurses()

            from Clasessala import Salas
            compatibles, mensaje_compat = Salas.compatibility_verification(recursos)
            if not compatibles:
                return False, mensaje_compat, None

            disponible, mensaje = self.verificar_reserva_completa( sala_numero, fecha_hora, duracion_horas, recursos)
       
            hora_fin = fecha_hora + timedelta(hours=duracion_horas)

            id_reserva = add_reservations(descripcion or f"Reserva Sala {sala_numero}",fecha_hora.strftime("%Y-%m-%d %H:%M:%S"),sala_numero, duracion_horas, recursos,interfaz=self)

            if id_reserva:
                print("Reserva confirmada")
               

                funtion_save()

                mensaje_exito = (

                    f"✅ **RESERVA CONFIRMADA**\n\n"

                    f"**ID Reserva:** {id_reserva}\n"

                    f"**Sala:** {sala_numero}\n"

                    f"**Fecha:** {fecha_hora.strftime('%Y-%m-%d')}\n"

                    f"**Horario:** {fecha_hora.strftime('%H:%M')} - {hora_fin.strftime('%H:%M')}\n"

                    f"**Duración:** {duracion_horas} horas\n"  
                    f"**Recursos:** {', '.join(recursos) if recursos else 'Ninguno'}"

            
                    
                   

                )
                

                return True, mensaje_exito, id_reserva
            else:

                return False, " Error al crear la reserva en el sistema" 

        except Exception as e:

            return False, f" Error: {str(e)}", None
                    



    def search_disponibles_hours(self, sala_numero, duracion, fecha_inicio=None, dias_busqueda=7):
        if fecha_inicio is None:
            fecha_inicio = datetime.now()
        
        ahora = datetime.now()
        huecos = []
        duracion_float = float(duracion)
       
        duracion_int = int(duracion_float) 

        for i in range(dias_busqueda):
            fecha_dia = fecha_inicio + timedelta(days=i)
            if fecha_dia.weekday() >= 5: continue 
            
          
            for hora in range(8, 17 - duracion_int + 1):
                for minuto in [0, 30]:
                    posible_inicio = fecha_dia.replace(hour=hora, minute=minuto, second=0, microsecond=0)
                    posible_fin = posible_inicio + timedelta(hours=duracion_float)
                    
                    if posible_inicio < ahora: continue
                    
                    colision = False
                    for element in List.values():
                        if str(element.get('Sala')) == str(sala_numero):
                            ex_ini = datetime.strptime(element['Inicio'], "%Y-%m-%d %H:%M:%S")
                            ex_fin = datetime.strptime(element['Fin'], "%Y-%m-%d %H:%M:%S")
                            if posible_inicio < ex_fin and posible_fin > ex_ini:
                                colision = True
                                break
                    
                    if not colision:
                        huecos.append({
                            'fecha': posible_inicio.strftime('%Y-%m-%d'),
                            'hora_inicio': posible_inicio.strftime('%H:%M'),
                            'duracion': duracion_float
                        })
                    
                    if len(huecos) >= 5: return huecos 
        return huecos


    


    

