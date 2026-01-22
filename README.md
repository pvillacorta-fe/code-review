# Code Review Exercise

API de gestión de usuarios con FastAPI y SQLAlchemy.

## Estructura

```
├── README.md
├── requirements.txt
└── src/
    ├── main.py              # Entry point FastAPI
    ├── database.py          # Configuración BD
    ├── models/
    │   └── models.py        # Modelo User
    ├── routers/
    │   └── users.py         # Endpoints de usuarios
    └── services/
        └── user_service.py  # Lógica de negocio
```

## Endpoints

- `GET /users/` - Listar usuarios
- `GET /users/search` - Buscar usuarios
- `GET /users/{id}` - Obtener usuario
- `POST /users/` - Crear usuario
