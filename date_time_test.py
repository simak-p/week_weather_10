from datetime import datetime, timedelta

delta = timedelta(hours=1)
print(delta)
start_data = datetime(2022, 7, 8, 18, 10, 55)
end_data = datetime.now()
delta1 = end_data - start_data
print(start_data)
print(end_data)
print(delta1)
if delta1 > delta:
    print(True)
else:
    print(False)
