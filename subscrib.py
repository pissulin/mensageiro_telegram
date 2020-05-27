import paho.mqtt.client as mqtt
import telepot
from time import sleep

tweets = list()

TOPICO =  'scripy/twitter'  
# Funçao a ser chamada quando chegar um pacote do tipo CONNACK .
def conectou(client, userdata, flags, rc):
    print("Conectado! Código recebido:"+str(rc))
    # Assinando todas as publicações dentro do tópio 
    

    client.subscribe(TOPICO)

# Função chamada quando uma nova mensagem do tópico é recebida.
def chegou_mensagem(client, userdata, msg):
    dado = msg.payload
    tweets.append(dado.decode())
    print(dado.decode())

def opcoes(msg):
    chat_id = msg['chat']['id']
    commando = msg['text']

    print(str(commando))


    if commando == "/noticias":
        global tweets
        tweetsCopy = tweets[:]
        for i in tweetsCopy:
            bot.sendMessage(chat_id, i)
        tweetsCopy = []
tweets = []
    

bot = telepot.Bot('1119773173:AAHDHl_fceEqq-ncu-m1ISRtqXPLZ_jajXQ') 
bot.message_loop(opcoes)
print("to esperando...")


client = mqtt.Client()
client.on_connect = conectou
client.on_message = chegou_mensagem

client.connect ("mqtt.eclipse.org",1883, 60)

# Permanece em loop, recebendo mensagens # e manipulando a conexão.
client.loop_forever()




