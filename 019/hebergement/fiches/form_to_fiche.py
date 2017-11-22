import sys
import subprocess
import csv

def Row():
	def __init(slug, field, *values):
		self.slug = slug
		self.field = field
		self.values = *values

	def tex():
		return "{} & {} \\\\ \\hline".format(self.field, ", ".join(value))


def Table():
	def __init__(slug, title, rows):
		self.slug = slug
		self.title = title
		self.rows = rows

	def tex():
		tex = "\\begin\{tableau\}\{{}\}\\hline".format(self.title)
		for row in self.rows:
			tex += row.tex()
		tex += "\end{tableau}"

		return tex

def Fiche():
	def __init__(slug, title, tables):
		self.title = title
		self.tables = tables

	def tex():
		tex = """
			\documentclass{../ki019}

			\usepackage[T1]{fontenc}
			\usepackage{array}
			%\usepackage{draftwatermark}

			\\newcolumntype{K}[1]{>{\centering\\arraybackslash}p{#1}}

			\\newenvironment{tableau}[1]{
			\LARGE #1\\\\
			\\vspace{0.4cm}
			\\begin{tabular}{|K{5cm}|K{10cm}|}
			}
			{
			\end{tabular}
			\\vspace{0.5cm}
			}

			\\begin{document}

			\pagestyle{empty} \% Removes the page number from the bottom of the page

			\\noindent

			\section{Fiche d'hébergement KI}

			\\begin{center}
		"""
		for table in self.tables:
			tex += table.tex()
		tex += """
			\end{center}

			\Large \\noindent
			$^{\phantom{*}*}$ Hébergement renouvelable auprès du responsable hébergement. \\\\
			$^{**}$ Liste des personnes autorisées à connaître et utiliser les identifiants de l'accès FTP. Toute modification doit être portée à la connaissance du responsable hébergement.

			\Footer

			\end{document}
		""")

fiche = Fiche('alpontscino', "Fiche d'hébergement KI",
	Table('site', "Site web",
		Row('name', "Nom"),
		Row('domain', "Nom de domaine"),
		Row('creation_date', "Date de création", "\\today")
		Row('expiry_date', "Date d'expiration"),
		Row('ssl', "Certificat SSL", "Oui"),
		Row('ipv6', "IPv6", "Oui"),
		Row('seperated_logs', "Logs séparés", "Non")
	),
	Table('owner',"Détenteur",
		Row('enity', "Entité")
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
		Row('max_space', "Espace maximum"),
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
		Row('login_page', "Page de login"),
		Row('address', "Adresse email", "mail.enpc.org (mail.ovh.net)"),
		Row('password', "Mot de passe"),
		Row('max_space', "Espace maximum", "1 Go")
	)
)

tables = {
	'site': {
		'title': "Site web",
		'fields': {
			'name': "Nom",
			'domain': "Nom de domaine",
			'creation_date': ["Date de création", "\\today"],
			'expiry_date': "Date d'expiration",
			'ssl': ["Certificat SSL", "Oui"],
			'ipv6': ["IPv6", "Oui"],
			'seperated_logs': ["Logs séparés", "Non"]
		}
	},
	'owner': {
		'title': "Détenteur",
		'fields': {
			'enity': "Entité",
			'person': "Responsable",
			'email': "Adresse email"
		}
	},
	'ftp': {
		'title': "Compte FTP",
		'fields': {
			'server_domain': ["Serveur hôte", "ftp.enpc.org (ftp.cluster007.ovh.net)"],
			'ip': ["IP", "213.186.33.18"],
			'port': ["Port", "21"],
			'authorized_people': "Personnes autorisées",
			'user': "Utilisateur",
			'password': "Mot de passe",
			'ssh': ["SFTP / SSH", "Oui"],
			'max_space': "Espace maximum",
			'apache': ["Apache", "v2.4"],
			'php': ["PHP", "v5.6"],
			'git': ["Git", "v2.1"]
		}
	},
	'database': {
		'title': "Base de données",
		'fields': {
			'server': ["Serveur", "mysql.enpc.org (va1757-001.privatesql)",
			'port': ["Port", "35287"],
			'name': "Base de données",
			'user': "Utilisateur",
			'permissions': ["Droits", "Admin (Select, Insert, Update, Delete, Create, Alter, Drop)"],
			'password': "Mot de passe",
			'interface': ["Interface admin", "https://phpmyadmin.ovh.net"],
			'type': ["Type", "MySQL 5.6"],
			'max_space': ["Espace maximum", "1 Go"],
			'backup': ["Sauvegarde hebdomadaire", "Oui"]
		}
	},
	'wordpress': {
		'title': "Wordpress",
		'fileds': {
			'login_page': "Page de login",
			'user': ["Utilisateur", "admin"],
			'password': "Mot de passe"
		}
	},
	'email': {
		'title': "Compte email",
		'fields': {
			'login_page': "Page de login",
			'address': ["Adresse email", "mail.enpc.org (mail.ovh.net)"],
			'password': "Mot de passe",
			'max_space': ["Espace maximum", "1 Go"]
		}
	}
}

# Le respo doit faire partie de l'entité
# Mot de passe différent pour les mails qui sera divulgué

def tex_row(field, value):
	return "{} & {} \\\\ \\hline".format(field, value)

def tex_table(table):
	tex = "\\begin\{tableau\}\{{}\}\\hline".format(table['title'])
	for field, value in table['fields'].iteritems():
		tex += tex_row(field, value)
	tex += "\end{tableau}"

	return tex

if __name__ == "__main__":
	title = sys.argv[1]
	os.system("mkdir {}".format(title))
	with open('form.csv', 'r') as form, open('{0}/{0}.tex'.format(title), 'w') as fiche:
	    form_csv = csv.reader(form)
		form_csv.next()
		for fields in form_csv.next():
			[site_creation_date, site_name, owner_entity, site_domain, owner_person, owner_email, a, b, c, lifetime, wordpress, email, database, ftp, owner_authorized_people, e] = fields
		fiche.write("""
			\documentclass{../ki019}

			\usepackage[T1]{fontenc}
			\usepackage{array}
			%\usepackage{draftwatermark}

			\\newcolumntype{K}[1]{>{\centering\\arraybackslash}p{#1}}

			\\newenvironment{tableau}[1]{
			\LARGE #1\\\\
			\\vspace{0.4cm}
			\\begin{tabular}{|K{5cm}|K{10cm}|}
			}
			{
			\end{tabular}
			\\vspace{0.5cm}
			}

			\\begin{document}

			\pagestyle{empty} \% Removes the page number from the bottom of the page

			\\noindent

			\section{Fiche d'hébergement KI}

			\\begin{center}
		""")

		for table in tables:
			fiche.write(tex_table(table))

		fiche.write("""
			\end{center}

			\Large \\noindent
			$^{\phantom{*}*}$ Hébergement renouvelable auprès du responsable hébergement. \\\\
			$^{**}$ Liste des personnes autorisées à connaître et utiliser les identifiants de l'accès FTP. Toute modification doit être portée à la connaissance du responsable hébergement.

			\Footer

			\end{document}
		""")



