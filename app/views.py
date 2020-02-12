from django.shortcuts import render
from app.forms import EpochForm
from django.http import HttpResponse
import time


def get_time(request):
    if request.method == "POST":
        length = len(request.POST.get('epochtime'))
        if length == 10 or length == 19:
            form = EpochForm(request.POST)
            form1 = EpochForm()
            tim = int(request.POST.get('epochtime'))
            micro = tim / 1000000000
            mod = tim % 1000000000
            # print(mod)
            # print(micro)
            if mod ==0:
               mod = '0'*9
            mod = str(mod)
            list = ([str(mod)[i:i + 3] for i in range(0, len(str(mod)), 3)])
            milisec = (list[0]) if length > 10 else 0
            microsec = (list[1])  if length > 10 else 0
            nanosec = (list[2])  if length > 10 else 0
            day = time.strftime("%a", time.localtime(micro))
            date = time.strftime("%d", time.localtime(micro))
            month = time.strftime("%b", time.localtime(micro))
            year = time.strftime("%Y", time.localtime(micro))
            hours = time.strftime("%H", time.localtime(micro))
            minute = time.strftime("%M", time.localtime(micro))
            sec = time.strftime("%S", time.localtime(micro))

            # print(day)
            # print(date)
            # print(month)
            # print(year)
            # print(hours)
            # print(minute)
            # print(sec)
            # print(milisec)
            # print(microsec)
            # print(nanosec)

            data = {'day': day, 'date': date, 'month': month, 'year': year, 'hour': hours,
                    'minute': minute, 'seconds': sec, 'mili': milisec, 'micro': microsec, 'nanosec': nanosec}

            return render(request, '../templates/index.html', {'data': data, 'form': form1})

        else:
            val = {'validation': 'Please enter Epoch time in Seconds or Nano seconds'}
            form = EpochForm()
            return render(request, '../templates/index.html', {'val': val, 'form': form})



    else:
        form = EpochForm()
        return render(request, '../templates/index.html', {'form': form})


