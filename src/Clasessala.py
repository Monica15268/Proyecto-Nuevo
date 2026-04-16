from datetime import timedelta, datetime
from collections import Counter
from FuncionesEspecificas import List
Recurses_inventary = {
    'PS5' : 3,
    'PS3' : 1,
    'PS4' : 3,
    'Comida' : 5,
    'Licores' : 3,
    'Bocinas' : 2,
    'Juegos de Mesa' : 1



}
class Salas :
    def __init__(self, capacidad,numero) :
        self.capacity = capacidad
        self.num = numero
        self.inventario = Recurses_inventary.copy()
   




    @staticmethod
    def Obtencion_estado(sala_numero, reserves_lists):
       
        now_hour = datetime.now()
        for reserve in reserves_lists.values():
            if str(reserve.get('Sala')) == str(sala_numero):
                try:
                    inicio = datetime.strptime(reserve['Inicio'], "%Y-%m-%d %H:%M:%S")
                    end = datetime.strptime(reserve['Fin'], "%Y-%m-%d %H:%M:%S")
                    if inicio <= now_hour <= end:
                        return "OCUPADA"
                except:
                    continue
        return "DISPONIBLE"
   
    @staticmethod
    def window_inventary():
       
        from FuncionesEspecificas import obtener_recursos_ocupados_en_horario
       
        
        now = datetime.now()
        not_disponibles_recurses = obtener_recursos_ocupados_en_horario(now, 0)
        
        print("\n📦 INVENTARIO DE RECURSOS:")
        print("="*50)
        
        for recurse, cantidad_total in Recurses_inventary.items():
            cantidad_ocupada = len(not_disponibles_recurses.get(recurse, []))
            cantidad_disponible = cantidad_total - cantidad_ocupada
            
            state = "🟢" if cantidad_disponible > 0 else "🔴"
            print(f"{state} {recurse}:")
            print(f"   Total: {cantidad_total}")
            print(f"   Ocupados: {cantidad_ocupada}")
            print(f"   Disponibles: {cantidad_disponible}")
            
            if cantidad_ocupada > 0:
               print(f"   En uso en: {', '.join([f'Sala {u["sala"]}' for u in not_disponibles_recurses.get(recurse, [])])}")
        
        print("="*50)
        return Recurses_inventary




    @staticmethod
    def verify_disponibility(recursos_solicitados, fecha_hora, duracion_horas):
       
        from collections import Counter
        from FuncionesEspecificas import obtener_recursos_ocupados_en_horario
        
        ocupated_recurses = obtener_recursos_ocupados_en_horario(fecha_hora, duracion_horas)
        
        ocupated_counter = Counter()
        for recurse, usos in ocupated_recurses.items():
            ocupated_counter [recurse] = len(usos)
        
        recursos_solicitados_counter = Counter(recursos_solicitados)
        
        for recurse, cantidad_solicitada in recursos_solicitados_counter.items():
            cantidad_total = Recurses_inventary.get(recurse, 0)
            cantidad_ocupada = ocupated_counter.get(recurse, 0)
            cantidad_disponible = cantidad_total - cantidad_ocupada
            
            if cantidad_solicitada > cantidad_disponible:
                return False, f"❌ No hay suficiente {recurse}. Disponibles: {cantidad_disponible}, Solicitados: {cantidad_solicitada}"
        
        return True, "✅ Inventario disponible"



    @staticmethod
    def compatibility_verification(solicited_recurses) :

        if isinstance(solicited_recurses, str):
            solicited_recurses = [solicited_recurses]
        
        recursos_dict = {recurso : True for recurso in solicited_recurses}
        consoles = ['PS5', 'PS3', 'PS4']
        disponibles_consoles = [c for c in consoles if c in solicited_recurses]
        if len(disponibles_consoles) > 1 :
            return False, "No se puede tener mas de un tipo de consola a la vez"
        
        if 'Comida' in recursos_dict:
            for console in consoles:
                if console in recursos_dict:
                    return False, f"❌ La comida no es compatible con {console}"
        if 'Licores' in recursos_dict:
            for console in consoles:
                if console in recursos_dict:
                    return False, f"❌ Los licores no son compatibles con {console}"
            if 'Juegos de Mesa' in recursos_dict:
                return False, "❌ Los licores no son compatibles con juegos de mesa"
        if 'Juegos de Mesa' in recursos_dict:
            if 'Comida' not in recursos_dict:
                return False, "❌ Los juegos de mesa requieren Comida"
            if 'Bocinas' not in recursos_dict:
                return False, "❌ Los juegos de mesa requieren bocinas"
        
        
        if any(consola in recursos_dict for consola in consoles):
            if 'Bocinas' not in recursos_dict:
                return False, "❌ Las consolas requieren bocinas"
        
        return True, "✅ Recursos compatibles"    

    
   
   
        
one_room = Salas(10,  1,)
two_room = Salas(20,  2, )
three_room = Salas(5,   3, )
four_room = Salas(7,   4, )
five_room = Salas(15,  5,)
  
        
    
        
    
        