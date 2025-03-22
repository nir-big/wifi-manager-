import socket

class HTTPServer:
    def __init__(self, motor_controller):
        self.motor_controller = motor_controller

    def start(self, ip, port=80):
        addr = socket.getaddrinfo(ip, port)[0][-1]
        server_socket = socket.socket()
        server_socket.bind(addr)
        server_socket.listen(1)
        print(f"Server started at http://{ip}:{port}")

        while True:
            conn, addr = server_socket.accept()
            print("Client connected from", addr)
            request = conn.recv(1024).decode()
            print("Request:", request)

            # Handle HTTP request
            response = self.handle_request(request)
            conn.sendall(response.encode())
            conn.close()

    def handle_request(self, request):
        # Map URL to motor commands
        if "/forward" in request:
            self.motor_controller.forward()
        elif "/backward" in request:
            self.motor_controller.backward()
        elif "/left" in request:
            self.motor_controller.left()
        elif "/right" in request:
            self.motor_controller.right()
        elif "/stop" in request:
            self.motor_controller.stop()
        elif "/forward_left" in request:
            self.motor_controller.forward_left()
        elif "/forward_right" in request:
            self.motor_controller.forward_right()
        elif "/backward_left" in request:
            self.motor_controller.backward_left()
        elif "/backward_right" in request:
            self.motor_controller.backward_right()
        elif "/rotate_left" in request:
            self.motor_controller.rotate_left()
        elif "/rotate_right" in request:
            self.motor_controller.rotate_right()
        else:
            return "HTTP/1.1 404 Not Found\n\nUnknown Command"

        return "HTTP/1.1 200 OK\n\nCommand Executed"

