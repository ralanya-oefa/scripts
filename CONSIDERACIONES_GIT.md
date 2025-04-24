# GIT Y GITHUB FOR CSEP
<img src="https://pifa.oefa.gob.pe/mfiscamb/images/oefa-logo-header.png" alt="Logo de OpenAI" width="40%" height="40%">

## Estructura de carpetas
- Nivel 1: Carpeta principal
- Nivel 2: Carpeta del Proyecto | Equipo | Área (En caso existe sub carpetas se considera en la estructura)
- Nivel 3: Carpeta de tipo de script: R, python, sql
- Nivel 4: Archivo del script

## Herramientas
- R Studio para scripts en R
- Visual Studio Code para Python
- Visual Studio Code o Git Bash para Sql

## GITHUB FOR R

### Pasos para configuración
- Instalación de Git en el equipo local
- Generación de cuenta en GitHub
- Crear un proyecto de R Studio donde se generara el archivo .Rproj
- Ejecutar en el R Scripts los comandos para instalar e inicializar git.
- Generar los scripts o archivos en el proyecto.
- Generar el token de la cuenta github.
- Realizar push con el código.

### Comandos de apoyo
|      Comando     |    Descripción   |
| ---------------- | ---------------- |
| system("git --version") | Verifica la versión instalada de R, ejecutarse en el terminal de R Studio
| use_git() | Ejecutar en el R Script para inicializar git |
| usethis::use_github() | Subir los cambios al github |
| gert::git_branch() | Ver las ramas existentes |

### Bibliografía
- Git y GitHub con R. Enlace: https://rpubs.com/RonaldoAnticona/818156
- This tutorial teaches you to create R Markdown documents with RStudio and publish them via GitHub, using GitHub Pages. Enlace: https://resources.github.com/github-and-rstudio/

## GITHUB FOR PYTHON
### Pasos para configuración
- Instalación de Git en el equipo local
- Generación de cuenta en GitHub
- Asignar o crear una carpeta para la ubicación de los scripts
- Iniciarla git en la carpeta elegida.
- 

### Comandos de apoyo

### Bibliografía
- https://docs.github.com/es/enterprise-cloud@latest/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces

## GITHUB FOR SQL
### Pasos para configuración

### Comandos de apoyo

### Bibliografía
- https://www.youtube.com/watch?v=feLhnvvPbd8

## Automatizar la ejecución de script de Git

### Pasos para la ejecución

### Consideraciones
- Los cambios realizado en el equipo debe ser realizado en la rama del usuario o colaborador para el posterior push en el repostorio.