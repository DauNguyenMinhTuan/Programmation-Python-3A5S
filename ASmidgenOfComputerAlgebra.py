# A Perfect Match
from dataclasses import dataclass

@dataclass
class BinExpr:
    a: object
    b: object

class BinOp(BinExpr):
    pass

@dataclass
class UnOp:
    a: object