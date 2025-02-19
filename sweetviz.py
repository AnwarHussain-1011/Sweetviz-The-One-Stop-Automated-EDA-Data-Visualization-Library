# -*- coding: utf-8 -*-
"""SweetViz.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ju0XL6q1dDFOz6DdQyb57EwB755mhHsg
"""

!pip install sweetviz

import seaborn as sns
df=sns.load_dataset('titanic')

df.head()



import sweetviz as sv

my_report = sv.analyze(df)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"

df.head()