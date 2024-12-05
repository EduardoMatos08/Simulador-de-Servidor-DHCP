from time import sleep
import os

# Boas Vindas #
os.system('cls')
name = input('\nOlá! Qual o seu nome? ')
print(f'\nBem vindo(a), {name}!')
sleep(2)
os.system('cls')

# Introdução DHCP #
print('\n\nO DHCP permite que os hosts obtenham as informações de configuração TCP/IP necessárias de um servidor DHCP.')
sleep(2.5)
print('\nDHCP também é uma função de servidor de rede opcional que você pode implantar em sua rede para conceder endereços IP e outras informações para clientes DHCP.')
sleep(2.5)

# Configuração DHCP #
os.system('cls')
print('\n~ Configuração DHCP ~\n')
sleep(1)

error = True
# Máscara
while error:
    print('\nA Máscara Padrão é: 255.255.255.0 ...')
    mascara = input('Digite a Máscara: ')
    if mascara != "255.255.255.0":
        print('\nHouve um erro...')
        sleep(2)
        print('Reiniciando...')
        sleep(2)
        os.system('cls')
    else:
        error = False

error = True
# Default Gateway
while error:
    print('\nÉ obrigatório que o final do Gateway seja 1.')
    defaultGateway = input('Digite o Default Gateway: ')
    # Quebra do Gateway por dígitos
    newGateway = defaultGateway.split('.')

    if len(newGateway) != 4:
        print('\nLeia atentamente as instruções antes de definir o Gateway.')
        sleep(2)
        print('Reiniciando...')
        sleep(2)
        os.system('cls')
    elif newGateway[0] == '255' or newGateway[1] == '255' or newGateway[2] == '255' or newGateway[3] == '255':
        print('\nHouve um erro...')
        sleep(2)
        print('Reiniciando...')
        sleep(2)
        os.system('cls')
    elif newGateway[3] != '1':
        print('\nHouve um erro...')
        sleep(2)
        print('Reiniciando...')
        sleep(2)
        os.system('cls')
    else:
        error = False

error = True
# DNS
while error:
    print(f'\nDNS Padrão é: 8.8.8.8 ou 8.8.4.4 ...')
    dns = input('Digite o DNS: ')
    if dns != "8.8.8.8" and dns != "8.8.4.4":
        print("\nHouve um erro...")
        sleep(2)
        print("Leia atentamente as instruções para definir o DNS.")
        sleep(2)
        os.system('cls')
    else:
        error = False

error = True
# QTD de Dispositivos
while error:
    DispositivosQTD = int(input('\nQuantidade de Dispositivos: '))
    error = False

error = True
# IP de Início
while error:
    print(f'\nO IP não pode ser diferente dos dois primeiros conjuntos de números de: {defaultGateway} ...')
    initIP = input('Digite o IP de Início: ')

    # Quebra do IP por dígitos
    newIp = initIP.split('.')

    # Verificação
    if newIp[0] != newGateway[0] or newIp[1] != newGateway[1] or newIp[3] == '1' or newIp[3] == '0' or newIp[3] == '255':
        print('\nLeia atentamente as instruções antes de definir o IP.')
        sleep(2)
        print('Reiniciando...')
        sleep(2)
        os.system('cls')
    elif DispositivosQTD + int(newIp[-1]) >= 255:
        print('\nO último número de um dos IPs irá atingir 255, isso não é permitido...')
        sleep(5)
        print('Reiniciando...')
        sleep(2)
        os.system('cls')
    else:
        error = False

error = True
# Prints
for i in range(DispositivosQTD):

    print("\n########################################\n")
    # Host
    print(f'\nHost {i + 1}')
    # IP
    if i == 0:
        print('\nIP: ', '.'.join(newIp))
        sleep(0.5)
    else:
        newIp[-1] = str(int(newIp[-1]) + 1)
        print('\nIP:', '.'.join(newIp))
        sleep(0.5)
    # Gateway
    print(f'\nGateway: {defaultGateway}')
    sleep(0.5)
    # DNS
    print(f'DNS: {dns}')
    sleep(0.5)
    # Máscara
    print(f'Máscara: {mascara}\n')
    sleep(0.5)

print('\n\n~ Servidor DHCP ~\nBy Eduardo Matos & Felipe Bueno\n\n\n')