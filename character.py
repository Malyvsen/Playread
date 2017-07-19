import pyttsx3 as tts
import threading as th
import random
import tkinter as tk


voice_engine = tts.init() # Used for property extraction only
available_voices = voice_engine.getProperty('voices')


def voice_descriptor(voice):
	return voice.name if voice.name else 'Unknown name'


speaking = False
def speak(text):
	global speaking
	voice_engine.say(text)
	voice_engine.runAndWait()
	speaking = False


def launch_speak_thread(text):
	global speaking
	speaking = True
	thread = th.Thread(target = speak, args = (text,))
	thread.start()



max_volume_control = 100

class character:
	name = None
	voice = None
	volume = None
	rate = None

	window = None
	voice_list = None
	volume_slider = None
	rate_slider = None


	def __init__(self, name = 'UNKNOWN_NAME', voice = None, volume = 0.5, rate = 150):
		random.seed(name)

		self.name = name
		self.voice = voice if voice else random.choice(available_voices)
		self.volume = volume
		self.rate = rate

		self.window = tk.Tk()
		self.window.wm_title(name)
		self.window.resizable(width = False, height = False)

		tk.Label(self.window, text = 'Voice').pack()
		self.voice_list = tk.Listbox(self.window, selectmode = tk.SINGLE, width = 64)
		for curr_voice in range(len(available_voices)):
			self.voice_list.insert(curr_voice + 1, voice_descriptor(available_voices[curr_voice]))
		voice_id = next(i for i in range(len(available_voices)) if available_voices[i] == self.voice)
		self.voice_list.selection_set(voice_id)
		self.voice_list.activate(voice_id)
		self.voice_list.pack()

		tk.Label(self.window, text = 'Volume').pack()
		self.volume_slider = tk.Scale(self.window, from_ = 0, to = max_volume_control, orient = tk.HORIZONTAL, length = 480)
		self.volume_slider.set(max_volume_control // 2)
		self.volume_slider.pack()

		tk.Label(self.window, text = 'Speaking rate').pack()
		self.rate_slider = tk.Scale(self.window, from_ = 50, to = 300, orient = tk.HORIZONTAL, length = 480)
		self.rate_slider.set(175)
		self.rate_slider.pack()


	def speak(self, text):
		voice_engine.setProperty('voice', self.voice.id)
		voice_engine.setProperty('volume', self.volume)
		voice_engine.setProperty('rate', self.rate)
		launch_speak_thread(text)


	def ui_update(self):
		try:
			self.window.update()
			voice_selection = self.voice_list.curselection()
			if len(voice_selection) > 0:
				self.voice = available_voices[voice_selection[0]]
			self.volume = self.volume_slider.get() / max_volume_control
			self.rate = self.rate_slider.get()
			return True
		except:
			return False
