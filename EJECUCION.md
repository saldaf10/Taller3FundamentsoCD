# INSTRUCCIONES DE EJECUCIÓN
## Challenge 02: Optimización de Activos Críticos

### 1. Configuración Inicial

```bash
# Clonar repositorio
git clone <tu-repo-url>
cd Taller3FundamentsoCD

# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Activar entorno (Linux/Mac)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Verificar Datos

Los datasets ya están incluidos en `data/`:
- `agro_clean.csv` - Sensores agroclimáticos limpios
- `agro_noise.csv` - Con ruido inyectado
- `ener_clean.csv` - Series energéticas limpias
- `ener_noise.csv` - Con ruido inyectado (SNR 5-12dB)

Si necesitas regenerar `ener_noise.csv`:
```bash
python generate_noise.py
```

### 3. Ejecutar Análisis

#### Opción A: Jupyter Notebook (Recomendado)
```bash
jupyter notebook notebooks/agro_visualization.ipynb
```

Luego:
1. Ejecuta todas las celdas: `Cell → Run All`
2. Los gráficos aparecerán interactivos
3. Guarda outputs si es necesario

#### Opción B: Desde Python Script
```python
# Si necesitas ejecutar programáticamente
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

with open('notebooks/agro_visualization.ipynb') as f:
    nb = nbformat.read(f, as_version=4)
    
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})
```

### 4. Generar PDF del Informe

El informe técnico está en `docs/INFORME_TECNICO.md`

#### Opción A: Con Pandoc (recomendado)
```bash
# Requiere pandoc instalado
pandoc docs/INFORME_TECNICO.md -o docs/INFORME_TECNICO.pdf --pdf-engine=xelatex
```

#### Opción B: Herramientas Online
1. Abrir `docs/INFORME_TECNICO.md` en VS Code
2. Instalar extensión "Markdown PDF"
3. Clic derecho → "Markdown PDF: Export (pdf)"

#### Opción C: Con Grip (preview online)
```bash
pip install grip
grip docs/INFORME_TECNICO.md
# Abrir http://localhost:6419 y "Imprimir a PDF" desde navegador
```

### 5. Estructura de Outputs

Los gráficos generados se guardarán automáticamente en:
```
outputs/
├── geo_map.png
├── windowing_ener5.png
├── fft_comparison.png
├── spectrogram_comparison.png
├── butterworth_filtering.png
├── network_graph.png
└── wind_ndvi_correlation.png
```

### 6. Troubleshooting

**Problema:** Plotly no muestra mapas interactivos
```bash
# Instalar extensión de Jupyter
jupyter labextension install jupyterlab-plotly
```

**Problema:** Errores de path en CSV
- Asegúrate de ejecutar desde la raíz del proyecto
- Las rutas en el notebook son relativas: `../data/`

**Problema:** Kernel muere en FFT
- La FFT es intensiva en memoria
- Reduce el tamaño de muestra en la celda correspondiente

**Problema:** NetworkX no dibuja el grafo
```bash
# Instalar matplotlib backend
pip install --upgrade matplotlib
```

### 7. Notas Importantes

- **Tiempo de ejecución:** ~5-10 minutos (depende del hardware)
- **Memoria requerida:** Mínimo 4GB RAM
- **Python version:** 3.8 o superior
- **Kernel recomendado:** Python 3 (ipykernel)

### 8. Contacto

Para dudas o problemas:
- Revisar issues en GitHub
- Email: tu-email@eafit.edu.co
