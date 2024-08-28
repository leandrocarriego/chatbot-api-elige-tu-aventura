from src import create_app, run_server


if __name__ == "__main__":
    app = create_app()
    run_server(app)
