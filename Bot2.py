import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
def write_message(sender, message):
    authorize.method('messages.send', {'chat_id': sender, 'message': message, 'random_id': get_random_id()})
token = ""
authorize = vk_api.VkApi(token = token)
longpoll = VkBotLongPoll(authorize, group_id=)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat and event.message.get('text'):
        reseived_message = event.message.get('text')
        sender = event.chat_id
        if reseived_message == "Ильшат":
            write_message(sender, "Приветики коотик")
        elif reseived_message == "Привет":
            write_message(sender, "O Hi Mark!")
        elif reseived_message == "Книга":
            write_message(sender, "Attention")

