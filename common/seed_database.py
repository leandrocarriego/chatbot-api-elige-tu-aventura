from src.models import Node, Option


def seed_database(db):
    start_node = Node(description="Has comenzado un nuevo proyecto como desarrollador. Te enfrentas a una decisión importante sobre cómo proceder.")
    backend_django_node = Node(description="Tu aplicación Django está lista, pero necesitas elegir cómo desplegarla.")
    backend_flask_node = Node(description="Tu aplicación Flask está lista, pero necesitas elegir cómo desplegarla.")
    backend_php_node = Node(description="Tu aplicación PHP está lista, ahora debes desplegarla.")
    
    aws_deploy_node = Node(description="Tu aplicación se despliega con éxito en AWS, y se convierte en un gran éxito. Recibes ofertas de trabajo de las mejores empresas de tecnología.")
    heroku_deploy_node = Node(description="Tu aplicación se despliega en Heroku y se vuelve viral en las redes sociales. Todos quieren saber cómo la desarrollaste.")
    vps_deploy_node = Node(description="Tu aplicación se ha desplegado exitosamente en un VPS y ahora tienes más control.")
    php_deploy_node = Node(description="Después de muchas horas de lucha, logras que tu aplicación funcione. Pero al lanzarla, aparece un error que hace que toda la interfaz se vuelva color púrpura y tu mascota se convierte en un gato gigante. En un intento de arreglarlo, terminas hablando con el gato, que ahora cree que es el verdadero desarrollador. Al final, lo nombran CTO y tú te conviertes en su asistente.")

    db.session.add_all([start_node, backend_django_node, backend_flask_node, backend_php_node, aws_deploy_node, heroku_deploy_node, vps_deploy_node, php_deploy_node])
    db.session.commit()

    option_backend_django = Option(description="Usar Django para el backend", next_node_id=backend_django_node.id)
    option_backend_flask = Option(description="Usar Flask para el backend", next_node_id=backend_flask_node.id)
    option_backend_php = Option(description="Usar PHP para el backend", next_node_id=backend_php_node.id)

    option_deploy_aws = Option(description="Desplegar en AWS", next_node_id=aws_deploy_node.id)
    option_deploy_heroku = Option(description="Desplegar en Heroku", next_node_id=heroku_deploy_node.id)
    option_deploy_vps = Option(description="Desplegar en un VPS", next_node_id=vps_deploy_node.id)
    option_deploy_php = Option(description="Desplegar", next_node_id=php_deploy_node.id)

    start_node.options.append(option_backend_django)
    start_node.options.append(option_backend_flask)
    start_node.options.append(option_backend_php)

    backend_django_node.options.append(option_deploy_aws)
    backend_django_node.options.append(option_deploy_vps)

    backend_flask_node.options.append(option_deploy_aws)
    backend_flask_node.options.append(option_deploy_heroku)

    backend_php_node.options.append(option_deploy_php)
    
    db.session.add_all([option_backend_django, option_backend_flask, option_backend_php, option_deploy_aws, option_deploy_heroku, option_deploy_vps, option_deploy_php])

    db.session.commit()


