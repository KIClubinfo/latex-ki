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
	loader = jinja2.FileSystemLoader(os.path.abspath('app/templates/'))
)

class Row():
	def __init__(self, slug, field, values=None):
		self.slug = slug
		self.field = field
		self.values = values if type(values) is list else [values]
		self.template = latex_env.get_template('row.tex')

	def template(self, table_slug):
		return self.template.render(field=self.field, value=(', '.join(self.values) if self.values else "\VAR{%s}" % (table_slug+"_"+self.slug)))

	def tex(self, value=None):
		if not value and not self.values:
			raise ValueError("Mandatory filled not filled")
		if type(value) is list:
			value = ', '.join(value)
		return self.template.render(field=self.field, value=value if value else ', '.join(self.values))

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

	def tex(self, json_data, draft=False):
		return self.template.render(title=self.title, tables=[self.table(table_slug).tex(json_data[table_slug]) for table_slug, table_data in json_data.items()], draft=draft)

	def save_tex(self, slug_name, json_data, draft=False, dir=None):
		if dir:
			if dir[-1] not in {"/", "."}:
				dir+="/"
		else:
			dir = "app/tex/"
		subprocess.call(["mkdir", "-p", dir])

		with open(dir+'{}.tex'.format(slug_name), 'w') as output_file:
			output_file.write(fiche.tex(json_data, draft))

	def clean(self, slug_name="*"):
		if slug_name == "*":
			tmp_folder = "app/tmp/"
		else:	
			tmp_folder = "app/tmp/"+slug_name

		subprocess.call(["rm", "-R", tmp_folder])

	def save_pdf(self, slug_name, json_data, draft=False):
		tmp_folder = "app/tmp/"+slug_name
		self.save_tex(slug_name, json_data, draft, tmp_folder)
		for i in range(2):
			subprocess.call(["xelatex", "{}.tex".format(slug_name)], cwd=tmp_folder)
		subprocess.call(["mv", "{}/{}.tex".format(tmp_folder, slug_name), "app/tex/{}.tex".format(slug_name)])
		subprocess.call(["mv", "{}/{}.pdf".format(tmp_folder, slug_name), "pdf/{}.pdf".format(slug_name)])
		#subprocess.call(["rm", "-R", tmp_folder])

	def placeholders(self):
		return sum(table.placeholders() for table in self.tables)

	def table(self, table_slug):
		for table in self.tables:
			if table.slug == table_slug:
				return table


fiche = Fiche("fiche", "Fiche d'hébergement KI",
			Table('site', "Site web",
				Row('name', "Nom"),
				Row('domain', "Nom de domaine"),
				Row('creation_date', "Date de création"),
				Row('expiry_date', "Date d'expiration$^*$"),
				Row('ssl', "Certificat SSL", "Oui"),
				Row('ipv6', "IPv6", "Oui"),
				Row('seperated_logs', "Logs séparés", "Non")
			),
			Table('owner',"Détenteur",
				Row('entity', "Entité"),
				Row('person', "Responsable$^{**}$"),
				Row('email', "Adresse email")
			),
			Table('redirection', "Redirections",
				Row('from', "Origine"),
				Row('to', "Destination"),
				Row('type', "Type")
			),
			Table('ftp', "Compte FTP",
				Row('server_domain', "Serveur hôte", "ftp.enpc.org (ftp.cluster007.ovh.net)"),
				Row('ip', "IP", "213.186.33.18"),
				Row('port', "Port", "21"),
				Row('authorized_people', "Personnes autorisées$^{***}$"),
				Row('user', "Utilisateur"),	# without hiphens
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
				Row('user', "Utilisateur"),
				Row('password', "Mot de passe")
			),
			Table('email', "Compte email",
				Row('login_page', "Page de login", "mail.enpc.org (mail.ovh.net)"),
				Row('address', "Adresse email"),
				Row('password', "Mot de passe"),
				Row('max_space', "Espace maximum", "1 Go")
			)
		)
