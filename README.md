# Challenge 02: Optimización de Activos Críticos - TechLogistics S.A.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)


## Autores

Juan Pablo Rua, Pedro Saldarriaga, Juan Pablo Mejia

## 📋 Descripción del Proyecto

Proyecto de análisis avanzado de datos para optimización de infraestructura crítica en **TechLogistics S.A.** mediante técnicas de:
- 🗺️ Análisis geoespacial y visualización con Plotly
- 📈 Series temporales y pruebas de estacionariedad (ADF)
- 🎛️ Procesamiento de señales (FFT, filtros Butterworth)
- 🕸️ Teoría de grafos y análisis de redes (NetworkX)
- 🤖 Modelado predictivo (ARIMAX, Causalidad de Granger)

**Curso:** Análisis de Datos Avanzado  
**Docente:** Jorge Iván Padilla-Buriticá  
**Institución:** Universidad EAFIT  
**Periodo:** 2026-1  
**Fecha de entrega:** 07 de febrero de 2026

---

## 📂 Estructura del Proyecto

```
Taller3FundamentsoCD/
├── data/                          # Datasets del proyecto
│   ├── agro_clean.csv            # Datos agroclimáticos limpios
│   ├── agro_noise.csv            # Datos agroclimáticos con ruido
│   ├── ener_clean.csv            # Datos energéticos limpios
│   └── ener_noise.csv            # Datos energéticos con ruido (SNR 5-12dB)
├── notebooks/                     # Jupyter Notebooks
│   └── agro_visualization.ipynb  # Notebook principal del análisis
├── docs/                          # Documentación del proyecto
├── outputs/                       # Resultados, gráficos y reportes
├── generate_noise.py             # Script para generar datasets con ruido
├── .gitignore                    # Archivos ignorados por Git
├── LICENSE                       # Licencia MIT
└── README.md                     # Este archivo
```

---

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- (Opcional) Entorno virtual

### Dependencias Principales
```bash
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
plotly>=5.11.0
networkx>=2.8.0
scipy>=1.9.0
scikit-learn>=1.1.0
statsmodels>=0.13.0
```

### Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/Taller3FundamentsoCD.git
cd Taller3FundamentsoCD
```

2. **Crear entorno virtual (recomendado):**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias:**
```bash
pip install pandas numpy matplotlib seaborn plotly networkx scipy scikit-learn statsmodels jupyter
```

4. **Ejecutar Jupyter Notebook:**
```bash
jupyter notebook notebooks/agro_visualization.ipynb
```

---

## 📊 Descripción de los Datos

### Datasets Agroclimáticos (`agro_*.csv`)
- **Registros:** ~2000 observaciones
- **Variables:**
  - `Latitude`, `Longitude`: Coordenadas GPS de sensores
  - `Agro_1`: Humedad del suelo (%)
  - `Agro_3`: Temperatura ambiente (°C)
  - `Agro_5`: NDVI (Índice de vegetación normalizado)
  - `Agro_10`: Varianza del viento (proxy de pendiente/erosión)
  - `Source_Node`, `Target_Node`: Conexiones de red entre sensores

### Datasets Energéticos (`ener_*.csv`)
- **Registros:** ~2000 observaciones
- **Variables:**
  - `Ener_1`: Demanda energética (MW)
  - `Ener_4`: Generación eólica (MW)
  - `Ener_5`: Costo del gas natural ($/MMBTU)
  - `Ener_9`: Voltaje (kV)
  - `Ener_10`: Factor de potencia
  - `Source_Node`, `Target_Node`: Topología de subestaciones

---

## 🔬 Metodología (CRISP-DM)

### Fase 1: Comprensión de Datos y Geo-Visualización
✅ **Tarea 1.1:** Visualización geoespacial con `scatter_mapbox`  
✅ **Tarea 1.2:** Análisis de estacionariedad con Test ADF y ventanas móviles

### Fase 2: Procesamiento de Señales
✅ **Tarea 2.1:** Análisis espectral (FFT) y espectrogramas  
✅ **Tarea 2.2:** Filtrado Butterworth y cálculo de RMSE

### Fase 3: Análisis de Grafos
✅ **Tarea 3:** Construcción de red con NetworkX, cálculo de centralidad (Degree, Betweenness)

### Fase 4: Modelado y Toma de Decisiones
✅ **P1:** Test de Causalidad de Granger (Factor Potencia → Voltaje)  
✅ **P2:** Optimización geo-agrónoma (NDVI vs Varianza del Viento)  
✅ **P3:** Modelado ARIMAX con variables exógenas topológicas

---

## 📈 Resultados Principales

### Hallazgos Clave

1. **🗺️ Clustering Espacial:** Se identificaron zonas con biomasa baja (NDVI < umbral) correlacionadas con alta varianza de viento, indicando potencial erosión.

2. **📊 Estacionariedad:** El costo del gas (`Ener_5`) exhibe comportamiento de Random Walk con drift (p-valor ADF > 0.05), requiriendo diferenciación para modelado ARIMA.

3. **🎛️ Ruido Espectral:** El ruido inyectado (SNR 5-12dB) se distribuye uniformemente pero es dominante en frecuencias altas (>0.2), donde la señal original tiene menor energía.

4. **🕸️ Nodo Crítico:** Se identificó el nodo con mayor *Betweenness Centrality* como cuello de botella. Su fallo fragmentaría la red significativamente.

5. **🔗 Causalidad:** El Factor de Potencia causa (en sentido de Granger) al Voltaje (p < 0.05), confirmando que inestabilidades en potencia se propagan.

6. **🤖 Modelo Predictivo:** Incorporar centralidad del nodo mejoró el AIC del modelo ARIMAX para predicción de demanda energética.

---

## 🎯 Recomendaciones de Negocio

1. **Prioridad Alta:** Implementar redundancia eléctrica en el nodo identificado como cuello de botella.
2. **Infraestructura Agrícola:** Invertir en sistemas de irrigación en zonas con `Agro_10` alto (pendientes) y `Agro_5` bajo (NDVI).
3. **Monitoreo Predictivo:** Desplegar el modelo ARIMAX con información topológica para pronóstico de demanda.
4. **Calidad de Datos:** Aplicar filtrado Butterworth (cutoff=0.1) a sensores de humedad antes del modelado.

---

## 🛠️ Uso del Proyecto

### Generar Dataset con Ruido
```bash
python generate_noise.py
```

### Ejecutar Análisis Completo
1. Abrir `notebooks/agro_visualization.ipynb` en Jupyter
2. Ejecutar todas las celdas secuencialmente (`Shift + Enter`)
3. Los gráficos se mostrarán interactivamente

### Modificar Parámetros
- **SNR del ruido:** Editar `snr_target` en celdas de FFT
- **Ventana móvil:** Ajustar `window=50` en análisis de estacionariedad
- **Filtro Butterworth:** Cambiar `cutoff` y `order` en sección de filtrado

---

## 📚 Referencias

1. Granger, C. W. J. (1969). *Investigating Causal Relations by Econometric Models*. Econometrica.
2. Box, G. E. P., & Jenkins, G. M. (1976). *Time Series Analysis: Forecasting and Control*.
3. Newman, M. E. J. (2010). *Networks: An Introduction*. Oxford University Press.
4. Oppenheim, A. V. (1999). *Discrete-Time Signal Processing*. Prentice Hall.
5. Rouse Jr, J. W. et al. (1974). *Monitoring Vegetation Systems with NDVI*.

---

## ⚠️ Disclaimer

Este proyecto fue desarrollado con el apoyo de herramientas de inteligencia artificial, específicamente **Claude (Anthropic)**, para la estructuración del código, documentación técnica, y optimización de análisis de datos. El uso de IA como asistente de desarrollo permitió acelerar la implementación de técnicas avanzadas de ciencia de datos y garantizar mejores prácticas en la organización del proyecto.

La supervisión académica, validación de resultados, y decisiones metodológicas fueron realizadas por los estudiantes bajo la guía del profesor del curso.

---

