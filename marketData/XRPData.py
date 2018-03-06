from alpha_vantage.cryptocurrencies import CryptoCurrencies

cc = CryptoCurrencies(key='XNPHCZ8ACJ6PW4T6')
data, meta_data = cc.get_digital_currency_intraday(symbol='XRP', market='USD')

dailyData, dailyMetaData = cc.get_digital_currency_daily(symbol='XRP', market='USD')

print(dailyData)

# data['1b. price (USD)'].plot()
# plt.tight_layout()
# plt.title('Intraday value for ripple (XRP)')
# plt.grid()
# plt.show()
