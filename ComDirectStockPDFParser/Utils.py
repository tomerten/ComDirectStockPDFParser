from tika import parser

def readRaw(_file):
    """
    Read raw pdf data from file.

    Parameters:
    -----------
    _file: str
        PDF file to open.
    """
    return parser.from_file(_file)

def stringToNumber(s):
    """
    Rudimentary string to float conversion
    if the string representation contains both 
    comma and dot.
    
    Pythonic way would be using locale, but
    leads to problems on mac, keep this
    method for the time being.

    Parameters:
    -----------
    s: str
        string to convert to float
    """
    s = float(s.replace('.','').replace(',','.'))
    return s