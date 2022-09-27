def make_country(country_name, capital):
    res = {'key_country': country_name, 'key_capital': capital }
    print(res['key_country'], res['key_capital'])


make_country(input('Country name: '), input('Capital: '))



