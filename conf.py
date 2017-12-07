import os

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    html_theme = 'yeti'
else:
    html_theme = 'yeti'
