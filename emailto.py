#neste código iremos receber uma matriz 4x8 indicando se houve uma mudança de estado de 
#de false para true em alguma coordenada da matriz.
import smtplib
import numpy as np
from email.mime.text import MIMEText

def emailto(x,y):
	# matriz de emails dos professores
	f = open('matriz_de_emails.txt')
	emails=f.read().split()
	for i in range(0,len(emails)):
         emails[i]=emails[i].split(',')
	#print(emails)
	# conexão com os servidores do google
	smtp_ssl_host = 'smtp.gmail.com'
	smtp_ssl_port = 465
	# username ou email para logar no servidor
	username = 'escaninhododes@gmail.com'
	password = 'professoresnotificados'

	from_addr = 'escaninhododes@gmail.com'
	to_addrs = ['d4vidcavalcante@gmail.com']

	# a biblioteca email possuí vários templates
	# para diferentes formatos de mensagem
	# neste caso usaremos MIMEText para enviar
	# somente texto
	message = MIMEText('Hello World')
	message['subject'] = 'Hello'
	message['from'] = from_addr
	message['to'] = ', '.join(to_addrs)

	# conectaremos de forma segura usando SSL
	server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
	# para interagir com um servidor externo precisaremos
	# fazer login nele
	server.login(username, password)
	server.sendmail(from_addr, to_addrs, message.as_string())
	server.quit()

#0 0 0 0 0 0 0 0
#0 0 0 0 0 0 0 0
#0 0 0 0 0 0 0 0
#0 0 0 0 0 0 0 0