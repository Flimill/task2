import sys

import panflute
from panflute import run_filter

var = set()


def upper_str(elem, doc):
    if isinstance(elem, panflute.Str):
        elem.text = elem.text.upper()


def file_processing(element, doc):
    if isinstance(element, panflute.Header):
        text = panflute.stringify(element)
        if text in header:
            sys.stderr.write("Повторяющиеся заголовки : \"" + element + "\"")
        else:
            header += element
    if isinstance(element, panflute.Str) and element.text.lower() == "bold":
        return panflute.Strong(element)
    if isinstance(element, panflute.Header) and element.level <= 3:
        return element.walk(upper_str)


def main(doc=None):
    return panflute.run_filter(file_processing, doc=doc)


if __name__ == "__main__":
    main()
