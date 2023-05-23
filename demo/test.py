import datetime

now = datetime.datetime.now() + datetime.timedelta(hours=8)
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

with open("demo/nowtime.txt", "w") as f:
    f.write(current_time)


