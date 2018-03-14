import mistune
from mistune_contrib.highlight import HighlightMixin
from mistune_contrib.math import MathRendererMixin


class MDRenderer(HighlightMixin, MathRendererMixin, mistune.Renderer):
    pass


renderer = MDRenderer()


def mdtohtml(text):
    markdown = mistune.Markdown(renderer=renderer)
    return markdown(text)
