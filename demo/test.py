import datetime

now = datetime.datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open("nowtime.txt", "w") as f:
    f.write(current_time)


