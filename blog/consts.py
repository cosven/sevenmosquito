"""
    blog.consts
    ~~~~~~~~~~~

    consts for blog app.
"""


from enum import Enum


class Themes(Enum):
    mist = 'Mist'
    muse = 'Muse'
    pisces = 'Pisces'


ThemeDict = {k: v.value for k, v in Themes.__members__.items()}
ThemeChoices = [(v.value, k) for k, v in Themes.__members__.items()]
