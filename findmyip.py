# THIS CODE EXISTS BECAUSE I WANT TO BE ALERTED WHEN MY PUBLIC IP CHANGES AND I COULDN'T GET TO GRIPS WITH NOIP.COM DDNS.
# WHEN MY PUBLIC IP CHANGES I NEED TO CHANGE THE IP THAT MY WIREGUARD CLIENTS/PEERS CONNECT TO SO THEY MATCH.
# IT CAN RUN ON DEMAND ON MY COMPUTERS AND UPDATE THE WIREGUARD PEER DIRECTLY OR CAN RUN SCHEDULED AND I JUST GET AN EMAIL 
# TELLING ME THE PUBLIC IP HAS CHANGED. THE FUNCTION update_winguard_peers SHOULD ONLY BE CALLED IF YOU HAVE AN ACTIVE
# WIREGUARD PEER/CLIENT RUNNING OTHERWISE IT WILL ERROR. 
# THE PURPOSE OF THE FILE myipaddress.txt IS TO STORE THE EXISTING PUBLIC IP SO YOU GET ALERTED CORRECTLY. DJS 2025/11/09
import requests
import smtplib
import subprocess
import time
from email.message import EmailMessage


class IP:
    def __init__(self):
        self.FILE_PATH = "myipaddress.txt"                         # CREATE A FILE WITH THIS NAME CONTAINING ANYTHING E.G. 1.1.1.1
        self.EMAIL_ADDRESS = "YOUR_EMAIL@ADDRESS"
        self.SMTP_SERVER = "YOUR SMTP SERVER E.G. smtp.gmail.com"
        self.SMTP_PORT = 587                                       # YOUR SMTP PORT - THIS IS THE GMAIL ONE
        self.SMTP_PASSWORD = 'YOUR APP SMTP PASSWORD'              # IF YOU USE GMAIL SEE THE GOOGLE INSTRUCTIONS
        self.EMAIL_SUBJECT = "IP Change Notification"
        self.WG_INTERFACE = "THE NAME OF YOUR WIREGUARD INSTANCE"  # ONLY APPLICABLE IF YOU USE WIREGUARD
        self.WG_PEER_PUBLIC_KEY = "YOUR WIREGUARD PEER PUBLIC KEY" # ONLY APPLICABLE IF YOU USE WIREGUARD
        self.WG_PORT = ":51820"                                    # ONLY APPLICABLE IF YOU USE WIREGUARD
        self.IP_API_URL = "https://api.ipify.org/?format=json"     # THIS URL RETURNS YOUR PUBLIC IP AS JSON


    def get_current_ip(self) -> str:
        response = requests.get(self.IP_API_URL)
        print(f"Current IP: {response.json()['ip']}")
        return response.json()['ip']


    def get_saved_ip(self) -> str:
        print(f"File Path : {self.FILE_PATH}")
        with open(self.FILE_PATH, 'r') as f:
            saved_ip = f.read().strip()
        print(f"Saved IP  : {saved_ip}")        
        return saved_ip


    def send_email(self, ip: str, saved_ip: str):
        print(f"IP has changed from {saved_ip} to {ip}, sending email.")
        msg = EmailMessage()
        msg['Subject'] = self.EMAIL_SUBJECT
        msg['From'] = self.EMAIL_ADDRESS
        msg['To'] = self.EMAIL_ADDRESS
        msg.set_content(ip)

        with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
            server.starttls()
            server.login(self.EMAIL_ADDRESS, self.SMTP_PASSWORD)
            server.send_message(msg)
        with open(self.FILE_PATH, 'w') as f:
            f.write(ip)
            f.flush()
            f.close()


    def update_winguard_peers(self, ip: str):
        new_endpoint = ip+self.WG_PORT
        cmd = [
            "wg", "set", self.WG_INTERFACE,
            "peer", self.WG_PEER_PUBLIC_KEY,
            "endpoint", new_endpoint
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("Endpoint updated successfully.")
            result = subprocess.run(["wg", "show", self.WG_INTERFACE], capture_output=True, text=True)
            print(result.stdout)
        else:
            print("Error updating endpoint:")
            print(result.stderr)


if __name__ == "__main__":
    ip_instance = IP()
    current_ip = ip_instance.get_current_ip()
    saved_ip = ip_instance.get_saved_ip()
    if current_ip != saved_ip:
        ip_instance.send_email(current_ip, saved_ip)
    #   ip_instance.update_winguard_peers(current_ip)  # ONLY RUN IF YOU HAVE OPEN WIREGUARD PEER CLIENT
    time.sleep(5)
