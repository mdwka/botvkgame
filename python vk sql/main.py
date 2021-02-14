import vk_api
from sqlqwe import sender

from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token

vk_session = vk_api.VkApi(token = main_token)
longpoll = VkLongPoll(vk_session)
print(longpoll.method

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                msg = event.text.lower()
                #sender(msg)