"""
Script de verificación del proyecto
Valida que todos los componentes estén presentes antes de la entrega
"""
import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Verifica si un archivo existe"""
    exists = os.path.exists(filepath)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {filepath}")
    return exists

def check_folder_exists(folder, description):
    """Verifica si una carpeta existe"""
    exists = os.path.isdir(folder)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {folder}")
    return exists

def main():
    print("="*60)
    print("VERIFICACIÓN DE COMPLETITUD DEL PROYECTO")
    print("Challenge 02: TechLogistics S.A.")
    print("="*60)
    
    checks = []
    
    # 1. Estructura de carpetas
    print("\n[1/6] Estructura de Carpetas")
    print("-" * 60)
    checks.append(check_folder_exists("data", "Carpeta de datos"))
    checks.append(check_folder_exists("notebooks", "Carpeta de notebooks"))
    checks.append(check_folder_exists("docs", "Carpeta de documentación"))
    checks.append(check_folder_exists("outputs", "Carpeta de outputs"))
    
    # 2. Datasets
    print("\n[2/6] Datasets Requeridos")
    print("-" * 60)
    checks.append(check_file_exists("data/agro_clean.csv", "Datos agro limpios"))
    checks.append(check_file_exists("data/agro_noise.csv", "Datos agro con ruido"))
    checks.append(check_file_exists("data/ener_clean.csv", "Datos energía limpios"))
    checks.append(check_file_exists("data/ener_noise.csv", "Datos energía con ruido"))
    
    # 3. Notebooks
    print("\n[3/6] Jupyter Notebooks")
    print("-" * 60)
    checks.append(check_file_exists("notebooks/agro_visualization.ipynb", "Notebook principal"))
    
    # 4. Documentación
    print("\n[4/6] Documentación")
    print("-" * 60)
    checks.append(check_file_exists("README.md", "README principal"))
    checks.append(check_file_exists("docs/INFORME_TECNICO.md", "Informe técnico"))
    checks.append(check_file_exists("EJECUCION.md", "Instrucciones de ejecución"))
    
    # 5. Archivos de configuración
    print("\n[5/6] Configuración del Proyecto")
    print("-" * 60)
    checks.append(check_file_exists(".gitignore", "Archivo .gitignore"))
    checks.append(check_file_exists("LICENSE", "Archivo de licencia"))
    checks.append(check_file_exists("requirements.txt", "Dependencias Python"))
    
    # 6. Scripts
    print("\n[6/6] Scripts Auxiliares")
    print("-" * 60)
    checks.append(check_file_exists("generate_noise.py", "Generador de ruido"))
    
    # Resumen
    print("\n" + "="*60)
    total_checks = len(checks)
    passed_checks = sum(checks)
    percentage = (passed_checks / total_checks) * 100
    
    print(f"RESULTADO: {passed_checks}/{total_checks} verificaciones pasadas ({percentage:.1f}%)")
    
    if percentage == 100:
        print("✓ ¡Proyecto completo y listo para entrega!")
    elif percentage >= 90:
        print("⚠ Proyecto casi completo. Revisar ítems faltantes.")
    else:
        print("✗ Proyecto incompleto. Completar ítems faltantes antes de entregar.")
    
    print("="*60)
    
    # Verificación adicional de Git
    print("\n[BONUS] Verificación de Git")
    print("-" * 60)
    
    import subprocess
    try:
        # Contar commits
        result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], 
                              capture_output=True, text=True, check=True)
        commit_count = int(result.stdout.strip())
        
        if commit_count >= 10:
            print(f"✓ Commits: {commit_count} (mínimo 10 requerido)")
        else:
            print(f"✗ Commits: {commit_count} (se requieren al menos 10)")
            
        # Verificar si hay cambios sin commit
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        
        if result.stdout.strip():
            print("⚠ Hay cambios sin commitear:")
            print(result.stdout)
        else:
            print("✓ No hay cambios pendientes")
            
    except subprocess.CalledProcessError:
        print("⚠ No se pudo verificar información de Git")
    except FileNotFoundError:
        print("⚠ Git no está instalado o no está en PATH")
    
    print("="*60)
    
    return 0 if percentage == 100 else 1

if __name__ == "__main__":
    sys.exit(main())
