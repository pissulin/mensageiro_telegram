from time import sleep
import paho.mqtt.client as mqtt
import json
import tweepy 
import telepot

tweets = list()

TOPICO =  'scripy/twitter'

client = mqtt.Client()

client.connect("mqtt.eclipse.org",1883, 60)


chave_consumidor = 'ZYsGMoOFEGsZZ9zyCWEXy3C5H'
segredo_consumidor = '102hsQ3Z1FYPlA2HNg8Vwc0wudKQQfn1l726r7Q3eH6ZchZz4R'
token_acesso = '1065019734167613440-riMkzW2vmo68FNYQlPXrOdHFG2gCOf'
token_acesso_segredo = 'eTHwBEHdcHxSZiI54euMDU78wyElZJ7iX2CJMK17zmrO5'

autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_segredo)

twitter = tweepy.API(autenticacao)


while True:
    resultados = twitter.search(q= 'VVAR3')
    for tweet in resultados:
        st = f'Usuário: {tweet.user.screen_name} - Tweet: {tweet.text}'

        payload = st.encode()
        client.publish(TOPICO, payload, qos = 0)
        print( payload.decode())
        sleep(5)
    

    sleep(15)


