import jinja2
import csv
import os
import subprocess
from optparse import OptionParser
from jinja2 import Template

parser = OptionParser()
parser.add_option("-d", "--draft", \
                  action="store_true", dest="draft", default=False, \
                  help="draw a watermark at the center of each page")

latex_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('templates/'))
)

def random_password():
	'''Contains between 9 and 16 letters, with digits and capital letters'''
	return "el3Ip45Mpzbi8"

class Row():
	def __init__(self, slug, field, *values):
		self.slug = slug
		self.field = field
		self.value = ', '.join(values) if values else "\VAR{%s}" % (slug)
		self.template = latex_env.get_template('row.tex')

	def template(self):
		return self.template.render(field=self.field, value=self.value)

	def tex(self, dico):
		return self.template.render(field=self.field, value=Template(self.value).render(**dico))

class Table():
	def __init__(self, slug, title, *rows):
		self.slug = slug
		self.title = title
		self.rows = rows
		self.template = latex_env.get_template('table.tex')


	def template(self):
		return self.template.render(title=self.title, rows=[row.template() for row in self.rows])

	def tex(self, dico):
		return self.template.render(title=self.title, rows=[row.tex(dico) for row in self.rows])

	def placeholders(self):
		return [row.slug for row in rows if row.value[0:4] == "\VAR{"]

class Fiche():
	def __init__(self, slug, title="Fiche d'hébergement KI", *tables):
		self.slug = slug
		self.title = title
		self.tables = tables
		self.template = latex_env.get_template('fiche.tex')

	def template(self):
		return self.template.render(title=self.title, tables=[table.template() for table in self.tables])

	def tex(self, dico={}):
		if "watermark" not in dico:
			dico["watermark"] = False
		return self.template.render(title=self.title, tables=[table.tex(dico) for table in self.tables])

	def save_tex(self, slug_name, dico={}, dir=""):
		if dir:
			if dir[-1] != "/":
				dir+="/"
			subprocess.call(["mkdir", "-p", dir])

		with open(dir+'{}.tex'.format(slug_name), 'w') as output_file:
			output_file.write(fiche.tex(dico))

	def save_pdf(self, slug_name, dico):
		self.save_tex(slug_name, dico, slug_name)

		for i in range(3):
			subprocess.call(["xelatex", "{0}/{0}.tex".format(slug_name)])
		subprocess.call(["mv", "{0}/{0}.pdf".format(slug_name), "{}.pdf".format(slug_name)])
		subprocess.call(["rm", "-R", slug_name])

	def placeholders(self):
		return sum(table.placeholders() for table in self.tables)

class Database():
	def __init__(self, *fiches):
		self.fiches = {fiche.slug: fiche for fiche in fiches}

	def find(slug):
		return self.fiches[slug]

	def __iadd__(self, fiche):
		self.fiches[fiche.slug] = fiche
		return self

fiches = Database()
fiche = Fiche("campagne", "Fiche d'hébergement KI",
			Table('site', "Site web",
				Row('name', "Nom"),
				Row('domain', "Nom de domaine"),
				Row('creation_date', "Date de création", "\\today"),
				Row('expiry_date', "Date d'expiration"),
				Row('ssl', "Certificat SSL", "Oui"),
				Row('ipv6', "IPv6", "Oui"),
				Row('seperated_logs', "Logs séparés", "Non")
			),
			Table('owner',"Détenteur",
				Row('enity', "Entité"),
				Row('person', "Responsable"),
				Row('email', "Adresse email")
			),
			Table('ftp', "Compte FTP",
				Row('server_domain', "Serveur hôte", "ftp.enpc.org (ftp.cluster007.ovh.net)"),
				Row('ip', "IP", "213.186.33.18"),
				Row('port', "Port", "21"),
				Row('authorized_people', "Personnes autorisées"),
				Row('user', "Utilisateur"),
				Row('password', "Mot de passe", random_password()),
				Row('ssh', "SFTP / SSH", "Oui"),
				Row('max_space', "Espace maximum", "1Go"),
				Row('apache', "Apache", "v2.4"),
				Row('php', "PHP", "v5.6"),
				Row('git', "Git", "v2.1")
			),
			Table('database', "Base de données",
				Row('server', "Serveur", "mysql.enpc.org (va1757-001.privatesql)"),
				Row('port', "Port", "35287"),
				Row('name', "Base de données"),
				Row('user', "Utilisateur"),
				Row('permissions', "Droits", "Admin (Select, Insert, Update, Delete, Create, Alter, Drop)"),
				Row('password', "Mot de passe", random_password()),
				Row('interface', "Interface admin", "https://phpmyadmin.ovh.net"),
				Row('type', "Type", "MySQL 5.6"),
				Row('max_space', "Espace maximum", "1 Go"),
				Row('backup', "Sauvegarde hebdomadaire", "Oui")
			),
			Table('wordpress', "Wordpress",
				Row('login_page', "Page de login"),
				Row('user', "Utilisateur", "admin"),
				Row('password', "Mot de passe", random_password())
			),
			Table('email', "Compte email",
				Row('login_page', "Page de login", "mail.enpc.org (mail.ovh.net)"),
				Row('address', "Adresse email"),
				Row('password', "Mot de passe", random_password()),
				Row('max_space', "Espace maximum", "1 Go")
			)
		)

	if __name__ == "__main__":
		(options, args) = parser.parse_args()
	with open('form.csv', 'r') as form:
		form_csv = csv.reader(form)
		placeholders = ["site_creation_date", "site_name", "owner_entity", "site_domain", "owner_person", "owner_email", \
			"a", "b", "c", "lifetime", "wordpress", "email", "database", "ftp", "owner_authorized_people", "e"]
		dico = dict(zip(placeholders, [e for i, e in enumerate(form_csv) if i == 1]))
		dico["watermark"] = options.draft

	fiche.save_pdf(args[0], dico)
