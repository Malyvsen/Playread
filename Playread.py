import tkinter as tk
import tkinter.filedialog as fd
import character
import line


characters = {}
lines = []


master_win = tk.Tk()
master_win.wm_title('Playread controller')
filename = fd.askopenfilename(title = 'Select script', filetypes = (('Plain text', '*.txt'),))


num_lines = 0
with open(filename, encoding = 'latin-1') as script:
	for txt_line in script:
		num_lines += 1
		line_dat = line.extract_line(txt_line)
		if line_dat.char_name in characters:
			pass
		else:
			# The character hasn't yet been listed
			characters[line_dat.char_name] = character.character(name = line_dat.char_name)
		lines.append(line_dat)


def set_current_line(value):
	global current_line
	current_line = int(value)


tk.Label(master_win, text = 'Line number').pack()
progress_slider = tk.Scale(master_win, from_ = 0, to = num_lines, orient = tk.HORIZONTAL, length = 1000, command = set_current_line)
progress_slider.pack()


current_line = 0
end = False
while not end:
	line_dat = lines[current_line]
	current_line += 1
	characters[line_dat.char_name].speak(line_dat.text)
	print(line_dat.char_name + ':\t\t' + line_dat.text, end = '')
	while character.speaking and not end:
		for char in characters:
			if not characters[char].ui_update():
				end = True
		try:
			progress_slider.set(current_line)
			master_win.update()
		except:
			end = True
		if end:
			character.voice_engine.endLoop()
