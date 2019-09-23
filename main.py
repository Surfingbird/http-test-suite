from myhttplib import Server

class Config:
    port = 8080

if __name__ == '__main__':
    port = Config.port
    server = Server(port)

    server.run()