from telepot.loop import MessageLoop
import telepot
import time
from Recognition import findLetters
import signal


bot = telepot.Bot('токен сюды')
proxy = telepot.api.set_proxy('http://89.111.103.154:36813')

def imageUploadHandler(msg):
    content_type = telepot.glance(msg)

    chat_id = msg['chat']['id']
  #  print(msg)
  #  print(chat_id)
  #  print(content_type)
    file_path = 'img/id' +  msg['photo'][0]['file_id'] + '.png'
    file_id =  msg['photo'][2]['file_id']

    if content_type[0] == 'photo':

        bot.download_file(file_id,file_path)
        bot.sendMessage(chat_id,findLetters(file_path))



MessageLoop(bot, imageUploadHandler).run_as_thread()


while 1:
    time.sleep(10)


