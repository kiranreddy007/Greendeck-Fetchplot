def FetchPlot(key, x_axis, y_axis):

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    from pprint import pprint
    import matplotlib.pyplot as plt

    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "creds.json", scope)

    client = gspread.authorize(creds)
    try:

        sheet = client.open_by_key(key).sheet1

        col_names = sheet.row_values(1)
        try:
            x1 = sheet.col_values(col_names.index(x_axis)+1)

            y1 = sheet.col_values(col_names.index(y_axis)+1)

            plt.plot(x1, y1)
            plt.xlim(0, 13)
            plt.ylim(0, 13)
            plt.savefig('chart.png')
        except ValueError:
            print("INVALID X-axis or Y-axis or Not Found Corresponding column Name")

    except gspread.exceptions.APIError:
        print('sheeet Key Invalid or Not Found ')
