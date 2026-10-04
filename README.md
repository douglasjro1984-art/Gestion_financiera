# Gestión financiera

Trabajo práctico grupal (TP4, grupo **Los Tiburones**): sistema de gestión financiera con una API en Python y una interfaz web.

## Tecnologías

**Backend**
- Python y FastAPI
- Uvicorn, como servidor
- SQLAlchemy, para el acceso a la base de datos
- Pydantic, para validar los datos
- Autenticación con tokens (`python-jose`)
- Contraseñas cifradas con `passlib` y `bcrypt`
- `python-dotenv`, para manejar la configuración fuera del código

**Frontend:** HTML (`index.html`)

## Estructura

```
├── backend/
│   └── app/            # Código de la API
├── index.html          # Interfaz web
├── requirements.txt    # Dependencias de Python
└── .gitignore
```

## Cómo ejecutarlo en tu computadora

1. Cloná el repositorio. La rama principal es `grupos/LosTiburones`:

   ```bash
   git clone https://github.com/douglasjro1984-art/Gestion_financiera.git
   cd Gestion_financiera
   ```

2. Creá un entorno virtual e instalá las dependencias:

   ```bash
   python -m venv venv
   source venv/bin/activate        # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Creá un archivo `.env` con la configuración de la aplicación (conexión a la base de datos y clave secreta para los tokens).

4. Iniciá la API desde la carpeta `backend`:

   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

5. FastAPI genera la documentación interactiva de la API en http://127.0.0.1:8000/docs

6. Abrí `index.html` en el navegador para usar la interfaz.

## Autor

**Douglas Romero**, desarrollador backend junior. Trabajo realizado en grupo.
[GitHub](https://github.com/douglasjro1984-art) · [LinkedIn](https://www.linkedin.com/in/douglas-romero-574576384)
