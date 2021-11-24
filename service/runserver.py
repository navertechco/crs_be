from os import environ
from src.INFRA.WEB.App.routes import app 


if __name__ == '__main__': 

    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
        HOST = environ.get('SERVER_HOST', 'localhost')
        print("HOST: "+HOST)
        print("PORT: "+str(PORT))
    except ValueError:
        PORT = 5002
        HOST = "172.0.0.1"
        print("HOST: "+HOST)
        print("PORT: "+str(PORT))        
        
    print("HOST: "+HOST)
    print("PORT: "+str(PORT))
    app.run(host=HOST, port=PORT)
