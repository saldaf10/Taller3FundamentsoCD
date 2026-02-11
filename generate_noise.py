"""
Script para generar ener_noise.csv a partir de ener_clean.csv
Agrega ruido gaussiano con SNR entre 5-12 dB a las columnas de energía
"""
import pandas as pd
import numpy as np

def add_noise_to_column(signal, snr_db):
    """Agrega ruido gaussiano a una señal con SNR específico"""
    sig_power = np.mean(signal**2)
    snr_linear = 10**(snr_db / 10)
    noise_power = sig_power / snr_linear
    noise = np.random.normal(0, np.sqrt(noise_power), len(signal))
    return signal + noise

# Cargar datos limpios
df_clean = pd.read_csv('data/ener_clean.csv')

# Crear copia para agregar ruido
df_noise = df_clean.copy()

# Identificar columnas de energía (Ener_1 a Ener_10)
ener_cols = [col for col in df_clean.columns if col.startswith('Ener_')]

# Agregar ruido a cada columna de energía con SNR aleatorio entre 5-12 dB
np.random.seed(42)  # Para reproducibilidad
for col in ener_cols:
    snr_db = np.random.uniform(5, 12)
    df_noise[col] = add_noise_to_column(df_clean[col].values, snr_db)
    print(f"{col}: SNR = {snr_db:.2f} dB")

# Guardar archivo con ruido
df_noise.to_csv('data/ener_noise.csv', index=False)
print(f"\n✓ Archivo 'data/ener_noise.csv' generado exitosamente")
print(f"  - Registros: {len(df_noise)}")
print(f"  - Columnas con ruido: {len(ener_cols)}")
