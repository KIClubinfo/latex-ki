psp = {
	'site': {
		'name': "Ponts Safe Place",
		'domain': "psp.enpc.org",
		'creation_date': "8 décembre 2017",
		'expiry_date': "8 décembre 2018"
	},
	'owner': {
		'entity': "Ponts Safe Place",
		'person': "Frédéric Martin",
		'email': "frederic.martin@eleves.enpc.fr"
	},
	'ftp': {
		'authorized_people': "Frédéric Martin",
		'user': "enpc-psp",
		'password': "lt9nXlpy4RibZxXN"
	},
	'ki': {
		'directory': "www/psp/"
	}
}

bal = {
	'site': {
		'name': "Bal des Ponts",
		'domain': "baldesponts.enpc.org",
		'creation_date': "avant 2016",
		'expiry_date': "8 décembre 2018"
	},
	'owner': {
		'entity': "Bal des Ponts",
		'person': "Paul Gréaume",
		'email': "paul.greaume@eleves.enpc.fr"
	},
	'redirection': {	# Les redirections visibles permanentes d'OVH créent une entrée A et TXT
		'from': [
			"bal.enpc.org",
			"bal-des-ponts.enpc.org",
			"gala.enpc.org"
		],
		'to': "https://baldesponts.enpc.org",
		'type': "visible permanente"	# dégueux
	},
	'ftp': {
		'authorized_people': [
			"Paul Gréaume",
			"Nathan Godey",
			"Thomas Chabal"
		],
		'user': "enpc-bal",
		'password': "tu3Dya3Pf26sdflS"
	},
	'wordpress': {
		'login_page': "bal.enpc.org/wp-admin",
		'user': "enpc-gala",
		'password': "KzkqjbKZ5Cpc"
	},
	'email': {
		'address': "baldesponts@enpc.org",
		'password': "Connemara2017"
	},
	'ki': {
		'directory': "www/gala/"
	}
}

pontslarbears = {
	'site': {
		'name': "Pont'slar Bears",
		'domain': "pontslar-bears.enpc.org",
		'creation_date': "10 décembre 2017",
		'expiry_date': "10 juin 2018"
	},
	'owner': {
		'entity': "Liste BDE des Ponts'lar Bears",
		'person': "Sébastien Le Bouteiller",
		'email': "sebastien.le-bouteiller@eleves.enpc.fr (lebouteillersebastien@gmail.com)"
	},
	'ftp': {
		'authorized_people': "Sébastien Le Bouteiller",
		'user': "enpc-pontslarbears",
		'password': "edbfd5O3Inf5"
	},
	'email': {
		'address': "pontslar-bears@enpc.org",
		'password': "TonPrlU69em"
	},
	'ki': {
		'directory': "www/sitesdecampagne/pontslar-bears/"
	}
}

ghostpontsters = {
	'site': {
		'name': "Ghost Ponts'ters",
		'domain': "ghostpontsters.enpc.org",
		'creation_date': "10 décembre 2017",
		'expiry_date': "10 juin 2018"
	},
	'owner': {
		'entity': "Liste BDE Ghost Ponts'ters",
		'person': "Marius Schmidt-Mengin",
		'email': "ghostpontsters@eleves.enpc.fr"
	},
	'ftp': {
		'authorized_people': "Marius Schmidt-Mengin",
		'user': "enpc-ghostpontsters",
		'password': "aslkn86eP83sp"
	},
	'database': {
		'name': "ghostpontsters",
		'user': "ghostpontsters",
		'password': "yf5DpD3trg5"
	},
	'email': {
		'address': "ghostpontsters@enpc.org",
		'password': "ebF6oiTui65zM"
	},
	'ki': {
		'directory': "www/sitesdecampagne/ghostpontsters/"
	}
}