def remove_tags(html_file, result=open('/Users/jan/Desktop/cleaned_text.txt', 'w', encoding='utf-8')):
    html_file = html_file.replace(html_file[html_file.find('<'):html_file.find('>') + 1], "")
    if '<' and '>' in html_file:
        remove_tags(html_file)
    else:
        result.write(html_file)
        result.close()
    return None


def remove_empty_lines(file, result=open('/Users/jan/Desktop/cleaned_text2.txt', 'w', encoding='utf-8')):
    for i in range(len(file)):
        file[i] = file[i].strip()
    f = []
    for j in range(len(file)):
        if file[j] != "":
            f.append(file[j])
    text = '\n'.join(f)
    result.write(text)
    result.close()
    return None


raw_text = open('/Users/jan/Desktop/draft.html', 'r', encoding='utf-8')
ht = raw_text.read()
remove_tags(ht)
new_text = open('/Users/jan/Desktop/cleaned_text.txt', 'r', encoding='utf-8')
nt = new_text.readlines()
remove_empty_lines(nt)