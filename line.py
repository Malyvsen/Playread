didaskalia = 'Didaskalia'


class line:
	char_name = None
	text = None


	def __init__(self, char_name = 'UNKNOWN_CHARACTER', text = 'UNKNOWN_TEXT'):
		self.char_name = char_name
		self.text = text.strip(' \t\n')


	def full_text(self):
		return self.char_name + ': ' + ''.join([' ' for i in range(32 - len(self.char_name))]) + self.text



def extract_line(plain_text):
	colon = plain_text.find(':')
	if colon < 0:
		return line(char_name = didaskalia, text = plain_text)
	char_name = plain_text[ : colon]
	text = ''
	if colon + 1 < len(plain_text):
		text = plain_text[colon + 1 : ]
	return line(char_name = char_name, text = text)
