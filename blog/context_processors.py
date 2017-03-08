from .consts import Theme


def expose_consts(request):
    return {
        'Theme': Theme
    }
