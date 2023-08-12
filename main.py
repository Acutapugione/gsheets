import gspread as gs

from oauth2client.service_account import ServiceAccountCredentials as Sac


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

creds = Sac.from_json_keyfile_name('vendor/secrets.json', scopes)
client = gs.authorize(credentials=creds)

# url = 'https://docs.google.com/spreadsheets/d/1-rtzt8giakXsCYENPcPgSYORmY1gQcD2CxYERY32GQk/edit#gid=0'
key = '1-rtzt8giakXsCYENPcPgSYORmY1gQcD2CxYERY32GQk'

# data_by_url = client.open_by_url(url)
data_by_key = client.open_by_key(key)

sheet1 = data_by_key.sheet1
print(sheet1.get_all_values())