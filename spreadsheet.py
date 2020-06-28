import gspread
from oauth2client.service_account import ServiceAccountCredentials

gsheet_id = '1twnRPyhNn8Dfg_ybybRluEIYSh0sa9dHniM9t07qjzM'

def gsheet_store(activeCases, recoveries, deaths):
    print('Accessing gooogle sheet...')

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', scope)
    client = gspread.authorize(creds)

    ws = client.open_by_key(gsheet_id).sheet1

    col = ws.col_values(13)
    toInsert = len(col) + 1
    print('Row to insert val at ',toInsert)

    ws.update_cell(toInsert, 17, activeCases)
    print('Active cases stored at row ', toInsert)

    ws.update_cell(toInsert, 15, recoveries)
    print('Recoveries stored at row ', toInsert)

    ws.update_cell(toInsert, 13, deaths)
    print('Deaths stored at at row ', toInsert)