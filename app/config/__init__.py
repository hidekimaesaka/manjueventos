from dotenv import load_dotenv, dotenv_values

def start(app):

    load_dotenv()

    for key, value in dotenv_values().items():
        app.config[key] = value
