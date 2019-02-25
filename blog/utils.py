import mistune
from mistune_contrib.highlight import HighlightMixin
from mistune_contrib.math import MathRendererMixin
from mistune_contrib.toc import TocMixin


# patch mistune: render table with indent in list
# ::
#   add two rules ('table' and 'nptable') to list_rules,
#   they should be placed before text rule.
old_list_rules = mistune.BlockLexer.list_rules
mistune.BlockLexer.list_rules = (
    'newline', 'block_code', 'fences', 'lheading', 'hrule',
    'block_quote', 'list_block', 'block_html', 'nptable', 'table', 'text',)


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
