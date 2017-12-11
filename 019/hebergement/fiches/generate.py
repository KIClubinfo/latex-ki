from optparse import OptionParser

import string
import random

from app import models, data

parser = OptionParser()
parser.add_option("-d", "--draft", \
                  action="store_true", dest="draft", default=False, \
                  help="draw a watermark at the center of each page \
                  and does not print signing part")
parser.add_option("-k", "--ki", \
                  action="store_true", dest="ki", default=False, \
                  help="make fiche with ki reserved information")

def random_password(size = 16):
	'''FTP contains between 8 and 30 characters, being only digits and letters, with at least one digit, one capital letter, one lowercase letter'''
	pwd_list = 	[random.choice(string.ascii_lowercase)]+ \
				[random.choice(string.ascii_uppercase)]+ \
				[random.choice(string.digits)]+ \
				[random.choice(string.ascii_letters+string.digits) for _ in range(size-3)]
	random.shuffle(pwd_list)
	return  ''.join(pwd_list)

def json_to_dict(json):	# useless
	dico = {}
	for table_slug, table_dict in json.items():
		for row_slug, row_value in table_dict.items():
			dico[table_slug+"_"+row_slug] = row_value

	return dico

def vars_of(module):
	return [var for var in dir(module) if not var.startswith('__')]

if __name__ == "__main__":
	(options, args) = parser.parse_args()
	if args[0] == "*":
		print(vars_of(data))
		for slug in vars_of(data):
			json_data = getattr(data, slug)
			models.fiche.save_pdf(slug, json_data, options)
	else:
		for slug in args:
			json_data = getattr(data, slug)
			models.fiche.save_pdf(slug, json_data, options)