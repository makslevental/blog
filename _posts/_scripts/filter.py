#!/usr/bin/env python

import sys

import os
import re
import shutil
import io
import sys
from subprocess import call
from tempfile import mkdtemp

from pandocfilters import toJSONFilter, Para, Para, RawBlock, Div, Math, Link, stringify, Str

from bs4 import BeautifulSoup
from tika import parser
import re

def ppprint(x, lbl=""):
    sys.stderr.write(f"---{lbl}---: {str(x)}\n\n")

label_to_fignum = {}

file_path = os.environ.get('FLOATS_LABELED', None)
if file_path is not None:
    data = parser.from_file(file_path, xmlContent=True)
    xhtml_data = BeautifulSoup(data['content'], features="html.parser")
    for page, content in enumerate(xhtml_data.find_all('div', attrs={'class': 'page'})):
        for fig_r in [r".*fig:.*", r".*tab:.*", r".*lst:.*"]:
            for fig_label in re.findall(fig_r, str(content).replace("<p>", "").replace("</p>", ""), re.MULTILINE):
                label_to_fignum[fig_label] = page+1


ppprint(label_to_fignum, "label_to_fignum")

N_FIGS = 0
N_TABS = min([v for k, v in label_to_fignum.items() if "tab:" in k]) - 1

fig = f"""
<p align="center">
  <img src="../images/{os.environ.get('PROJECTNAME', "no_project_name")}/{{path}}"/>
</p>
"""

def html(x):
    return RawBlock('html', x)


# ppprint(label_to_fignum, "labels")

def link(href, label):
    return Link(
            ["",[],[("reference-type","ref"),("reference",href)]],
            [Str(label)],
            [href, ""]
            )


def tikz(key, value, format, meta):
    global N_FIGS, N_TABS
    if key == 'Div':
        if "figure*" in str(value):
            N_FIGS += 1
            [[ident, classes, kvs], _contents] = value
            newcontents = [html(fig.format(path=f"float{N_FIGS:03}.png"))]
            ident = f"fig:{N_FIGS}"
            return Div([ident, classes, kvs], newcontents)
    if key == 'Table':
            N_TABS += 1
            newcontents = [html(fig.format(path=f"float{N_TABS:03}.png"))]
            ident = f"tab:{N_TABS}"
            return Div([ident, [], []], newcontents)
    if key == 'Link':
        label = value[-1][0].replace("#", "")
        if len(label.split(",")) > 1:
            links = []
            for label in label.split(","):
                pref = label.split(":")[0]
                # ppprint(pref, "pref")
                links.append(
                    link(
                        href=f"#{pref}:{label_to_fignum[label]}",
                        label=f"{label_to_fignum[label]}"
                    ),
                )
                links.append(Str(","))

            del links[-1]
            return links
        if label in label_to_fignum:
            pref = label.split(":")[0]
            value[-2][0]['c'] = f"{label_to_fignum[label]}"
            value[-1][0] = f"#{pref}:{label_to_fignum[label]}"
        if "eq:" in label:
            return Math({'t': 'InlineMath'}, f"\eqref{{{label}}}")
        if "sec:" in label:
            value[-2][0]['c'] = value[-2][0]['c'][1:-1].split(":")[1]

    if key == 'Span' and "label" in str(value):
        value[-1][0]['c'] = ""
    if key == 'Para':
        ret = []
        rets = []
        for v in value:
            if v['t'] == 'Math' and v['c'][0]['t'] == 'DisplayMath':
                rets.append(Para(ret))
                rets.append(Para([v]))
                ret = []
            else:
                ret.append(v)
        if len(ret):
            ret = Para(ret)
            rets.append(ret)
        if len(rets):
            return rets

# Link ("",[],[("reference-type","ref"),("reference","sec:background")]) [Str "[sec:background]"] ("#sec:background","")

if __name__ == "__main__":
    toJSONFilter(tikz)
