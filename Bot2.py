import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
def write_message(sender, message):
    authorize.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})
token = "5d6682670dbb8617e8b7e06d03a6ea3a5892bdf237bcd54dbab821cbe7f8dfa9364e55eb019495eca2756"
authorize = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(authorize, group_id=197734658)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text'):
        reseived_message = event.message.get('text')
        sender = event.chat_id
        if reseived_message == "Ильшат":
            write_message(sender, "Приветики коотик")
        elif reseived_message == "Привет":
            write_message(sender, "O Hi Mark!")

