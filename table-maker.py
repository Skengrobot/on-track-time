#!/usr/bin/python

from swim import time_percent
from swim import swim_parse

def make_table(conversion_percent):
    # Latex formatting for tables
    f.write("""\n\\begin{table}\n\centering\n\caption{\\textbf{Times """)
    f.write(str(conversion_percent))
    f.write(' percent off SNC FINAL on track times}}\n\\begin{tabular}{ |c||c|c|c|c|c|c|c|c|c|c| }\n\hline\n& \multicolumn{5}{|c|}{Female} & \multicolumn{5}{|c|}{Male}')
    f.write(' \\')
    f.write('\\')
    f.write('\n')
    f.write('\hline\n')
    for i in range(len(f_ages)):
        f.write(' & ')
        f.write(f_ages[i])
    for i in range(len(m_ages)):
        f.write(' & ')
        f.write(m_ages[i])
    f.write('\\')
    f.write('\\')
    f.write('\hline\n')

    # Table entries
    for event_key in data:
        f.write(event_key)
        for age_key in range(len(f_ages)):
            f.write(' & ')
            standard = data[event_key]['female'][f_ages[age_key]]
            conversion = time_percent(standard,conversion_percent)
            f.write(conversion)
        for age_key in range(len(m_ages)):
            f.write(' & ')
            standard = data[event_key]['male'][m_ages[age_key]]
            conversion = time_percent(standard,conversion_percent)
            f.write(conversion)
        f.write(""" \\""")
        f.write("""\\""")
        f.write('\n')

    f.write('\hline\n\end{tabular}\n\end{table}\n\n')




data = swim_parse('gold-times')
m_ages = ['18', '17', '16', '15', '14']
f_ages = ['17-18', '16', '15', '14', '13']

f = open('tables.tex','w')
f.seek(0)

# Latex file things
f.write("""
\documentclass{report}
\usepackage[english]{babel}
\usepackage{graphicx}
\usepackage[margin=2cm]{geometry}
\usepackage{setspace}
\usepackage{float}
\usepackage{rotating}

\\begin{document}
""")

make_table(2)
make_table(3)
make_table(5)

f.write("""
\end{document}""")
f.truncate()
f.close()
