psp = {
	'_id': "psp",
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

baldesponts = {
	'_id': "baldesponts",
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
		'login_page': "https://bal.enpc.org/wp-admin",
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
	'_id': "pontslarbears",
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
	'_id': "ghostpontsters",
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

geoponts = {
	'_id': "geoponts",
	'site': {
		'name': "GéoPonts",
		'domain': "geoponts.enpc.org",
		'creation_date': "Avant 2016",
		'expiry_date': "13 décembre 2018"
	},
	'owner': {
		'entity': "Entreprise GéoSchool",
		'person': "Albéric Trancart",
		'email': "alberic.trancart@eleves.enpc.fr (alberic@geoschool.fr)",
		'role': "CTO"
	},
	'dns1': {
		'domain': "m1._domainkey.geoponts.enpc.org.",
		'txt': "k=rsa; t=s; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDOgNN1U6MDDmxam79iCxUv2Z+diW74tTxh6CATDloWmW70X7vjgcodx4hV46rOpCSOLPXRr7cJcA6BhP3fFw1EterUhFyVoUWrmfLHVZ7HZAPKoZOtTdrIzjET+kBxlgNui/MFIynHSE1hyn7Xe33F3lZALShg3/swxeRjkq92CQIDAQAB"
	},
	'dns2': {
		'domain': "geoponts.enpc.org.",
		'cname': "geoponts.enpc.fr.",
		'mx': ["20 mail.geoschool.fr.", "100 mx.sendgrid.net."],
		'txt': "v=spf1 mx a:geoponts.enpc.fr a:geoponts.enpc.org ip4:37.187.243.249 ip6:2001:41d0:52:cff::4e0 include:servers.mcsv.net include:sendgrid.net ~all",
		'anomaly': "zone enpc.org/IN: geoponts.enpc.org/MX 'mail.geoschool.fr' (out of zone) is a CNAME 'sw-par1-geoponts.stajou.top' (illegal)"
	}
}

# Remplacer club_data par les données à insérer

from pymongo import MongoClient
client = MongoClient()
db = client.fiches
clubs = db.clubs
#print(clubs.insert_one(geoponts).inserted_id)
#clubs.update_one({'_id': "geoponts"}, {'$set': {'dns1': geoponts['dns1'], 'dns2': geoponts['dns2']}})
#clubs.update_one({'_id': "geoponts"}, {'$set': {'dns2.txt': "k=rsa; t=s; p=MIGfMA0GCSqGSIb3DQEBAQU AA4GNADCBiQKBgQDOgNN1U6M DDmxam79iCxUv2Z+diW74tTxh6CA TDloWmW70X7vjgcodx4hV46rOpCSO LPXRr7cJcA6BhP3fFw1EterUhFyVoU WrmfLHVZ7HZAPKoZOtTdrIzjET+k BxlgNui/MFIynHSE1hyn7Xe33F3lZA LShg3/swxeRjkq92CQIDAQAB"}})
#clubs.update_one({'_id': "geoponts"}, {'$unset': {'dns': ""}})
#clubs.remove({'_id': "geoponts"})
#print(clubs.insert_one(geoponts).inserted_id)