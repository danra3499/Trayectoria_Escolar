from src import start_app
from config import config

configuration = config['development']
app = start_app(configuration)

if __name__ == '__main__':
    app.run()
