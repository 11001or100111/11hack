import subprocess 
import socket
import time
import signal
import colorama
import sys

kirmizi = colorama.Fore.RED
yesil = colorama.Fore.GREEN
mavi = colorama.Fore.BLUE
sari = colorama.Fore.YELLOW
reset = colorama.Fore.RESET

def signal_handler(sig, frame):
 for i in range(3, -1):
  print(f"{i} ", end='', flush=True)
 time.sleep(1)
 sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

subprocess.run(["figlet" , "11001or10011"])

question = (f"""{yesil}
1)Hack
2)Repo
3)Oyunlar{reset}
""")

games = (f"""{yesil}
1)Hollywood
2)Matrix
3)Tren
{reset} """)

library = (f"""{yesil}
1) Network Maping (Nmap)
2) Sqlmap
3) Waffw00f
4) Commix
5) Metasploit {reset}
""")

hack = (f"""{yesil}
1) Sql Hack Tarayıcı (1) 
2) XSS Bulguları Tarayıcı
3) Admin Panel Finder
4)Network Maping Analiz (1-2-3)

{reset}""")

subprocess.run(["clear"])

print(f"{kirmizi}Hoşgeldin kardeş 😉{reset}")

print(question)
soru1 = int(input("Seçiniz: "))
subprocess.run(["clear"])

if soru1 == 1:
   print(hack)
   hack1 = int(input("Hack Degeri Girin: "))
   if hack1 ==1:
    subprocess.run(["clear"])
    subprocess.run(["python","/data/data/com.termux/files/home/11Hack/Plugins/sql.py"])
   elif hack1 == 2:
    subprocess.run(["clear"])
    subprocess.run(["python", "/data/data/com.termux/files/home/11Hack/Plugins/xss.py"])
   elif hack1 == 3:
    subprocess.run(["clear"])
    subprocess.run(['adminpanelfinder'])

elif soru1 == 2:
 print(library)
 lib1 = int(input("Seçiniz: "))
 if lib1 == 1:
  subprocess.run(["clear"])
  print(f"{mavi}Yükleniyor... Lütfen Bekle {reset}")
  subprocess.run(['pkg','install','nmap','-y'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  subprocess.run(["nmap"])
 elif lib1 == 2:
  subprocess.run(["clear"])
  print(f"{mavi}Yükleniyor... Lütfen Bekle {reset}")
  subprocess.run(['git','clone','https://github.com/sqlmapproject/sqlmap.git'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
  subprocess.run(["clear"])
 elif lib1 ==3:
  subprocess.run(["clear"])
  print(f"{mavi}Yükleniyor... Lütfen Bekle {reset}")
  subprocess.run(['git','clone','https://github.com/EnableSecurity/wafw00f.git'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 elif lib1 ==4:
  subprocess.run(["clear"])
  print(f"{mavi}Yükleniyor... Lütfen Bekle {reset}")
  subprocess.run(['git' , 'clone' , 'https://github.com/commixproject/commix.git' ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 elif lib1 ==5:
  subprocess.run(["clear"])
  print(f"{mavi}Yükleniyor... Lütfen Bekle {reset}")
  subprocess.run(['git' , 'clone' , 'https://github.com/gushmazuko/metasploit_in_termux'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 else:
  print(f"{kirmizi}Hatalı Seçim! {reset}")


elif soru1 == 3:
 print(games)
 games1 = int(input("Seciniz: "))
 if games1 == 1:
  subprocess.run(['pkg' , 'install' , 'hollywood', '-y' ])
  subprocess.run(["clear"])
  subprocess.run(['hollywood'])
 elif games1 ==2:
  subprocess.run(['pkg' , 'install', 'cmatrix', '-y']) 
  subprocess.run(["clear"])
  subprocess.run(["cmatrix"])
 elif games1 ==3:
  subprocess.run(['pkg', 'install', 'sl' ,'-y' , 'sl'])
  subprocess.run(["sl"])
  subprocess.run(["clear"])
else:
 print(f"{kirmizi} Hata! Yanlış Seçim{reset}")

