#!/usr/bin/python3
# Generate the HTML pages for each document. We load & parse each document
# found in the doc/ or rsd/ directories, and then generate a HTML page
# from it using the template.html file.

import os
import re


with open('template.html') as f:
    template = f.read()


def die(*msgs):
    print(*msgs)
    exit()


def replace_urls(content: str) -> str:
    # Replace <url> with <a href="url"></a> HTML tags.
    found = re.findall(r'<https?://[A-z0-9_\-.:/]*>', content)
    for f in found:
        n = f'<a href="{f[1:-1]}">&lt;{f[1:-1]}&gt;</a>'
        content = content.replace(f, n)
    return content


def parse_doc(path: str) -> dict:
    # Parse a document and return the parsed data. The first line of the
    # document is also the title.
    data = {}
    with open(path) as f:
        source = f.readlines()

    if len(source[0]) < 3:
        die(f'Failed to parse {path}')

    data['title'] = source[0][1:].strip()

    content = []
    i = 0
    while i < len(source):
        line = source[i]
        if line.startswith('#'):
            p = f'<h2>{line[2:-1]}</h2>'
            if line.startswith('##'):
                p = p.replace('h2>', 'h4>')
            content.append(p)
            i += 1
            continue

        # Collect a whole block. This means that there is text until the
        # next hash.
        local = []
        while i < len(source):
            local.append(line)
            line = source[i]
            if line.startswith('#'):
                break
            i += 1
        block = '<p>' + ''.join(local).strip() + '</p>'
        content.append(block)

    data['content'] = replace_urls('\n'.join(content))
    return data


def parse_rsd(path: str) -> dict:
    # Parse a RSD and return the parsed data. The first two lines contain the
    # title.
    with open(path) as f:
        source = f.readlines()

    title = 'RSD ' + path.split('-')[-1]
    content = f'<h2>{source[0].strip()}</h2>'
    source = source[2:]

    source = ''.join(source)
    content += f'\n<p>{source}</p>'

    return {'title': title, 'content': content}


def create_file_group(name, parse_f):
    for file in os.listdir(name):
        data = parse_f(name + '/' + file)
        html = template
        for k, v in data.items():
            html = html.replace(f'[${k}]', v)
        html = html.replace('\t', '    ')
        with open(f'docs/{name}/{file}.html', 'w') as f:
            f.write(html)
        print(f'Created: docs/{name}/{file}.html')


create_file_group('doc', parse_doc)
create_file_group('rsd', parse_rsd)
