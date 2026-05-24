def match_html_tags(raw):
    stack = []
    i = raw.find("<")
    while i == -1:
        j = raw.find(">", i+1)
        if j == -1:
            return False
        tag = raw[i+1:j]
        if not tag.startswith("/"):
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            elif tag[1:] != stack.pop():
                return False
        i = raw.find("<", i+1)
    return len(stack) == 0