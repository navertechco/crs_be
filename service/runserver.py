import os 
from src import app 
from werkzeug.serving import WSGIRequestHandler
WSGIRequestHandler.protocol_version = "HTTP/1.1"



def main():
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
        HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
        print("HOST: ",HOST)
        print("PORT: ",str(PORT))
        print("HOST: ",HOST)
        print("PORT: ",str(PORT))
        SECRET_KEY = os.urandom(32)
        app.config['SECRET_KEY'] = SECRET_KEY
        app.run(host=HOST, port=PORT)
    except Exception as error:
        print(error)      



if __name__ == '__main__': 
    main()
        

