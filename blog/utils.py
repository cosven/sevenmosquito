import re

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


class TasklistRenderMixin:

     def list_item(self, text):
         """render list item with task list support"""

         # list_item implementation in mistune.Renderer
         old_list_item = mistune.Renderer.list_item
         new_list_item = lambda _, text: '<li class="task-list-item">%s</li>\n' % text

         task_list_re = re.compile(r'\[[xX ]\] ')
         m = task_list_re.match(text)
         if m is None:
             return old_list_item(self, text)
         prefix = m.group()
         checked = False
         if prefix[1].lower() == 'x':
             checked = True
         if checked:
             checkbox = '<input type="checkbox" class="task-list-item-checkbox" checked disabled/> '
         else:
             checkbox = '<input type="checkbox" class="task-list-item-checkbox" disabled /> '
         return new_list_item(self, checkbox + text[m.end():])


class MDRenderer(HighlightMixin,
                 # MathRendererMixin,
                 TocMixin,
                 TasklistRenderMixin,
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
