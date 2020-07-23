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
    logger.info(f"Getting cells from {workbook_name}/{worksheet_name}..")
    workbook = gc.open(workbook_name)
    worksheet = workbook.worksheet(worksheet_name)
    cells = worksheet.get_all_records()
    logger.info(f"Got cells from {workbook_name}/{worksheet_name}")

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
    logger.info(f"Updating cells on {worksheet.title}..")
    columns = [df.columns.values.tolist()]
    values = df.values.tolist()
    cells = columns + values if header else values

    worksheet.update(range_name, cells)
    logger.log(44, f"Updated cells on {worksheet.title}")


def get_letter_from_index(index: int) -> str:
    """Gets the nth letter in the alphabet

    Parameters
    ----------
    index : int
        Position in the alphabet

    Returns
    -------
    str
        Letter at given position in the alphabet
    """
    return chr(ord("@") + index)


def get_last_row(worksheet, col_num: int = 1) -> int:
    """Retrives the last nonblank row on Google Sheets

    Parameters
    ----------
    worksheet : Google Sheets worksheet
        The worksheet being queried
    col_num : int, optional
        Column that's indicative of the overall data length, by default 1

    Returns
    -------
    int
        The number of the last occupied row
    """
    col_values = worksheet.col_values(col_num)

    return len(col_values)


def get_last_col(worksheet, row_num: int = 1) -> int:
    """Retrives the last nonblank column on Google Sheets

    Parameters
    ----------
    worksheet : Google Sheets worksheet
        The worksheet being queried
    row_num : int, optional
        Row that's indicative of the overall data length, by default 1

    Returns
    -------
    int
        The number of the last occupied column
    """
    row_values = worksheet.row_values(row_num)

    return len(row_values)
