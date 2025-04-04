import socket
import concurrent.futures
import argparse

def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            return port, True
    except:
        return port, False
    
def scan_range(ip, start_port, end_port, threads=100):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port+1)]
        for f in concurrent.futures.as_completed(futures):
            port, is_open = f.result()
            if is_open:
                results.append(port)
                print(f"Port {port} is open")
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("target", help="Target IP / hostname")
    parser.add_argument("-sp", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-ep", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Amount of threads to be used")

    args = parser.parse_args()
    ip = socket.gethostbyname(args.target)

    print(f"Scanning {ip} from port {args.start} to {args.end}")
    scan_range(ip, args.start, args.end, args.threads)
