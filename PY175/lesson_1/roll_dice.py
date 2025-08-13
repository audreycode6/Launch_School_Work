'''Update echo_server to now roll dice'''
import socket
import random # NEW

REQUIRED_PARAM_KEYS = {"rolls", "sides"}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ensure port is reuasabel if 'OSError: [Errno 48] Address already in use', 
 # else have to wait a min before port can be used again
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request = client_socket.recv(1024).decode()
    if (not request) or ('favicon.ico' in request):
        client_socket.close()
        continue

    request_line = request.splitlines()[0]

    request_line_items = request_line.split()
    response_body = f"{request_line_items}\n"

    http_method = request_line_items[0]
    path = request_line_items[1][0]
    query_strings = request_line_items[1][2:] # string of all query strings
    parameters = query_strings.split('&')
    
    #split each query param in paremeters into dict of param name: param value
    params_dict = {}
    for param in parameters:
        middle = param.find('=')
        key = param[:middle]
        value = param[middle + 1:]
        params_dict[key]=value

    # Handle error if side or rolls not in query strings:
    missing_param_message = (
            "ERROR: Expecting a query parameters for 'rolls' and 'sides' in order to continue.\n"
            "Please try a different url with the proper query strings.")  
    if not REQUIRED_PARAM_KEYS.issubset(params_dict.keys()):
        response = ("HTTP/1.1 400 Not Found\r\n"
                    "Content-Type: text/plan\r\n"
                    f"Content-Length: {len(missing_param_message)}\r\n"
                     "\r\n"
                     f"{missing_param_message}")
        client_socket.sendall(response.encode())
        client_socket.close()
        continue
    
    # Handle error if side or rolls value are not numeric: # TODO fix
    bad_request = False
    invalid_value_for_param_message = ("ERROR: Expecting numeric values"
            " for the 'rolls' and 'sides' parameters.")
    for key in REQUIRED_PARAM_KEYS:
        value = params_dict[key]
        if not value.isnumeric():
            response = ("HTTP/1.1 400 Not Found\r\n"
                        "Content-Type: text/plain\r\n"
                        f"Content-Length: {len(invalid_value_for_param_message)}\r\n"
                        "\r\n"
                        f"{invalid_value_for_param_message}")
            bad_request = True
    
    if bad_request:
        client_socket.sendall(response.encode())
        client_socket.close()
        continue

    # roll die (value of rolls in params_dict) -> for num in range(int(params_dict.get('rolls')
        # with (value of sides in params_dict) possibilities -> str(random.randint(1, int(params_dict.get('sides'))))
        # and keep track of each roll in list -> roll_history
    roll_history = [f'Roll {num + 1}: {str(random.randint(1, int(params_dict.get('sides'))))}' 
                    for num in range(int(params_dict.get('rolls')))]
    display_rolls = "\r\n".join(roll_history)
    
    
    response_body = (f"HTTP Method: {http_method}\r\n"
                     f"Path: {path}\r\n"
                     f"Parameters: {params_dict}'\r\n"
                     f"{display_rolls}")
    

    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(response_body)}\r\n" # NEW
                "\r\n"
                f"{response_body}\n") # NEW
    
    client_socket.sendall(response.encode())
    client_socket.close()
