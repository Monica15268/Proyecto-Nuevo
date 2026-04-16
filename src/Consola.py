from datetime import datetime, timedelta
from Clasessala import Salas, one_room, two_room, three_room, four_room, five_room
from FuncionesEspecificas import load_archives, add_reservations, listar, funtion_save, List, eliminar, obtention_state
from bueno import Interfaz
def main():
    """Función principal para interfaz de consola"""
    print("="*60)
    print("🎮 LUDOPATH - SISTEMA DE RESERVAS DE SALAS")
    print("="*60)
    
   
    interfaz = Interfaz()
    
    while True:
        print("\n" + "="*60)
        print("MENÚ PRINCIPAL")
        print("="*60)
        print("\n1. 📅 Nueva Reserva")
        print("2. 📋 Ver Todas las Reservas")
        print("3. 🔍 Buscar Huecos Disponibles")
        print("4. 🗑️  Eliminar Reserva")
        print("5. 🏢 Ver Estado de Salas")
        print("6. Eliminar reservas fuera de fecha")
        print("7. 🚪 Salir")
        print("8. Ver recursos")
        print("\n" + "-"*40)
        
        opcion = input("👉 Selecciona una opción (1-8): ").strip()
        
        if opcion == "1":
            nueva_reserva(interfaz)
        elif opcion == "2":
            ver_reservas()
        elif opcion == "3":
            buscar_huecos(interfaz)
        elif opcion == "4":
            id_a_eliminar = input("Introduce el ID de la reserva a borrar: ")
            if eliminar(id_a_eliminar):
                print("✅ Borrado con éxito")
            else:
                print("❌ ID no encontrado")
        elif opcion == "5":
            estado_salas(interfaz)
        elif opcion == "6":
            eliminar_pasadas()
           
        

        elif opcion == "7":
            print("\n👋 ¡Gracias por usar LUDOPATH!")
            break
        
        elif opcion == "8":
            print("\n--- 🔍 CONSULTAR RECURSOS DISPONIBLES ---")
            fecha = input("Introduce la fecha (AAAA-MM-DD): ").strip()
            h_inicio = input("Hora inicio (HH:MM): ").strip()
            h_fin = input("Hora fin (HH:MM): ").strip()
            
          
            inicio_full = f"{fecha} {h_inicio}:00"
            fin_full = f"{fecha} {h_fin}:00"
            
        
            recursos_libres = obtention_state(inicio_full, fin_full)
            
            print(f"\n📦 Stock disponible para el {fecha} de {h_inicio} a {h_fin}:")
            print("-" * 45)
            for nombre, cantidad in recursos_libres.items():
                status = "✅ Disponible" if cantidad > 0 else "❌ AGOTADO"
                print(f"{nombre.ljust(15)} | Cantidad: {cantidad} | {status}")
            print("-" * 45)
            

        else:
            print("\n❌ Opción inválida. Intenta de nuevo.")
def eliminar_pasadas():
  
    load_archives()
    
    ahora = datetime.now()
   
    ids_a_borrar = []

    print(f"--- Escaneando reservas ---")

    for res_id, datos in List.items():
        try:
        
            fecha_fin = datetime.strptime(datos['Fin'], "%Y-%m-%d %H:%M:%S")
            
            if fecha_fin < ahora:
                ids_a_borrar.append(res_id)
        except Exception as e:
            print(f"Error en ID {res_id}: {e}")

   
    if ids_a_borrar:
        for rid in ids_a_borrar:
            print(f"🗑️ Eliminando if {rid} (vencio el {List[rid]['Fin']})")
            del List[rid]
        
     
        funtion_save() 
       
    else:
        print("ℹ️ No hay reservas pasadas para eliminar.")
        
def nueva_reserva(interfaz):
    print("\n--- NUEVA RESERVA ---")
    try:
        sala = int(input("Numero de sala (1-5): ").strip())
        fecha_str = input("Fecha y hora (YYYY-MM-DD HH:MM): ").strip()
        duracion = float(input("Duracion en horas: "))
        desc = input("Descripcion: ")

        try:
            fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        except ValueError:
            fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
       
        valido, mensaje, id_reserva = interfaz.reservar_sala(
            sala_numero=sala,
            fecha_hora=fecha_dt,
            duracion_horas=duracion,
            descripcion=desc,
            usuario=""
        )
        if valido:
            print(f"\n✅ {mensaje}")
            print(f"Reserva guardada con ID: {id_reserva}")
        else:
            print(f"\n❌ {mensaje}")
            
            
            
   
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado: {e}")



    
        
def ver_reservas():
    """Mostrar todas las reservas usando la función existente"""
    print("\n" + "="*50)
    print("📋 LISTADO DE RESERVAS")
    print("="*50)
    

    reservas = listar()
    
    if not reservas:
        print("\n📭 No hay reservas existentes")




