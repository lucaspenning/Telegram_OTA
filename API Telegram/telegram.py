import configparser
import socket
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
from pprint import pprint
from time import sleep, strftime
from datetime import datetime
import ctypes
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
PORTA = 1883
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):

    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("/lucas.penning@sou.ucpel.edu.br/")
palavra = '';
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    arquivo = open('novo-arquivo.txt', 'w')
    arquivo.write(str(msg.payload))
    arquivo.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Seta um usuário e senha para o Broker, se não tem, não use esta linha
client.username_pw_set("lucas.penning@sou.ucpel.edu.br", password="ae8d0e1c")

# Conecta no MQTT Broker
client.connect("mqtt.dioty.co", PORTA, 1883)


ctypes.windll.kernel32.SetConsoleTitleW('Telegram Bot')
config = configparser.ConfigParser()
config.read('config.ini')

API_TOKEN = config['TELEGRAM']['API_TOKEN']
TRUSTED_USERS = [int(x) for x in config['TELEGRAM']['TRUSTED_USERS'].split(',')]
ADMIN = int(config['TELEGRAM']['ADMIN'])
ESP8266_IP = config['LOCAL']['ESP8266_IP']


def auth_user(chat_id):
    TRUSTED_USERS.append(chat_id)  # todo: add config functionality

#Dialogo com Telegram
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'Olá! Se você ainda não está cadastrado, clique em "cadastrar".', reply_markup=keyboard)
        #Comando para ESP
        elif msg['text'] == "Versão_Atual":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="version", qos=0, retain=False)
                    sleep(12)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "version"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("Versao Atual: " + palavra) if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Reiniciar":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="reiniciar", qos=0, retain=False)
                    sleep(12)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    resp = ("Sistema reiniciado") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Uptime":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="uptime", qos=0, retain=False)
                    sleep(12)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "uptime"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("Ativo desde(Dia/Mes/Ano - HH/MM/SS):" + palavra) if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Horario":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="horario", qos=0, retain=False)
                    sleep(12)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "horario"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("Horário (Dia/Mes/Ano - HH/MM/SS):" + palavra) if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Atualizar":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="atualizar", qos=0, retain=False)
                    sleep(12)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "atualizar"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("" + palavra) if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Sensores":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="sensores", qos=0, retain=False)
                    sleep(12)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "sensores"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("Sensores: " + palavra) if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Temperatura":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="temperatura", qos=0, retain=False)
                    sleep(15)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "temperatura"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("Temperatura: " + palavra +"C") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Umidade":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="umidade", qos=0, retain=False)
                    sleep(15)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "umidade"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("Umidade: " + palavra +"%") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Log_24Hrs_Temperatura":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="logt", qos=0, retain=False)
                    sleep(15)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "logt"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("" + palavra +"%") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Log_24Hrs_Umidade":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="logu", qos=0, retain=False)
                    sleep(15)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "logu"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("" + palavra +"%") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Histórico_Atualizações":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="hist", qos=0, retain=False)
                    sleep(15)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "hist"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("" + palavra +"%") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        elif msg['text'] == "Parametro":
            if chat_id in TRUSTED_USERS:
                try:
                    client.publish("/lucas.penning@sou.ucpel.edu.br/", payload="parametro", qos=0, retain=False)
                    sleep(15)
                    arquivo = open('novo-arquivo.txt', 'r')
                    linha = arquivo.readline()
                    comprimento = len(linha)
                    palavra = linha[2:comprimento-1]
                    if(palavra == "parametro"):
                        resp = ("Sem resposta, tente novamente, caso persistir, verifique o embarcado!") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    else:
                        resp = ("Cada click irá aumentar em 10 minutos, ao chega a 60 minutos, irá retornar para 10 minutos." + palavra +" minutos.") if chat_id in TRUSTED_USERS else 'Sem Autorização'
                    bot.sendMessage(chat_id, resp, reply_markup=keyboard)
                except Exception as e:
                    print(e)
                    bot.sendMessage(chat_id, 'Houve um erro')
                    bot.sendMessage(chat_id, e, reply_markup=keyboard)
        #
        #
        #Cadastrando do usuario
        elif msg['text'] == "Cadastro":
            # apply for registration
            if chat_id not in TRUSTED_USERS:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
                print(f'{timestamp}  #  {chat_id}  #  Requested access.')
                bot.sendMessage(ADMIN, f'{chat_id} has requested access')
                bot.sendMessage(chat_id, f'Tentando registro. Sua identificação: {chat_id}.', reply_markup=keyboard)
            else:
                bot.sendMessage(chat_id, f'Já registrado. Sua identificação: {chat_id}.', reply_markup=keyboard)

        #Verificando autorização
        elif msg['text'] == "Verifica_Cadastro":
            # check user's own authorization
            resp = 'Você está cadastrado!' if chat_id in TRUSTED_USERS else 'Usuario não encontrado, faça seu cadastro!'
            bot.sendMessage(chat_id, resp, reply_markup=keyboard)

        #Tornando Administrador 
        elif msg['text'].split(' ')[-1] == "access" and chat_id == ADMIN:
            # approve registrations as ADMIN
            user = int(msg['text'].split(' ')[0])
            auth_user(user)
            bot.sendMessage(ADMIN, f'{user} has been TRUSTED', reply_markup=keyboard)
            bot.sendMessage(user, 'You were authorized!', reply_markup=keyboard)

    else:
        bot.sendMessage(chat_id, f'not text', reply_markup=keyboard)
        pprint(msg)

#Botões de comando no Telegram
keyboard = ReplyKeyboardMarkup(keyboard=[["Versão_Atual", "Reiniciar", "Uptime", "Temperatura", "Umidade"], ["Cadastro", "Verifica_Cadastro", "Sensores", "Horario", "Atualizar"], ["Log_24Hrs_Temperatura", "Log_24Hrs_Umidade", "Histórico_Atualizações", "Parametro"]])
bot = telepot.Bot(API_TOKEN)
info = bot.getMe()

def main():
    try:
        MessageLoop(bot, handle).run_as_thread()  # handle incoming messages
        print('API Bot Telegram em execução!')
        # Inicia o loop/Escutando MQTT
        client.loop_forever()
    except Error as e:
        print(e)
        main()
        
if __name__ == "__main__":
    main()
    input()
