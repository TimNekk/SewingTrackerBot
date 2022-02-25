from loader import dp
from .whitelisted import IsWhitelisted
from .admin import IsAdmin


if __name__ == "filters":
    dp.filters_factory.bind(IsWhitelisted)
    dp.filters_factory.bind(IsAdmin)
