import os
import os,sys,time,mechanize
from bs4 import BeautifulSoup as sup

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders =[('Connection','keep-alive'),('Pragma','no-cache'),('Cache-Control','no-cache'),('Origin','http://sms.payuterus.biz'),('Upgrade-Insecure-Requests','1'),('Content-Type','application/x-www-form-urlencoded'),('User-Agent','Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),('Referer','http://sms.payuterus.biz/alpha/'),('Accept-Encoding','gzip, deflate'),('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),]
url = 'http://sms.payuterus.biz/alpha'
z = []


def menu():
	print
	kntl = input("\033[1;92mPiLiH \033[2;93mYa/No \033[1;92m \033[0m: ")
	if kntl =="":
		exit()
	elif kntl =="Ya":
		solo()
	elif kntl =="ya":
		solo()
	elif kntl =="No":
		os.system ("sh index.sh")
		exit()
	elif kntl =="no":
		os.system ("sh index.sh")
		exit()
	else:
		exit()

def solo():
	print("")
	ppq = int(input('\033[0mNomor Target \033[0m: '))
	pes   = input(' \033[0mKetik Pesan \033[0m: ')
	ajg  = pes.split(' ')
	if pes =="":
		exit()
	else:
		bangsat = "-XcodeIyXerXez777"
		ajg = pes+"        "+bangsat
		bs = sup(br.open(url),features="html.parser")
		for x in bs.find_all("span"):
			z.append(x.text)
		bypass = int(str(z)[2])+int(str(z)[6])
		br.select_form(nr=0)
		br.form['nohp']=str(ppq)
		br.form['pesan']=str(ajg)
		br.form['captcha']=str(bypass)
		get = br.submit().read()
		if 'SMS Gratis Telah Dikirim' in str(get):
			print ("")
			print('               \033[0m[\033[1;92mOK\033[0m] Berhasil dikirim ke : \033[1;92m'+str(ppq))
			print ("")
			print ("KEMBALI KE HALAMAN UTAMA Y/n")
			os.system('sh ulang.sh')
		else:
			print ("")
			print('               \033[0m[\033[1;91mGAGAL\033[0m] Gagal mengirim ke : \033[1;92m'+str(ppq))
			print ("")
			input("\033[0m[ \033[1;91mBack \033[0m]")
			menu()

menu()

