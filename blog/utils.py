import mistune
from mistune_contrib.highlight import HighlightMixin
from mistune_contrib.math import MathRendererMixin
from mistune_contrib.toc import TocMixin


class MDRenderer(HighlightMixin,
                 MathRendererMixin,
                 TocMixin,
                 mistune.Renderer):
    pass


renderer = MDRenderer()


def mdtohtml(text, toc=False):
    renderer.reset_toc()
    markdown = mistune.Markdown(renderer=renderer)
    body = markdown.parse(text)
    if not toc:
        return body

    toc = renderer.render_toc(level=5)
    return body, toc
