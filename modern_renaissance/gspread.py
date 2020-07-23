import logging
from modern_renaissance.log import logger_init

logger = logging.getLogger(__name__)


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


def update_gsheet_pandas(worksheet, df, range_name="A1", header=True):
    """Uploads a pandas DataFrame to a Google Sheets document

    Parameters
    ----------
    worksheet : Google Sheets worksheet
        The worksheet to push the df to
    df : pandas DataFrame
        The df to push up
    range_name: str
        The first cell to start the update
    header: bool
        Whether or not the df column headers should be included
    """
    logger.info(f"Updating cells on {worksheet.title}")
    columns = [df.columns.values.tolist()]
    values = df.values.tolist()
    cells = columns + values if header else values

    worksheet.update(range_name, cells)
    logger.log(44, f"Updated cells on {worksheet.title}")
