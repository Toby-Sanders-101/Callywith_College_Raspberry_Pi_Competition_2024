from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Harry:
	def __init__(self):
		chatbot = ChatBot('Harry the Health Expert')
		trainer = ChatterBotCorpusTrainer(chatbot)
		trainer.train("chatterbot.corpus.english")
		trainer.train("chatterbot.corpus.custom")
		self.chatbot = chatbot
	
	def getanswer(self, question):
		return self.chatbot.get_response(question)
