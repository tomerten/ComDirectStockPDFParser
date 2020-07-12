import os


class ComDirectParser:
    """
    Class to parse comdirect pdf files.

    Currently implemented are:
        - dividendgutschrift
        - kauf/verkauf wertpapier
        - steuermitteilung dividends
    """

    # CONSTANTS
    # currencies
    CUR = (
        "(AED|ARS|AUD|BDT|BGN|BRL|CAD|CHF|CNY|COP|CZK|DKK|EGP|"
        "EUR|GBP|GEL|GHS|HKDHUF|IDR|ILS|INR|JMD|JPY|KRW|KWD|KZTMAD|MXN|"
        "MYR|NGN|NOK|NZD|OMR|PEN|PHP|PKR|PLN|RON|RUB|SAR|SEK|SGD|THB|TRY|"
        "TWD|UAH|USD|VND|ZAR)"
    )

    # docutypes that can be parsed
    docuDict = {
        "Dividendengutschrift": "div",
        "Wertpapierkauf": "buy",
        "Wertpapierverkauf": "sell",
        "Steuerliche Behandlung": "tax",
    }


def __init__(self, inputlist: list) -> None:
    self.folders = []
    self.files = []
    self.filelist = []
    self.divparsed = []
    self.buysellparsed = []
    self.taxparsed = []
    # if inputlist is single file make a list out of it
    if isinstance(inputlist, list):
        pass
    else:
        inputlist = [inputlist]

    # check if entries in inputlist
    # have existing folders and files
    # select only the ones that do.
    for entry in inputlist:
        if os.path.isdir(entry):
            self.folders.append(entry)
        elif os.path.isfile(entry):
            self.files.append(entry)

    self.filelist = self.files.copy()
    for folder in self.folders:
        for file in os.listdir(folder):
            self.filelist.append(file)
