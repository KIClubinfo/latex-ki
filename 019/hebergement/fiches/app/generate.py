from optparse import OptionParser

import string
import random

import models
import json_data

parser = OptionParser()
parser.add_option("-d", "--draft", \
                  action="store_true", dest="watermark", default=False, \
                  help="draw a watermark at the center of each page")

def random_password(size = 16):
	'''FTP contains between 8 and 30 characters, being only digits and letters, with at least one digit, one capital letter, one lowercase letter'''
	pwd_list = 	[random.choice(string.ascii_lowercase)]+ \
				[random.choice(string.ascii_uppercase)]+ \
				[random.choice(string.digits)]+ \
				[random.choice(string.ascii_letters+string.digits) for _ in range(size-3)]
	random.shuffle(pwd_list)
	return  ''.join(pwd_list)

def json_to_dict(json):
	dico = {}
	for table_slug, table_dict in json.items():
		for row_slug, row_value in table_dict.items():
			dico[table_slug+"_"+row_slug] = row_value

	return dico

if __name__ == "__main__":
	(options, args) = parser.parse_args()
	data = getattr(json_data, args[0])
	print(options.watermark)
	models.fiche.save_pdf(args[0], data, options.watermark)
	# models.fiche.save_tex(args[0], data, options.watermark)
