from flasgger import Swagger, LazyString
from flasgger import swag_from



swagger_template ={
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
      "basePath":"http://localhost:5000",

              },
    "schemes": [
        "http",
        "https"
    ],
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
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/",
}
