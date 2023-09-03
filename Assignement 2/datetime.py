from datetime import datetime
dt = datetime.today();
print(dt)

d1 = dt.strftime("%d-%m-%y and %I:%M %p")
print(d1)

d1 = dt.strftime("%B %d %Y")
print(d1)

d1 = dt.strftime("%d/%b/%Y")
print(d1)

d1 = dt.strftime("%H:%M:%s")
print(d1)

d1 = dt.strftime("%d-%m-%y")
print(d1)

