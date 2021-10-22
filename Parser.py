# добавлен нормальный класс, вытаскивание ссылки и варианта, добавление данных в датафрейм

from telethon import  TelegramClient, events
import pandas as pd
import re

class TelegramParser:

    id_list = []
    name_list = []
    link_list = []

    def __init__(self):
        self.id_list = []
        self.name_list = []
        self.link_list = []
        self.variant_list = []

        self.df = pd.DataFrame({
                        'id': self.id_list,
                        'name': self.name_list,
                        'link': self.link_list,
                        'var': self.variant_list
                    })

        self.chat = 'tgparsertest'
        self.api_id = 7974144
        self.api_hash = 'b7b5376255818266620cd9c4508ca0a9'

        self.client = TelegramClient('session', self.api_id, self.api_hash)
        self.client.start()
        print('|    CLIENT STARTED  |\n')


        @self.client.on(events.NewMessage(chats=self.chat))
        async def event_handler(event):
            if 'https://github.com/' in event.text:
                msg = event.message.message

                match = re.search('\w{7}\s\d{1,}', msg) # регулярное выражение для поиска нмоера варианта
                variant = match[0]

                match = re.search('\w{5}\W{3}\w{6}\W\w{3}\W\w*\W\w*', msg) # регулярное выражение по поиску ссылки на гит

                msg = match[0]

                async for partic in self.client.iter_participants(self.chat): # прохдимся по списку пользователей чата
                    if partic.id == event.message.sender_id:
                        
                        if partic.id in self.id_list: # если айди пользователя уже есть в списке (т.е. уже этот чел присылал ссылку)
                            index = self.id_list.index(partic.id) # то индекс из списка запомним
                            self.link_list[index] = msg # и в списке ссылок по индексу заменяем ссылку
                            self.variant_list[index] = variant

                        else:
                            self.id_list.append(partic.id)      # добавляем айди, имя, ссылку -отправителя  в  списки
                            self.name_list.append(partic.first_name)
                            self.link_list.append(msg)
                            self.variant_list.append(variant)

                self.update_df()
                print(self.df, '\n')
               
        self.client.run_until_disconnected()

    def update_df(self):
        self.df = pd.DataFrame({
                        'id': self.id_list,
                        'name': self.name_list,
                        'link': self.link_list,
                        'var' : self.variant_list
                    })

pars = TelegramParser()

#toDO автоматическое сохранение в файл эксель при каком то событии
#
