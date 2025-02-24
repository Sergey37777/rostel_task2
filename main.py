from config.logger import logger
from excel_sheet_reader import ExcelSheetReader
from config.constants.paths import EXCEL_FILE_PATH
from config.constants.variables import SHEET_NAME


@logger.catch
def main():
    logger.info("Start main function")
    df = ExcelSheetReader.read_excel_file(EXCEL_FILE_PATH, SHEET_NAME, skiprows=1, usecols=[0, 1, 2, 4])
    logger.info("Dataframe: \n{}", df)
    logger.info("End main function")


if __name__ == '__main__':
    main()
