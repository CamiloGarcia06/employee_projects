# Employee Projects Module

Descripción

El módulo Employee Projects permite gestionar proyectos de empleados dentro de Odoo 16. Amplía las funcionalidades del módulo de Recursos Humanos (hr) y ofrece una experiencia intuitiva para la gestión de proyectos tanto en el backend como en el portal de empleados.
Requisitos Previos

    Versión de Odoo: Odoo 16 CE
    Dependencias:
        base
        hr
        portal
        website

Instalación

    Clonar o descargar el módulo: git clone https://github.com/CamiloGarcia06/employee_projects

Copiar el módulo en la carpeta custom-addons:

    cp -r employee_projects /ruta/a/custom-addons/

    Reiniciar el servidor Odoo.
    Actualizar la lista de aplicaciones desde el menú Apps.
    Instalar el módulo Employee Projects.

Configuración

    No se requieren comandos ni configuraciones adicionales.
    Los permisos se heredan del grupo Officer: Manage all employees del módulo de empleados.

Uso del Módulo
Acceso desde Backend:

    Navegar a Employees > Employee Projects > Projects.
    Crear, editar y visualizar proyectos de empleados.

Acceso desde el Portal:

    Acceder al menú My Projects.
    Hacer clic en el nombre del proyecto para ver los detalles.

Visualización del Campo Total Projects:

    Navegar a un empleado desde Employees.
    En la pestaña Private Information, visualizar el campo Total Projects al final del formulario.

Funcionalidades Principales

    Gestión de Proyectos:
        Crear, editar y listar proyectos en el backend.
    Vistas del Portal:
        Los empleados pueden ver y acceder a sus proyectos desde el portal.
    Campo Calculado:
        El campo Total Projects en el modelo hr.employee muestra la cantidad de proyectos asignados.

Capturas de Pantalla:
![image](https://github.com/user-attachments/assets/a67e0aa0-188f-4519-8fb4-50e4e25b55d0)
![image](https://github.com/user-attachments/assets/1f33de5a-15c9-45f5-a3b4-726ff03c3acc)
![image](https://github.com/user-attachments/assets/5d521805-77f3-481f-a9ca-9d642b12950d)
![image](https://github.com/user-attachments/assets/7760e4a8-d8d1-4534-811f-ac24c699909b)
![image](https://github.com/user-attachments/assets/1c5bfec6-aa31-4025-b89e-9e3f17a5e64e)

Backend:

Portal:
Estructura del Módulo

    employee_projects/
    │
    ├── controllers/
    │   └── portal.py        # Controlador del portal
    │
    ├── models/
    │   └── employee_project.py   # Modelo 'employee.project'
    │
    ├── views/
    │   ├── employee_project_views.xml  # Vistas backend
    │   ├── portal_project_templates.xml # Vistas portal
    │
    └── __manifest__.py      # Archivo de manifiesto
    
Contacto

    Nombre: Juan Camilo Sandoval Garcia
    Correo: juancasangar@hotmail.com
    Teléfono: +57 3115820195

Licencia

Este módulo no especifica una licencia.
