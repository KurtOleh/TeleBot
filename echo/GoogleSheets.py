import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from echo.config import CREDENTIALS_FILE, spreadsheet_id


credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)


def writing_data(count, data_dict):
    readvalues = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range="A{}".format(count),
        majorDimension="ROWS"
    ).execute()

    if readvalues.get('values') is None:
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": "A{}".format(count),
                     "majorDimension": "ROWS",
                     "values": [["{}".format(data_dict.get('Час')),
                                 "{}".format(data_dict.get('Курс')),
                                 "{}".format(data_dict.get('Локація')),
                                 "{}".format(data_dict.get('День')),
                                 "{}".format(data_dict.get('ПІБ')),
                                 "{}".format(data_dict.get('Номер телефону'))
                                 ]]
                     },
                ]
            }
        ).execute()
    else:
        return writing_data(count + 1, data_dict)


# if __name__ == '__main__':
#     writing_data()