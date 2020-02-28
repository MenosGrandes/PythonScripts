from pendulum import datetime,timezone
from ics import Calendar, Event
c = Calendar()

_timezone = timezone('Europe/Warsaw')

a = [datetime(2020, 3 ,8),datetime(2020, 3 ,15),datetime(2020, 3 ,29),datetime(2020, 4 ,5),datetime(2020, 4 ,19),datetime(2020, 4 ,26),datetime(2020, 5 ,10),datetime(2020, 5 ,24),datetime(2020, 6 ,7),datetime(2020, 6 ,21)]
for data in a:
    e = Event()
    e.name = "AK_445"
    data = _timezone.convert(data)
    e.begin = data.set(hour=16,minute=30)
    e.end = data.set(hour=18,minute=45)
    c.events.add(e)
    
    
with open('poli.ics', 'w') as my_file:
    my_file.writelines(c)