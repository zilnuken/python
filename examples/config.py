import sys

license = ''
if sys.platform == "linux" or sys.platform == "linux2":
    # linux
    license = 't0127lQMAAHB5ELMdLtyN7wvYFuvlOWfIdUteVciqXOyCXHhX9b2qE8N3AJIFPtT4/R7/yTAgaJzVpxInoe2LvUwnQ7626O54Z+WunA+pzWmY0zCnYU7DTMNMw0zDTMNMwyzDLMMswyzDXO+aP1GbjUZ1E6gavtW/6eiNh8YF2F+19A=='
elif sys.platform == "darwin":
    # OS X
    license = 't0068NQAAAKrcxSxZwCY7qwBNDJJXAG3rFcJZTDsCdTHB2TlI0f1DvBg34MazLhAqhf6D2iE60OnWk9imYMc0inxb9OXWcrY='
elif sys.platform == "win32":
    # Windows
    license = 't0068NQAAAJwEbwJjt0+DiC2gJpQN4VQUhYTBmazlOU0RgWzDins2JUhtO6TK2Kj/Ck9+z5FlwuHn0KLK1NvkXYvThosPYog='

barcodeTypes = 0x3FF | 0x2000000 | 0x4000000 | 0x8000000 | 0x10000000  # 1D, PDF417, QRCODE, DataMatrix, Aztec Code
