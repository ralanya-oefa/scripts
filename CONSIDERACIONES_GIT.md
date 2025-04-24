# GIT Y GITLAB FOR CSEP
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

## GitLab for R

### Pasos para configuración
- Instalación de Git en el equipo local
- Generación de cuenta en GitLab
- Crear un proyecto de R Studio donde se generara el archivo .Rproj
- Ejecutar en el R Scripts los comandos para instalar e inicializar git.
- Generar los scripts o archivos en el proyecto.
- Generar el token de la cuenta gitlab.
- Realizar push con el código.

### Configuración adicional del use this en R Studio
- Crear un token personal en GitLab.
- Guardar el token para R.
- Iniciar nuevo proyecto o existente.
- Realizar autenticación al hacer push.

### Comandos de apoyo
|      Comando     |    Descripción   |
| ---------------- | ---------------- |
| system("git --version") | Verifica la versión instalada de R, ejecutarse en el terminal de R Studio
| use_git() | Ejecutar en el R Script para inicializar git |
| usethis::use_github() | Subir los cambios al github o gitlab |
| gert::git_branch() | Ver las ramas existentes |

### Bibliografía
- Git y GitHub con R. Enlace: https://rpubs.com/RonaldoAnticona/818156
- This tutorial teaches you to create R Markdown documents with RStudio and publish them via GitHub, using GitHub Pages. Enlace: https://resources.github.com/github-and-rstudio/
- Capítulo 4 git con RStudio y GitLab. Enlace: https://vickysteeves.gitlab.io/repro-papers/git.html
- Guía para configurar GitLab con RStudio (Enrico Tips). Enlace: https://www.enricotips.com/post/setup-gitlab-with-rstudio
- Happy Git with R – Integración de RStudio con Git. Enlace: https://happygitwithr.com/rstudio-git-github.html
- Usar RStudio con Git y repositorios remotos como GitLab (WORCS). Enlace: https://cloud.r-project.org/web/packages/worcs/vignettes/git_cloud.html
- Tutorial completo para usar Git y GitLab con RStudio (Matthieu Bruneaux). Enlace: https://matthieu-bruneaux.gitlab.io/guide-r-rstudio-git-gitlab/030-setting-up-gitlab-repo.html
- Git con RStudio y GitLab – Reproducible Research Papers (Vicky Steeves). Enlace: https://vickysteeves.gitlab.io/repro-papers/git.html

## GitLab for Python
### Pasos para configuración
- Instalación de Git en el equipo local.
- Generación de cuenta en GitLab.
- Asignar o crear una carpeta para la ubicación de los scripts.
- Iniciar git en la carpeta elegida o clone el proyecto existente en el GitLab.
- Abrir el proyecto en Visual Studio Code.
- Utilizar o generar la rama asignada al usuario.
- Realizar el push o pull al repositorio.

### Comandos de apoyo
| Comando | Descripción |
| --------|-------------|
| git clone "https:..." | Comando para realizar la clonación de proyecto guardado en el repositorio GitLab |
| git status | Comando para revisar los archivos argregar al stage actual |
| git add . | Comando para agregar los cambios en el proyecto |
| git commit -m "..." | Comando para realizar un commit al proyecto |
| git remote add origin https://.... | Comando para agrenda el https remote al proyecto local |
| git branch -M main | Comando para cambiar la rama a main |
| git push origin -u main | Comando para subir o publicar los cambios desde la rama main |

### Bibliografía
- Configuración de un proyecto de Python para GitHub Codespaces. Enlace: https://docs.github.com/es/enterprise-cloud@latest/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces
- Documentación oficial de python-gitlab. Enlace: https://python-gitlab.readthedocs.io/​
- Ejemplos de uso de la API. Enlace: https://python-gitlab.readthedocs.io/en/stable/api-objects.html​
- Tutorial de Pierian Training. Enlace: https://pieriantraining.com/using-gitlab-python-api-a-tutorial-for-beginners/​
- Guía práctica de GitLab sobre automatización con python-gitlab. Enlace: https://about.gitlab.com/blog/2023/02/01/efficient-devsecops-workflows-hands-on-python-gitlab-api-automation/​
- Repositorio de ejemplos en GitLab. Enlace: https://gitlab.com/gitlab-da/use-cases/gitlab-api/gitlab-api-python

## GitLab for SQL

### Pasos para configuración
- Instalación de Git en el equipo local.
- Generación de cuenta en GitLab.
- Asignar o crear una carpeta para la ubicación de los scripts.
- Iniciar git en la carpeta elegida o clone el proyecto existente en el GitLab.
- Abrir el proyecto en Visual Studio Code.
- Utilizar o generar la rama asignada al usuario.
- Realizar el push o pull al repositorio.

### Comandos de apoyo
| Comando | Descripción |
| --------|-------------|
| git clone "https:..." | Comando para realizar la clonación de proyecto guardado en el repositorio GitLab |
| git status | Comando para revisar los archivos argregar al stage actual |
| git add . | Comando para agregar los cambios en el proyecto |
| git commit -m "..." | Comando para realizar un commit al proyecto |
| git remote add origin https://.... | Comando para agrenda el https remote al proyecto local |
| git branch -M main | Comando para cambiar la rama a main |
| git push origin -u main | Comando para subir o publicar los cambios desde la rama main |

### Bibliografía
- Cómo Integrar Scripts SQL de GitHub en tu Base de Datos SQL Server. Enlace: https://www.youtube.com/watch?v=feLhnvvPbd8
- Guía paso a paso para vincular una base de datos SQL Server a un repositorio de GitLab. Enlace: https://docs.devart.com/studio-for-sql-server/source-controlling-databases/linking-db-to-git-repository-in-gitlab.html
- Automatización de cambios en bases de datos con SQL Change Automation y GitLab CI/CD. Enlace: https://plantbasedsql.com/2020/09/08/sql-change-automation-and-gitlab-ci-cd-a-k-a-oh-this-is-fun-on-windows/
- Mejores prácticas de CI/CD para bases de datos con GitLab. Enlace: https://www.bytebase.com/docs/tutorials/database-cicd-best-practice-with-gitlab/
- Integración de GitLab y Microsoft SQL con n8n. Enlace: https://n8n.io/integrations/gitlab/and/microsoft-sql/
- Guía de consultas SQL en GitLab. Enlace: https://docs.gitlab.com/development/sql/

## Automatizar la ejecución de script de Git

### Pasos para la ejecución
- Agregar las líneas de comando de git en un archivo bash.
- Configurar el archivo bash desde la programación de tareas.
- Programar la ejecución de los archivos bash. 

### Consideraciones
- Los cambios realizado en el equipo debe ser realizado en la rama del usuario o colaborador para el posterior push en el repostorio.