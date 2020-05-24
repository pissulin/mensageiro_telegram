import telepot

class BotTelegram:
    def __init__(self):

        def opcoes(msg):
            chat_id = msg['chat']['id']
            commando = msg['text']

            print(str(commando))


            if commando == "/noticias":
                global tweets
                tweetsCopy = tweets[:]
                for i in tweetsCopy:
                    bot.sendMessage(chat_id, i)
                tweets = []

        bot = telepot.Bot('1119773173:AAHDHl_fceEqq-ncu-m1ISRtqXPLZ_jajXQ') 
        bot.message_loop(opcoes)