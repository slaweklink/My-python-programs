from calendar import weekday  #shows what day of the week is it
from datetime import date
import datetime

y,m,d = (input().split(","))
y = int(y)
m = int(m)
d = int(d)
dzis = datetime.datetime(y,m,d)

print(dzis.weekday())