def buscar_huecos(interfaz, sala_predefinida=None, duracion_predefinida=None):
    """Buscar huecos disponibles - SISTEMA DE SUGERENCIAS"""
    print("\n" + "="*50)
    print("🔍 SISTEMA DE SUGERENCIAS DE HORARIOS")
    print("="*50)
    
    try:
        if sala_predefinida is None:
            print("\n🏢 Selecciona una sala:")
            for num, sala in interfaz.salas.items():
                estado_salas = Salas.Obtencion_estado(num , List)
                estado = "🟢" if estado_salas == "DISPONIBLE" else "🔴"
                print(f"{num}. {estado} Sala {num} - Cap: {sala.capacidad}")
            
            sala_numero = int(input("\n👉 Número de sala: "))
        else:
            sala_numero = sala_predefinida
            print(f"\n🏢 Sala predefinida: {sala_numero}")
        
        if duracion_predefinida is None:
            duracion = float(input("⏱️  Duración necesaria (horas): "))
        else:
            duracion = duracion_predefinida
            print(f"⏱️  Duración predefinida: {duracion} horas")
        
        print("\n📅 ¿Cuántos días quieres buscar?")
        print("1. Hoy (1 día)")
        print("2. Esta semana (7 días)")
        print("3. Próximos 15 días")
        print("4. Próximos 30 días")
        
        periodo = input("👉 Opción (1-4): ").strip()
        
        if periodo == "1":
            dias = 1
        elif periodo == "2":
            dias = 7
        elif periodo == "3":
            dias = 15
        elif periodo == "4":
            dias = 30
        else:
            dias = 7
        
        print(f"\n🔍 Buscando huecos para los próximos {dias} días...")
        
        huecos = interfaz.buscar_huecos_disponibles(
        sala_numero=sala_numero, 
        duracion_horas=duracion, 
        dias_busqueda=dias
        )
        
        if huecos:
            print(f"\n✅ ¡ENCONTRADOS {len(huecos)} HORARIOS DISPONIBLES!")
            print("="*60)
            
            #Agrupar por fecha
            huecos_por_fecha = {}
            for hueco in huecos:
                fecha = hueco['fecha']
                if fecha not in huecos_por_fecha:
                    huecos_por_fecha[fecha] = []
                huecos_por_fecha[fecha].append(hueco)
            
            #Mostrar resultados
            for fecha, huecos_fecha in sorted(huecos_por_fecha.items()):
                print(f"\n📅 {fecha}:")
                for i, hueco in enumerate(huecos_fecha, 1):
                    print(f"   {i}. {hueco['hora_inicio']} - {hueco['hora_fin']} ({hueco['duracion']}h)")
            
            #Opcion para reservar
            print("\n" + "-"*40)
            print("¿Qué deseas hacer?")
            print("1. Reservar uno de estos horarios")
            print("2. Buscar en otra sala")
            print("3. Cambiar duración")
            print("4. Volver al menú")
            
            accion = input("👉 Opción: ").strip()
            
            if accion == "1":
                print("\n📝 Para reservar, vuelve al menú principal")
                print("   y selecciona 'Nueva Reserva' con los datos:")
                print(f"   • Sala: {sala_numero}")
                print(f"   • Duración: {duracion} horas")
                print(f"   • Fechas disponibles arriba")
                input("\n   Presiona Enter para continuar...")
            elif accion == "2":
                buscar_huecos(interfaz, duracion_predefinida=duracion)
            elif accion == "3":
                buscar_huecos(interfaz, sala_predefinida=sala_numero)
        else:
            print("\n😞 NO SE ENCONTRARON HORARIOS DISPONIBLES")
            print("\n💡 SUGERENCIAS:")
            print("   • Prueba con otra sala")
            print("   • Reduce la duración")
            print("   • Intenta con otra fecha")
            
            print("\n¿Buscar en otra sala? (s/n): ")
            if input().lower() == 's':
                buscar_huecos(interfaz)
    
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

def estado_salas(interfaz):
    """Mostrar estado y recursos de todas las salas"""
    print("\n" + "="*60)
    print("🏢 ESTADO Y RECURSOS DE TODAS LAS SALAS")
    print("="*60)
    
    
    for num, sala in interfaz.salas.items():
        print(f"\n📌 SALA {num}:")
       
      
        print(f"   Capacidad: {sala.capacidad} personas")
        print(f"Recursos disponibles : PS3, Juegos de Mesa, PS4, comida, PS5")
        
        
        
  
        reserva_activa = None
        for reserva_id, datos in List.items():
            if str(datos.get('Sala')) == str(num):
               
                inicio_str = datos.get('Inicio')
                if inicio_str:
                    inicio = datetime.strptime(inicio_str, "%Y-%m-%d %H:%M:%S")
                    fin = datetime.strptime(datos.get('Fin'), "%Y-%m-%d %H:%M:%S")
                    ahora = datetime.now()
                    if inicio <= ahora <= fin:
                        reserva_activa = datos
                        break
        
        if reserva_activa:
            print(f"   📅 Reserva activa:")
            print(f"      ID: {reserva_id}")
            print(f"      Descripción: {reserva_activa.get('Descripcion')}")
            print(f"      Horario: {reserva_activa.get('Inicio')} - {reserva_activa.get('Fin')}")
        estado_actual = Salas.Obtencion_estado(num, List)
        if estado_actual == "OCUPADA":
            print(f"   ⏳ Tiene reservas futuras")
        
    
    print("\n" + "="*60)
    print("📊 RESUMEN GENERAL:")
    
    disponibles = sum(1 for num in interfaz.salas.keys() if Salas.Obtencion_estado(num, List) == "DISPONIBLE")
    print(f"🟢 Salas disponibles: {disponibles}/5")
    print(f"🔴 Salas reservadas: {5 - disponibles}/5")
    
   
    
    print("\n📅 Horario de atencion: 08:00 - 17:00 (Lunes a Viernes)")
    print("="*60)

if __name__ == "__main__":
    main()
