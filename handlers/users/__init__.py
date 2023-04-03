from .start import dp
from .buttons import dp
from .anynum import dp
from .tt import dp
from .binfo import dp
from .admin import dp
from .donate import dp

# в самом низу, т. к. использует message handler с пустым значением
from .fb import dp

# специальная переменная, которая используется для указания того, какие имена должны
# быть экспортированы/импортированы при использовании синтаксиса from <module> import *
__all__ = ['dp']