import threading
import time
import random

# Simulación de los servicios de la plataforma de streaming

def servicio_transmision():
    print("[Bulkhead Transmisión] Iniciando transmisión de video...")
    time.sleep(random.uniform(2, 5))  # Simula tiempo de procesamiento
    print("[Bulkhead Transmisión] Transmisión de video completada.")

def servicio_recomendaciones():
    print("[Bulkhead Recomendaciones] Generando recomendaciones...")
    time.sleep(random.uniform(1, 4))  # Simula tiempo de procesamiento
    print("[Bulkhead Recomendaciones] Recomendaciones generadas.")

def servicio_gestion_usuarios():
    print("[Bulkhead Gestión de Usuarios] Actualizando preferencias de usuario...")
    time.sleep(random.uniform(1, 3))  # Simula tiempo de procesamiento
    print("[Bulkhead Gestión de Usuarios] Preferencias de usuario actualizadas.")

# Definir los bulkheads como hilos independientes
def bulkhead_servicios():
    # Crear hilos para cada servicio
    bulkhead_transmision = threading.Thread(target=servicio_transmision)
    bulkhead_recomendaciones = threading.Thread(target=servicio_recomendaciones)
    bulkhead_gestion = threading.Thread(target=servicio_gestion_usuarios)

    # Iniciar los hilos
    bulkhead_transmision.start()
    bulkhead_recomendaciones.start()
    bulkhead_gestion.start()

    # Esperar a que cada hilo complete su ejecución
    bulkhead_transmision.join()
    bulkhead_recomendaciones.join()
    bulkhead_gestion.join()

if __name__ == "__main__":
    print("Iniciando demo del patrón Bulkhead para plataforma de streaming...\n")
    bulkhead_servicios()
    print("\nDemo completada.")
