#IMPORTANDO BIBLIOTECAS
import time
import os
import phonenumbers
from phonenumbers import geocoder, carrier

#BARRA CARREGANDO
os.system("clear")
def progress_bar(done):
    print("\r\033[1;96mProgress: \033[1;93m[{0:50s}\033[1;93m]\033[1;35m{1:.1f}%".format('\033[1;92m#' * int(done * 50), done * 100),end='')

def pro():
    for n in range(101):
        progress_bar(n/100)
        time.sleep(0.1)
        os.system("clear")

pro()
#FINAL BARRA CARREGANDO

#PRINCIPAL
def main():
	os.system("clear")
	print("""
\033[1;96mBem vindo ao \033[1;101mTeleOP\033[0;0m
\033[1;96mDigite o numero de telefone com o \033[1;101m+55\033[0;0m
""")

	num = input("\033[1;95m>>>\033[1;92m ")

	if '+55' not in num:
		print("\nFaltou o +55\n")
		exit()

	pm = phonenumbers.parse(num)
	op = carrier.name_for_number(pm, 'pt-br')
	es = geocoder.description_for_number(pm, 'pt-br')

	os.system("clear")
	print("Encontrado!!!")
	print(f"\n\033[1;94mOperadora: {op}")
	print(f"Estado: {es}")
	print(f"Numero: {num}\n")

main()

#PERGUNTA PARA O USUARIO SE ELE DESEJA REALIZAR UMA NOVA CONSULTA
opc = input("\033[1;96mDeseja realizar uma nova consulta? \033[1;92ms\033[1;96m/\033[1;91mn\033[1;96m:\033[1;95m ")

#ACEITAR
if opc == 's' or opc == 'S' or opc == 'Y' or opc == 'y':
	main()

#RECUSAR
elif opc == 'n' or opc == 'N':
	print("\nTchauzinho ^-^\n")
	exit()

#RESPOSTA INVALIDA
else:
	print("\nTchauzinho ^-^\n")

if __name__== '__main__':
	main()
