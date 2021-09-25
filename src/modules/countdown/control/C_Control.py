import _thread
from modules.countdown.entities.E_Watch import E_Watch
from modules.countdown.const.Values import Commands, responses,Responses, commands
from modules.countdown.entities.E_Input import AMBIENT_NOISE
import time
import random

class C_Control:
	def __init__(self,mainGUI,sListener,sSpeaker,eInput,eWatch):
		self.mainGUI=mainGUI
		self.sListener=sListener
		self.sSpeaker=sSpeaker
		self.eInput=eInput
		self.eWatch=eWatch
	
	def process(self):
		workers=[self.listenningWorker,self.handlingWorker,self.greetingWorker]
		try:
			for worker in workers:
				self.startWorker(worker)
			self.mainGUI.process()
		except Exception as e:
			''''''
     
		while 1:
			pass

	def startWorker(self,job):
		_thread.start_new_thread(job,("",))

	def greetingWorker(self,name):
		self.sSpeaker.say(responses[Responses.GREETING])
		self.sSpeaker.say(responses[Responses.SELECT_TIME])

	def countDownGUIWorker(self,name):
		self.mainGUI.countdownGUI.countDown()
  
	def listenningWorker(self,name):
		self.sListener.process()
  
	def handlingWorker(self,name):
		while 1:
			time.sleep(0.001)
			inputValue=self.eInput.getValue()
			if not inputValue:
				continue

			for i in range(0, len(commands[Commands.GO])):
				if inputValue.find(commands[Commands.GO][i]) != -1:
		
					self.sSpeaker.say(responses[Responses.WAIT_COUNTING])
					count=3
					while count:
						self.sSpeaker.say(count)
						count=count-1
					i = random.randint(0, len(responses[Responses.START_COUNTING])-1)
					self.sSpeaker.say(responses[Responses.START_COUNTING][i])
					
					count=self.eWatch.getTotalSecs()
					self.startWorker(self.countDownGUIWorker)
					while count:
						time.sleep(1)
						count=count-1
						if count == 6: self.sSpeaker.say("5 seconds left")
					i = random.randint(0, len(responses[Responses.TIME_UP])-1)
					self.sSpeaker.say(responses[Responses.TIME_UP][i])			
	
					self.eInput.resetValue()
					continue
				if inputValue.find(AMBIENT_NOISE) != 0:
					''''''