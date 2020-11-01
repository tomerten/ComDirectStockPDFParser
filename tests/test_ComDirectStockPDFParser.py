import os

from ComDirectStockPDFParser.Utils import readRaw

kauffiles = []
base = "/Volumes/Docu_Tom/Stocks/BuySell/2018/Tom_ComDirect/Bill/"
for f in os.listdir(base):
    if f.startswith("Wertpapier"):
        kauffiles.append(os.path.join(base, f))


def test_readRaw() -> None:
    print(kauffiles[0])
    assert False
