#!/usr/bin/python3
# Generate a HTML page from the .rst doc files

import docutils.core
import os
import re

class Style:
    fg = "#4c4f69"
    bg = "#dce0e8"
    bg_page = "#eff1f5"
    bg_shadow = "#dce0e8"
    link = "#04a5e5"
    link_hover = "#fe640b"


additional_style = f"""
body {{
    background-color: {Style.bg};
    margin: 0;
}}

.document {{
    width: 50%;
    padding: 20px;
    margin: auto;
    margin-top: 0;
    margin-bottom: 0;
    background-color: {Style.bg_page};
    color: {Style.fg};
    box-shadow: 5px 5px 10px {Style.bg_shadow};
}}

.section {{
    margin-top: 2em;
}}

.section h1 {{
    font-family: monospace !important;
    font-size: 1.5em !important;
    text-decoration: underline dotted #7f849c;
}}

a {{
    font-family: monospace;
    color: {Style.link};
    text-decoration: underline #9399b2;
}}

a:visited {{
    color: {Style.link};
    text-decoration: underline #9399b2;
}}

a:hover {{
    color: {Style.link_hover};
    text-decoration: underline dotted #9399b2;
}}
"""


def list_dir_recursive(dir: str) -> list:
    files = os.listdir(dir)
    for f in files:
        if os.path.isdir(f):
            files.extend([f + '/' + x for x in list_dir_recursive(f)])
    return files


# Generate the web pages
files = sorted(list_dir_recursive('.'))
links = {}

if not os.path.exists('docs'):
    os.mkdir('docs')

for doc in files:
    if not doc.endswith('.rst'):
        continue
    if doc.startswith('docs'):
        continue

    basename = doc.rsplit('.', 1)[0]
    dest = f'docs/{basename}.html'

    move_backs = basename.count('/')

    dest_dir = os.path.dirname(dest)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    print('Generating', dest)

    docutils.core.publish_file(
        source_path=f'{basename}.rst',
        destination_path=dest,
        writer_name='html'
    )

    # Add custom styles
    with open(dest) as f:
        html = f.read()

    tag = '<style type="text/css">'
    html = html.replace(tag, tag + additional_style)

    back = '../' * move_backs
    link_back = f'<a href="{back}index.html">&lt;&lt;&lt; Back</a>'

    found = re.search(r'<h1 class="title">.*</h1>', html)
    if found:
        html = html.replace(found.group(0), found.group(0) + link_back)

    with open(dest, 'w') as f:
        f.write(html)

    # Try to read :Desc: and :Name: from the .rst file to get the symbols
    link = f'<a href="{basename}.html">'
    name = ''
    desc = ''

    with open(doc) as f:
        for line in f.readlines():
            if not name and line.strip().startswith(':Name:'):
                name = line[len(':Name:'):].strip()
            if not desc and line.strip().startswith(':Desc:'):
                desc = line[len(':Desc:'):].strip()

    # Add the page name
    link += (name if name else doc) + '</a>'
    if desc:
        link += ' - ' + desc
    link += '<br>'

    links[name if name else doc] = link


# Sort & join the links
link_keys = sorted(links.keys())
html_links = ''
for key in link_keys:
    html_links += links[key]
    html_links += '\n'


index_style = f"""
a {{
    font-family: monospace;
    color: {Style.link};
    text-decoration: underline #9399b2;
}}

a:visited {{
    color: {Style.link};
    text-decoration: underline #9399b2;
}}

a:hover {{
    color: {Style.link_hover};
    text-decoration: underline dotted #9399b2;
}}

body {{
    background-color: {Style.bg};
    margin: 0;
}}

.document {{
    width: 50%;
    margin: auto;
    padding: 20px;
    background-color: {Style.bg_page};
    color: {Style.fg};
    box-shadow: 5px 5px 10px {Style.bg_shadow};
}}
"""

index_source = f"""
<html>
    <head>
        <title>mini-rose documentation</title>
        <style>
{index_style}
        </style>
    </head>
    <body>
    <div class="document">
        <h1>mini-rose documentation</h1>
        <p>
            This webpage is a a collection of Reference Specification Documents
            (RDSs), random documents about code, little info messages and general
            software documentation.
        </p>
        <hr>
        <p>
            Here is the list of all generated HTML pages from the .rst files:
        </p>
{html_links}
    </div>
    </body>
</html>
"""

with open('docs/index.html', 'w') as f:
    f.write(index_source)
