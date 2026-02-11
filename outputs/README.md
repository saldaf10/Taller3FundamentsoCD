# Outputs / Resultados

Esta carpeta contendrá los gráficos y visualizaciones generados al ejecutar el notebook.

## Archivos que se generarán:

Al ejecutar `notebooks/agro_visualization.ipynb` completamente, se generarán los siguientes outputs (si se configuran para guardarse):

### Fase 1: Geo-Visualización
- `geo_map.html` o `geo_map.png` - Mapa interactivo de sensores

### Fase 1: Series Temporales
- `windowing_ener5.png` - Análisis de ventanas móviles del costo del gas

### Fase 2: Procesamiento de Señales
- `fft_comparison.png` - Comparación de densidad espectral
- `spectrogram_comparison.png` - Espectrogramas clean vs noise
- `butterworth_filtering.png` - Resultado del filtrado

### Fase 3: Grafos
- `network_graph.png` - Topología de la red de sensores

### Fase 4: Modelado
- `wind_ndvi_correlation.png` - Scatterplot viento vs NDVI
- `granger_results.txt` - Resultados del test de Granger (opcional)

## Nota:

Por defecto, el notebook genera los gráficos interactivos en el navegador. Para guardar las imágenes en esta carpeta, puedes añadir al final de cada celda de visualización:

```python
# Para matplotlib/seaborn
plt.savefig('../outputs/nombre_archivo.png', dpi=300, bbox_inches='tight')

# Para plotly
fig.write_html('../outputs/nombre_archivo.html')
fig.write_image('../outputs/nombre_archivo.png')  # Requiere kaleido
```

## Instrucciones para Plotly:

Si deseas exportar gráficos de Plotly a PNG:
```bash
pip install kaleido
```
