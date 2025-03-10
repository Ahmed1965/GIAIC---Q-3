import pandas as pd
tables = pd.read_html('https://www.w3schools.com/python/python_operators.aspx')
print(tables[0])
