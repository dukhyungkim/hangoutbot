import gspread
from google.oauth2.service_account import Credentials


def main():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = Credentials.from_service_account_file('key.json', scopes=scope)

    gc = gspread.authorize(credentials)

    wc = gc.open("TEST").sheet1
    a1 = wc.acell('A1').value
    print(a1)

    a2 = wc.cell(2, 1).value
    print(a2)

    cell = wc.find('6')
    print(cell)

    sum = int(a1) + int(a2)
    wc.update_acell('A3', sum)

    wc.update_cell(cell.row + 1, cell.col + 1, '0_0')


if __name__ == '__main__':
    main()
