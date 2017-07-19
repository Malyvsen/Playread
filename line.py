class line:
	char_name = None
	text = None

	def __init__(self, char_name = 'UNKNOWN_CHARACTER', text = 'UNKNOWN_TEXT'):
		self.char_name = char_name
		self.text = text



def extract_line(plain_text):
	colon = plain_text.find(':')
	if colon < 0:
		return line(char_name = 'Didaskalia', text = plain_text)
	char_name = plain_text[ : colon]
	text = ''
	if colon + 1 < len(plain_text):
		text = plain_text[colon + 1 : ]
	return line(char_name = char_name, text = text)
