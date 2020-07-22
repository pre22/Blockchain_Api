''' This is the createallet Module'''

from blockchain import createwallet

# Wallet Parameters
# password : str - password for the new wallet. At least 10 characters.
# api_code : str - API code with the create wallets permission
# service_url: str - URL to an instance of service-my-wallet-v3 (with trailing slash)
# priv : str - private key to add to the wallet (optional)
# label : str - label for the first address in the wallet (optional)
# email : str - email to associate with the new wallet (optional)

wallet = createwallet.create_wallet('1234password', '58ck39ajuiw', 'http://localhost:3000/', label = 'Test wallet')
