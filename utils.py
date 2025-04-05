import socket

def grab_banner(sock):
    try:
        sock.settimeout(2)
        return sock.recv(1024).decode().strip()
    except:
        return "No banner"

def resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None
    
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def check_common_services(port):
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
    }
    
    return common_ports.get(port, "Unknown")
    