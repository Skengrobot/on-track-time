#!/usr/bin/python

from swim import time_percent
from swim import swim_parse

conversion_percent = 3

data = swim_parse()
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

# Latex formatting for tables
f.write("""
\\begin{table}
\centering
\caption{\\textbf{Times """)
f.write(str(conversion_percent))
f.write(""" percent off SNC GOLD on track times}}
\\begin{tabular}{ |c|c|c|c|c|c|c|c|c|c|c| }
\hline
& \multicolumn{5}{|c|}{Female} & \multicolumn{5}{|c|}{Male}""")
f.write(""" \\""")
f.write("""\\
""")
f.write("""
\hline
""")
for i in range(len(f_ages)):
    f.write(' & ')
    f.write(f_ages[i])
for i in range(len(m_ages)):
    f.write(' & ')
    f.write(m_ages[i])
f.write(""" \\""")
f.write("""\\
""")

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

f.write("""
\hline
\end{tabular}
\end{table}
\end{document}""")
f.truncate()
f.close()
