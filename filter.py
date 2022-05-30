import sys
import panflute

headers = set()


def file_processing(element, doc):
    if isinstance(element, panflute.Header):
        text = panflute.stringify(element)
        if text in headers:
            sys.stderr.write("Повторяющиеся заголовки : \"" + text + "\"" + "\n")
        else:
            headers.add(text)
    if isinstance(element, panflute.Str) and element.text == "BOLD":  # Ищу слово в том же регистре, которое в задании
        return panflute.Strong(element)
    if isinstance(element, panflute.Header) and element.level <= 3:
        return element.walk(upp_elements)


def upp_elements(element, doc):
    if isinstance(element, panflute.Str):
        element.text = element.text.upper()


def main(doc=None):
    return panflute.run_filter(file_processing, doc=doc)


if __name__ == "__main__":
    main()
