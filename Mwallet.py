'''This is the wallet module which handles the recieve and send logic '''

from blockchain.wallet import Wallet

wallet = Wallet('ada4e4b6-3c9f-11e4-baad-164230d1df67', 'password123', 'http://localhost:3000/')

# wallet = Wallet('identifier', 'password', 'service_url')

# The following tuple variables are to be created
'''
identifier : str
password : str
service_url : str - URL to an instance of service-my-wallet-v3 (with trailing slash)
second_password : str (optional)
api_code : str (optional)
'''

def sendf():
	#  Send bitcoin from your wallet to a single address. Returns a PaymentResponse object.
	#  The following params are to be created
	'''
	to : str - receiving address
	amount : int - amount to send (in satoshi)
	from_address : str - specific address to send from (optional)
	'''

	payment = wallet.send('to', amount, from_address='')

	return payment.tx_hash

def send_manyf():
	# Send bitcoin from your wallet to multiple addresses. Returns a PaymentResponse object.

	recipients = { '1NAF7GbdyRg3miHNrw2bGxrd63tfMEmJob' : 1428300,
					'1A8JiWcwvpY7tAopUkSnGuEYHmzGYfZPiq' : 234522117 }
	# recipients : dictionary - dictionary with the structure of 'address':amount

	payment = wallet.send_many(recipients)

	return payment.tx_hash

def get_balancef():
	# Fetch the wallet balance. Includes unconfirmed transactions and possibly double spends. Returns the wallet balance in satoshi.
	print (wallet.get_balance())

