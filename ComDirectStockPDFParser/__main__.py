import sys

from ComDirectStockPDFParser.ComDirectStockPDFParser import fib
from . import log

if __name__ == "__main__":
	log.setup()

	n = int(sys.argv[1])

	log.info(n)

	print(fib(n))
