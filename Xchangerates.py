'''This module returns current exchagerates (for each cryptocurrency) and converts the values to btc'''

from blockchain import exchangerates

def get_tickerf():
	ticker = exchangerates.get_ticker()
	#print the 15 min price for every currency
	for k in ticker:
		print (k, ticker[k].p15min)

def to_btcf():
	# The 'tobtc' method converts x value in the provided currency to BTC. Returns a float
	btc_amount = exchangerates.to_btc('USD', 4342.11)

	return btc_amount