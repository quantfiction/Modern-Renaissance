from modern_renaissance.log import logger_init

import os
import logging
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CSSHTMLHeaderPreprocessor

logger = logging.getLogger(__name__)

IPYNB = ".ipynb"


def execute_notebook(notebook_name, **kwargs):
    logger.log(22, f"Executing {notebook_name}..")
    default_read_path = os.path.abspath(os.path.join(__file__, "..", "..", "notebooks"))
    default_write_path = os.path.abspath(
        os.path.join(__file__, "..", "..", "reports", "notebooks")
    )
    read_path = kwargs.get("read_path", default_read_path)
    write_path = kwargs.get("write_path", default_write_path)
    read_filename = os.path.join(read_path, notebook_name + IPYNB)
    write_filename = os.path.join(write_path, notebook_name + IPYNB)

    # read in notebook info
    with open(read_filename) as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    # execute notebook
    ep = ExecutePreprocessor(timeout=10000)
    ep.preprocess(nb, {"metadata": {"path": read_path}})

    # save to reports directory
    with open(write_filename, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    logger.info(f"Executed {notebook_name}")
