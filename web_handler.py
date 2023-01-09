import logging
import socket
import urllib.parse
from database_handler import DatabaseHandler
from config import HOST, PORT
from const import URLS
from request_parser import RequestHandler


class SocketServer:
    @staticmethod
    def form_content(status_code, url, data):
        logging.info('Form content')
        if status_code == 404:
            return '<h1>Not found</h1>'
        if status_code == 405:
            return '<h1>Method not allowed</h1>'
        URLS[url] = str(data)
        return URLS[url]

    @staticmethod
    def form_headers(method, url):
        if not method == 'POST':
            return 'HTTP/1.1 405 Method not allowed\n\n', 405
        if not url in URLS:
            return 'HTTP/1.1 404 Not found\n\n', 404
        return 'HTTP/1.1 200 OK\n\n', 200

    @staticmethod
    def unpack_request(request):
        request_string = request.split(' ')
        method = request_string[0]
        params = request_string[1].split('?')[1]
        url = request_string[1].split('?')[0]
        params = urllib.parse.unquote_plus(params, 'utf-8', 'replace')
        logging.info('Success unpacking')
        return method, url, params

    @staticmethod
    def form_response(request):
        logging.info('Unpacking of received data')
        method, url, params = SocketServer.unpack_request(request)
        logging.info('Parse of request\'s params. Form necessary data structures')
        data_with_types, data_list, data_with_no_types = RequestHandler.parse_request(params)
        logging.info('Connect to database')
        db_handler = DatabaseHandler()
        logging.info('Searching of forms from db')
        matched_forms = db_handler.find_matches(data_with_types, data_list, data_with_no_types)
        db_handler.delete_primary_data()
        headers, status_code = SocketServer.form_headers(method, url)
        body = SocketServer.form_content(status_code, url, matched_forms)
        return (headers + body).encode()

    @staticmethod
    def run_server():
        logging.info('Start of app')
        logging.info('Start of socket\'s configuration')
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IP
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)  # Reuse addresses
        server_sock.bind((HOST, PORT))
        logging.info('End of socket\'s configuration')
        server_sock.listen()
        while True:
            client_sock, addr = server_sock.accept()
            request = client_sock.recv(1024)
            response = SocketServer.form_response(request.decode('utf-8'))
            client_sock.sendall(response)
            client_sock.close()
