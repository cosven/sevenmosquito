import markdown2


def mdtohtml(text):
    return markdown2.markdown(text, extras=['fenced-code-blocks'])
