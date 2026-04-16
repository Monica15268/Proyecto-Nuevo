import json
import os 
from datetime import timedelta, datetime
archivo_de_json = "guardador.json"




List = {}
actually_id = 1
#Esta funcion se encarga de cargar los datos en el json
def load_archives():
    global List, actually_id
    if os.path.exists(archivo_de_json):
        try:
            with open(archivo_de_json, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                List.clear() 
                List.update(datos.get('guardador', {}))
                actually_id = datos.get('identidad', 1)
        except (json.JSONDecodeError, FileNotFoundError):
            List.clear()
            actually_id = 1
#Esta se encarga de guardarlos
def funtion_save():
    with open(archivo_de_json, 'w', encoding='utf-8') as f:
        json.dump({'guardador': List, 'identidad': actually_id}, f, indent=4)




#Esta se encarga de agregar las reservas al json
def add_reservations(descripcion, fecha_hora, sala_numero, duracion_horas, recurses=None, reserva_id_excluir=None, interfaz=None):
    global actually_id, List
    load_archives()
    
    if recurses is None:
        recurses = []
    
    if isinstance(fecha_hora, str): 
        initial_hour = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M:%S")
    else:
        initial_hour = fecha_hora
    
    end_hour = initial_hour + timedelta(hours=duracion_horas)
    
    format = "%Y-%m-%d %H:%M:%S"


    disponible_room = True
    problem_reserve = None
    
    for res_id, datos in List.items():
        if reserva_id_excluir and str(res_id) == str(reserva_id_excluir):
            continue
            
        if int(datos['Sala']) == int(sala_numero):
            ex_inicio = datetime.strptime(datos['Inicio'], format)
            ex_fin = datetime.strptime(datos['Fin'], format)
            
            if initial_hour < ex_fin and end_hour > ex_inicio:
                disponible_room = False
                problem_reserve = datos
                break
    
    if not disponible_room:
        print("\n❌ La sala ya está ocupada en ese horario")
        print(f"   Horario en conflicto: {problem_reserve['Inicio']} hasta {problem_reserve['Fin']}")
        print("\n🔍 Buscando horarios alternativos...")
        print("\n🔍 Buscando horarios alternativos...")
        try:
           
                if isinstance(fecha_hora, str):
                    fecha_busqueda = datetime.strptime(fecha_hora, format)
                else:
                    fecha_busqueda = fecha_hora
                
                
                huecos = interfaz.buscar_huecos_disponibles(
                    sala_numero=sala_numero,
                    duracion_horas=duracion_horas,
                    fecha_inicio=fecha_busqueda,
                    dias_busqueda=7
                )
                
                if huecos:
                    print("\n✅ ¡HORARIOS ALTERNATIVOS ENCONTRADOS!")
                    print("="*60)
                    
                   
                    huecos_por_fecha = {}
                    for hueco in huecos:
                        fecha = hueco['fecha']
                        if fecha not in huecos_por_fecha:
                            huecos_por_fecha[fecha] = []
                        huecos_por_fecha[fecha].append(hueco)
                    
               
                    print("\n📅 Próximos horarios disponibles:")
                    for fecha, huecos_fecha in sorted(huecos_por_fecha.items())[:3]:  # Limitar a 3 días
                        print(f"\n   {fecha}:")
                        for i, hueco in enumerate(huecos_fecha[:3], 1):  # Limitar a 3 horarios por día
                            print(f"     {i}. {hueco['hora_inicio']} - {hueco['hora_fin']} ({hueco['duracion']}h)")
                    
                   
                    respuesta = input("\n👉 ¿Deseas reservar alguno de estos horarios? (s/n): ").lower()
                    if respuesta == 's':
                        print("   ⚠️  Por favor, usa la opción 'Nueva Reserva' del menú principal con el horario sugerido.")
                else:
                    print("\n😞 No se encontraron horarios alternativos en los próximos 7 días.")
                    print("\n💡 SUGERENCIAS:")
                    print("   • Prueba con otra sala")
                    print("   • Reduce la duración de la reserva")
                    print("   • Intenta con otra fecha")
                    
        except Exception as e:
            print(f"\n❌ Error al buscar horarios alternativos: {e}")
        
        return False    
        
    
  
    if recurses:
        disponibles, mensaje = verificar_disponibilidad_recursos(
            initial_hour, duracion_horas, recurses, sala_numero, reserva_id_excluir
        )
        if not disponibles:
            print(f"\n❌ {mensaje}")
            
            recursos_ocupados = obtener_recursos_ocupados_en_horario(initial_hour, duracion_horas)
            recursos_conflicto = [r for r in recurses if r in recursos_ocupados]
            
            if recursos_conflicto:
                print("\n📋 Detalle del conflicto:")
                for recurso in recursos_conflicto:
                    print(f"\n   {recurso} está siendo usado en:")
                    for uso in recursos_ocupados[recurso]:
                        print(f"     • Sala {uso['sala']} (Reserva ID: {uso['reserva_id']})")
                        print(f"       Horario: {uso['horario']}")
            
            from Clasessala import Salas
            print("\n📊 Estado actual del inventario:")
            Salas.window_inventary()
            
            return None
    

    List[str(actually_id)] = {
        "Sala": int(sala_numero),
        "Descripcion": descripcion,
        "Inicio": initial_hour.strftime("%Y-%m-%d %H:%M:%S"),
        "Fin": end_hour.strftime("%Y-%m-%d %H:%M:%S"),
        "Duracion": duracion_horas,
        'Recursos': recurses if recurses else [],
        "Estado": "CONFIRMADA"
    }
    
    print(f"\n✅ RESERVA CREADA EXITOSAMENTE")
    print(f"   ID: {actually_id}")
    print(f"   Descripción: {descripcion}")
    if recurses:
        from collections import Counter
        conteo_recursos = Counter(recurses)
        print(f"   Recursos incluidos:")
        for recurso, cantidad in conteo_recursos.items():
            print(f"     • {cantidad}x {recurso}")
    else:
        print(f"   Recursos incluidos: Ninguno")
    
    print(f"   Inicio: {initial_hour.strftime('%Y-%m-%d %H:%M')}")
    print(f"   Fin: {end_hour.strftime('%Y-%m-%d %H:%M')}")
    print(f"   Duración: {duracion_horas} horas")
    
    id_reserva = actually_id
    actually_id += 1
    funtion_save()
    return id_reserva
def listar() :
    load_archives()
    if not List:
        print("No hay reservas existentes.")
        return
    print("📋 LISTADO DE RESERVAS")
    print("="*60)
    
    for id_tarea, datos_tarea in List.items():
        print(f"\n ID: {id_tarea}")
        print(f"   Descripción: {datos_tarea.get('Descripcion', 'N/A')}")
        print(f"    Estado: {datos_tarea.get('Estado', 'N/A')}")
        print(f"   Sala: {datos_tarea.get('Sala', 'N/A')}")
        if 'Inicio' in datos_tarea:
            print(f"   Inicio: {datos_tarea['Inicio']}")
        if 'Fin' in datos_tarea:
            print(f"   Fin: {datos_tarea['Fin']}")
        if 'Duracion' in datos_tarea:
            print(f"    Duración: {datos_tarea['Duracion']} horas")
        
        print("  " + "-"*40)
    
    print(f"\n📊 Total: {len(List)} reserva(s)")
    print("="*60)
    return List

def eliminar(id) :
    global List
    load_archives()
    str_id = str(id)
    if str_id in List :
        del List[str_id]
        funtion_save()
        return True
    return False
    



def verificar_disponibilidad_recursos(fecha_hora, duracion_horas, recursos_solicitados, sala_numero=None, reserva_id_excluir=None):
   
    global List
    load_archives()
    
    if not recursos_solicitados or recursos_solicitados == []:
        return True, "✅ Recursos disponibles"
    
    hora_fin = fecha_hora + timedelta(hours=duracion_horas)
    
   
    from Clasessala import Salas
    inventario_ok, mensaje_inventario = Salas.verify_disponibility(
        recursos_solicitados, fecha_hora, duracion_horas
    )
    
    if not inventario_ok:
        return False, mensaje_inventario
    
   
    recursos_no_disponibles = []
    
    for reserva_id, reserva_data in List.items():
       
        if reserva_id_excluir and str(reserva_id) == str(reserva_id_excluir):
            continue
        
       
        try:
            inicio_existente = datetime.strptime(reserva_data['Inicio'], "%Y-%m-%d %H:%M:%S")
            fin_existente = datetime.strptime(reserva_data['Fin'], "%Y-%m-%d %H:%M:%S")
        except:
            continue
        
        
        if fecha_hora < fin_existente and hora_fin > inicio_existente:
          
            recursos_existentes = reserva_data.get('Recursos', [])
            
           
            for recurso in recursos_solicitados:
                if recurso in recursos_existentes:
                  
                    sala_existente = reserva_data.get('Sala')
                    if sala_existente and str(sala_existente) != str(sala_numero):
                        recursos_no_disponibles.append(recurso)
    
    if recursos_no_disponibles:
        recursos_unicos = list(set(recursos_no_disponibles))
        return False, f"❌ Los siguientes recursos no están disponibles en ese horario: {', '.join(recursos_unicos)}"
    
    return True, "✅ Recursos disponibles"
def obtener_recursos_ocupados_en_horario(fecha_hora, duracion_horas):
   
    global List
    load_archives()
    
    hora_fin = fecha_hora + timedelta(hours=duracion_horas)
    recursos_ocupados = {}
    
    for reserva_id, reserva_data in List.items():
        try:
            inicio_existente = datetime.strptime(reserva_data['Inicio'], "%Y-%m-%d %H:%M:%S")
            fin_existente = datetime.strptime(reserva_data['Fin'], "%Y-%m-%d %H:%M:%S")
        except:
            continue
        
     
        if fecha_hora < fin_existente and hora_fin > inicio_existente:
            recursos = reserva_data.get('Recursos', [])
            sala = reserva_data.get('Sala', 'Desconocida')
            
            for recurso in recursos:
                if recurso not in recursos_ocupados:
                    recursos_ocupados[recurso] = []
                recursos_ocupados[recurso].append({
                    'sala': sala,
                    'reserva_id': reserva_id,
                    'horario': f"{inicio_existente.strftime('%H:%M')} - {fin_existente.strftime('%H:%M')}"
                })
    
    return recursos_ocupados

def selection_counter_recurses():

    from Clasessala import Recurses_inventary
    
    recursos_seleccionados = []
    
    print("\n" + "="*50)
    print("🎮 SELECCIÓN DE RECURSOS CON CANTIDAD")
    print("="*50)
    

    from Clasessala import Salas
    Salas.window_inventary()
    
    while True:
        print("\nOpciones:")
        print("1. Agregar recurso")
        print("2. Remover recurso") 
        print("3. Ver selección actual")
        print("4. Finalizar selección")
        
        opcion = input("👉 Selecciona una opción: ").strip()
        
        if opcion == "1":
            print("\nRecursos disponibles:")
            recursos_lista = list(Recurses_inventary.keys())
            for i, recurso in enumerate(recursos_lista, 1):
                print(f"{i}. {recurso}")
            
            try:
                recurso_idx = int(input("Número del recurso: ")) - 1
                if 0 <= recurso_idx < len(recursos_lista):
                    recurso = recursos_lista[recurso_idx]
                    
           
                    cantidad_max = Recurses_inventary[recurso]
                    print(f"Cantidad máxima disponible: {cantidad_max}")
                    
                    cantidad = int(input(f"Cantidad de {recurso} (1-{cantidad_max}): "))
                    
                    if 1 <= cantidad <= cantidad_max:
                 
                        for _ in range(cantidad):
                            recursos_seleccionados.append(recurso)
                        print(f"✅ {cantidad}x {recurso} añadido(s)")
                    else:
                        print("❌ Cantidad inválida")
                else:
                    print("❌ Opción inválida")
            except ValueError:
                print("❌ Entrada inválida")
                
        elif opcion == "2":
            if not recursos_seleccionados:
                print("❌ No hay recursos seleccionados")
                continue
                
            print("\nRecursos seleccionados:")
            from collections import Counter
            conteo = Counter(recursos_seleccionados)
            for i, (recurso, cantidad) in enumerate(conteo.items(), 1):
                print(f"{i}. {cantidad}x {recurso}")
            
            try:
                recurso_idx = int(input("Número del recurso a remover: ")) - 1
                recursos_lista = list(conteo.keys())
                if 0 <= recurso_idx < len(recursos_lista):
                    recurso = recursos_lista[recurso_idx]
                    recursos_seleccionados = [r for r in recursos_seleccionados if r != recurso]
                    print(f"✅ {recurso} removido")
                else:
                    print("❌ Opción inválida")
            except ValueError:
                print("❌ Entrada inválida")
                
        elif opcion == "3":
            if recursos_seleccionados:
                from collections import Counter
                conteo = Counter(recursos_seleccionados)
                print("\n📋 Selección actual:")
                for recurso, cantidad in conteo.items():
                    print(f"   • {cantidad}x {recurso}")
                print(f"   Total recursos: {len(recursos_seleccionados)}")
            else:
                print("\n📋 No hay recursos seleccionados")
                
        elif opcion == "4":
            break
            
        else:
            print("❌ Opción inválida")
    
    return recursos_seleccionados


def obtention_state(inicio, fin) :
    global List
    from Clasessala import Recurses_inventary

    stock = Recurses_inventary.copy()
    
    formato = "%Y-%m-%d %H:%M:%S"
    
    try:
        start_application = datetime.strptime(inicio, formato)
        end_application = datetime.strptime(fin, formato)
        
        for valor in List.values():
            start_valor = datetime.strptime(valor['Inicio'], formato)
            end_valor = datetime.strptime(valor['Fin'], formato)
            
           
            if start_application < end_valor and end_application > start_valor:
                for item in valor.get('Recurses_inventary', []):
                    if item in stock:
                        stock[item] -= 1
    except Exception as e:
        print(f"Error calculando stock: {e}")
        
    return stock