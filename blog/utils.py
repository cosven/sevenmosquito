import mistune


def mdtohtml(text):
    return mistune.markdown(text)
