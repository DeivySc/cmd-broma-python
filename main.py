import time
import random

def fake_loading():
    print("Iniciando análisis de compatibilidad...🔍")
    for i in range(1, 101):
        print(f"Cargando... {i}%", end="\r")
        time.sleep(random.uniform(0.01, 0.1))  # Simula una carga lenta
    print("\nAnálisis completado ✅")

def compatibility_analysis():
    fake_loading()
    print("Resultado del análisis:")
    time.sleep(1)
    print("Ella no te ama... 😂 Pero el código sí.")

# Ejecuta el análisis
compatibility_analysis()
