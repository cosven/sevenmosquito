from .consts import ThemeDict


def expose_consts(request):
    return {
        'ThemeDict': ThemeDict
    }
