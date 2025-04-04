def grab_banner(socket):
    try:
        socket.settimeout(2)
        return socket.recv(1024).decode().strip()
    except:
        return "No banner"