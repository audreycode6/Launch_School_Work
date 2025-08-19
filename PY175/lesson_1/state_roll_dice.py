import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request = client_socket.recv(1024).decode()
    if not request or 'favicon.ico' in request:
        client_socket.close()
        continue

    request_line = request.splitlines()[0]
    http_method, path_and_params, _ = request_line.split(" ")
    if "?" in path_and_params:
        path, params = path_and_params.split("?")
    else:
        path = path_and_params
        params = "number=0"

    params = params.split("&")
    params_dict = {}
    for param in params:
        key, value = param.split("=")
        params_dict[key] = value

    number = int(params_dict.get('number', 0))

    response_body = ("<html><head><title>Counter</title></head><body>"
                     f"<h1>HTTP Request Information:</h1>"
                     f"<p><strong>Request Line:</strong> {request_line}</p>"
                     f"<p><strong>HTTP Method:</strong> {http_method}</p>"
                     f"<p><strong>Path:</strong> {path}</p>"
                     f"<p><strong>Parameters:</strong> {params_dict}</p>"
                     "<h2>Counter:</h2>"
                     f"<p style='color: red;'>The current number is {number}</p>"
                     f"<a href='?number={number + 1}'>Add one</a>"
                     "&nbsp;&nbsp;"
                     f"<a href='?number={number - 1}'>Subtract one</a>"
                     "</body></html>")

    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}")

    client_socket.sendall(response.encode())
    client_socket.close()