import tkinter as tk
import tkinter.filedialog as fd
import character
import line


characters = {}
lines = []


master_win = tk.Tk()
master_win.wm_title('Playread controller')
filename = fd.askopenfilename(title = 'Select script', filetypes = (('Plain text', '*.txt'),))


with open(filename, encoding = 'latin-1') as script:
	for txt_line in script:
		line_dat = line.extract_line(txt_line)
		if line_dat.char_name in characters:
			pass
		else:
			# The character hasn't yet been listed
			characters[line_dat.char_name] = character.character(name = line_dat.char_name)
		lines.append((line_dat.char_name, line_dat.text))


with open(filename, encoding = 'latin-1') as script:
	end = False
	while not end:
		txt_line = script.readline()
		line_dat = line.extract_line(txt_line)
		characters[line_dat.char_name].speak(line_dat.text)
		print(txt_line, end = '')
		while character.speaking:
			for char in characters:
				if not characters[char].ui_update():
					end = True
			try:
				master_win.update()
			except:
				end = True
			if end:
				character.voice_engine.endLoop()
