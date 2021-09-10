from transformers.pipelines.conversational import Conversation
import bot.chatbot as cb
from transformers import pipeline, set_seed, Conversation

class chatbot:
    def __init__(self):
        self.__messages = Conversation()
    def getResponse(self,text):
        return str(cb.get_response_to_text(text,self.__messages)).split('bot >> ')[-1]
    def reply(text):
        return chatbot().getResponse(text)