import jinja2
import os
import subprocess

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

class Row():
	def __init__(self, slug, field, *values):
		self.slug = slug
		self.field = field
		self.value = ', '.join(values) if values else None
		self.template = latex_env.get_template('row.tex')

	def template(self, table_slug):
		return self.template.render(field=self.field, value=(self.value if self.value else "\VAR{%s}" % (table_slug+"_"+self.slug)))

	def tex(self, value):
		return self.template.render(field=self.field, value=self.value if self.filled() else value)

	def filled(self):
		return self.value != None

class Table():
	def __init__(self, slug, title, *rows):
		self.slug = slug
		self.title = title
		self.rows = rows
		self.template = latex_env.get_template('table.tex')


	def template(self):
		return self.template.render(title=self.title, rows=[row.template(self.slug) for row in self.rows])

	def tex(self, json_data):
		return self.template.render(title=self.title, rows=[row.tex(json_data[row.slug] if row.slug in json_data else None) for row in self.rows])

	def placeholders(self):
		return [self.slug+"_"+row.slug for row in rows if row.filled()]

class Fiche():
	def __init__(self, slug, title="Fiche d'hébergement KI", *tables):
		self.slug = slug
		self.title = title
		self.tables = tables
		self.template = latex_env.get_template('fiche.tex')

	def template(self):
		return self.template.render(title=self.title, tables=[table.template() for table in self.tables])

	def tex(self, json_data, watermark=False):
		return self.template.render(title=self.title, tables=[table.tex(json_data[table.slug]) for table in self.tables if table.slug in json_data], watermark=watermark)

	def save_tex(self, slug_name, json_data, watermark=False, dir=None):
		if dir:
			if dir[-1] not in {"/", "."}:
				dir+="/"
		else:
			dir = "tex/"
		subprocess.call(["mkdir", "-p", dir])

		with open(dir+'{}.tex'.format(slug_name), 'w') as output_file:
			output_file.write(fiche.tex(json_data, watermark))

	def clean(self, slug_name="*"):
		if slug_name == "*":
			tmp_folder = "tmp/"
		else:	
			tmp_folder = "tmp/"+slug_name

		subprocess.call(["rm", "-R", tmp_folder])

	def save_pdf(self, slug_name, json_data, watermark=False):
		tmp_folder = "tmp/"+slug_name
		self.save_tex(slug_name, json_data, watermark, tmp_folder)
		for i in range(2):
			subprocess.call(["xelatex", "{}.tex".format(slug_name)], cwd=tmp_folder)
		subprocess.call(["mv", "tmp/{0}/{0}.tex".format(slug_name), "tex/{}.tex".format(slug_name)])
		subprocess.call(["mv", "tmp/{0}/{0}.pdf".format(slug_name), "../pdf/{}.pdf".format(slug_name)])
		subprocess.call(["rm", "-R", tmp_folder])

	def placeholders(self):
		return sum(table.placeholders() for table in self.tables)


fiche = Fiche("fiche", "Fiche d'hébergement KI",
			Table('site', "Site web",
				Row('name', "Nom"),
				Row('domain', "Nom de domaine"),
				Row('creation_date', "Date de création"),
				Row('expiry_date', "Date d'expiration"),
				Row('ssl', "Certificat SSL", "Oui"),
				Row('ipv6', "IPv6", "Oui"),
				Row('seperated_logs', "Logs séparés", "Non")
			),
			Table('owner',"Détenteur",
				Row('entity', "Entité"),
				Row('person', "Responsable"),
				Row('email', "Adresse email")
			),
			Table('ftp', "Compte FTP",
				Row('server_domain', "Serveur hôte", "ftp.enpc.org (ftp.cluster007.ovh.net)"),
				Row('ip', "IP", "213.186.33.18"),
				Row('port', "Port", "21"),
				Row('authorized_people', "Personnes autorisées"),
				Row('user', "Utilisateur"),
				Row('password', "Mot de passe"),
				Row('ssh', "SFTP / SSH", "Oui"),
				Row('max_space', "Espace maximum", "1 Go"),
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
				Row('password', "Mot de passe"),
				Row('interface', "Interface admin", "https://phpmyadmin.ovh.net"),
				Row('type', "Type", "MySQL 5.6"),
				Row('max_space', "Espace maximum", "1 Go"),
				Row('backup', "Sauvegarde hebdomadaire", "Oui")
			),
			Table('wordpress', "Wordpress",
				Row('login_page', "Page de login"),
				Row('user', "Utilisateur", "admin"),
				Row('password', "Mot de passe")
			),
			Table('email', "Compte email",
				Row('login_page', "Page de login", "mail.enpc.org (mail.ovh.net)"),
				Row('address', "Adresse email"),
				Row('password', "Mot de passe"),
				Row('max_space', "Espace maximum", "1 Go")
			)
		)
