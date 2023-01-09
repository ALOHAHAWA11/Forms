from logger import init_logger
from web_handler import SocketServer

if __name__ == '__main__':
    init_logger()
    SocketServer.run_server()

