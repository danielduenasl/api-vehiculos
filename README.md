# API de Vehículos

API REST hecha con Django REST Framework y MySQL para el examen final de Desarrollo Web.

## Cómo correrlo

1. Crear la base de datos `api_vehiculos` en MySQL (phpMyAdmin).
2. Doble clic en `iniciar.bat` (crea el entorno, instala, migra y levanta el servidor).
3. Abrir http://127.0.0.1:8000/api/vehiculos/

## Endpoints

| Método | URL | Acción |
| --- | --- | --- |
| GET | /api/vehiculos/ | Listar |
| POST | /api/vehiculos/ | Crear |
| GET | /api/vehiculos/{id}/ | Consultar por id |
| PUT | /api/vehiculos/{id}/ | Actualizar |
| DELETE | /api/vehiculos/{id}/ | Eliminar |
