def get_cells(gc, workbook_name, worksheet_name):
    """Retrieves all cells from a Google Sheets document as a dict-of-dicts

    Parameters
    ----------
    gc : gspread.client.Client
        An instance to communicate with Google API
    workbook_name : str
        Name of the Google Sheets workbook
    worksheet_name : str
        Name of the Google Sheets sheet/tab
    """
    workbook = gc.open(workbook_name)
    worksheet = workbook.worksheet(worksheet_name)
    cells = worksheet.get_all_records()

    return cells


def update_gsheet_pandas(worksheet, df):
    """Uploads a pandas DataFrame to a Google Sheets document

    Parameters
    ----------
    worksheet : Google Sheets worksheet
        The worksheet to push the df to
    df : pandas DataFrame
        The df to push up
    """
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
