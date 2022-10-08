# Ваша задача написать функцию,
# которая прочитает заданный файл, очистит текст от html-тэгов, и запишет этот текст в другой файл.
# html-тэг всегда начинается с "<" и заканчивается на ">" Т.е. нужно удалить эти символы и все, что между ними.
# Функция получает на вход два параметра - имя файла, который нужно очистить,
# и имя файла, куда нужно записать очищенный текст.
# Имя файла, куда нужно писать, можно задать значением по умолчанию.
# Пример файлов во вложении - файл который нужно очистить (расширение html) и файл, с очищенным текстом.
# Доп. задача для тех, кто захочет усложнить решение - попробуйте убрать строки, в которых нет информации.

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