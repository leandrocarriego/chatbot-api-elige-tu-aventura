swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Chatbot 'Elige tu propia aventura'",
        "description": "API Documentation for 'Elige tu propia aventura' Chatbot",
        "contact": {
            "name": "Admin",
            "email": "leandrocarriego@hotmail.com",
            "url": "https://www.linkedin.com/in/leandro-carriego/",
        },
        "version": "1.0",
        "basePath": "/api/v1",
    },
    "schemes": ["http", "https"],
}

swagger_config = {
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST"),
    ],
    "specs": [
        {
            "endpoint": 'api_spec',
            "route": '/api_spec.json',
        },
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/",
}
