while index < len(text):
    if text[index] == "<":
        tag = re.split(r'(?<=[>])\s*', text[index:])[0]
        if any(tag in tuple for tuple in tag_list):
            print('tag found:' + tag)
            index += len(tag)
            contents = re.split(fr'(?<=[{tuple[1]}])\s*', text[index:])[0]
            print('contents found:' + contents)
            index += (len(tuple[1]) + len(contents))
        
    else:
        index += 1