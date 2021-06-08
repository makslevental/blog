#!/usr/bin/env python

import sys

import os
import re
import shutil
import sys
from subprocess import call
from tempfile import mkdtemp

from pandocfilters import toJSONFilter, Para, Image, get_filename4code, get_extension, Para, Span, RawBlock, Div, Math

from bs4 import BeautifulSoup
from tika import parser
import re

file_path = os.environ['FLOATS_LABELED']

label_to_fignum = {}
data = parser.from_file(file_path, xmlContent=True)
xhtml_data = BeautifulSoup(data['content'], features="html.parser")
for page, content in enumerate(xhtml_data.find_all('div', attrs={'class': 'page'})):
    for fig_label in re.findall(r"fig:.*", str(content).replace("</p>", ""), re.MULTILINE):
        label_to_fignum[fig_label] = page+1



N_FIGS = 0

fig = f"""
<p align="center">
  <img src="../images/{os.environ['PROJECTNAME']}/{{path}}"/>
</p>
"""

def html(x):
    return RawBlock('html', x)

def ppprint(x, lbl=""):
    sys.stderr.write(f"---{lbl}: {str(x)}\n")

ppprint(label_to_fignum, "labels")

def tikz(key, value, format, _):
    global N_FIGS
    if key == 'Div':
        if "figure*" in str(value):
            N_FIGS += 1
            [[ident, classes, kvs], contents] = value
            newcontents = [html(fig.format(path=f"float{N_FIGS:03}.png"))]
            ident = f"fig:{N_FIGS}"
            return Div([ident, classes, kvs], newcontents)
    if key == 'Table':
            N_FIGS += 1
            newcontents = [html(fig.format(path=f"float{N_FIGS:03}.png"))]
            ident = f"fig:{N_FIGS}"
            return Div([ident, [], []], newcontents)
    if key == 'Link':
        label = value[-1][0].replace("#", "")
        if label in label_to_fignum:
            value[-2][0]['c'] = f"{label_to_fignum[label]}"
            value[-1][0] = f"#fig:{label_to_fignum[label]}"
        if "eq:" in label:
            return Math({'t': 'InlineMath'}, f"\eqref{{{label}}}")
        elif "sec:" in label:
            value[-2][0]['c'] = value[-2][0]['c'][1:-1].split(":")[1]
    if key == 'Span' and "label" in str(value):
        value[-1][0]['c'] = ""
    if key == 'Para':
        ret = []
        rets = []
        for v in value:
            if v['t'] == 'Math' and v['c'][0]['t'] == 'DisplayMath':
                # sys.stderr.write(f"---math {len(value)}: {str(value)}\n")
                rets.append(Para(ret))
                rets.append(Para([v]))
                ret = []
            else:
                ret.append(v)
        if len(ret):
            ret = Para(ret)
            rets.append(ret)
        # sys.stderr.write(f"{rets}\n\n")
        if len(rets):
            return rets


if __name__ == "__main__":
    toJSONFilter(tikz)
