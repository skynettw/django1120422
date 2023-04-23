from django.shortcuts import render  # (渲染: 1.來自於瀏覽器的請求 2.HTML範本 3.要送過去的變數資料)
from django.shortcuts import redirect
import random
from mysite.models import News, BodyInfo

def index(request):
    return render(request, "index.html", locals())

def bodyinfo(request):
    rawdata = BodyInfo.objects.all()
    data = list()
    for item in rawdata:
        temp = dict()
        temp['name'] = item.name 
        temp['height'] = item.height
        temp['weight'] = item.weight
        temp['bmi'] = round(int(item.weight) / (int(item.height)/100)**2, 2)
        data.append(temp)
    return render(request, "bodyinfo.html", locals())

def shownews(request, id):
    try:
        news = News.objects.get(id=id)
    except:
        return redirect("/mynews/")

    return render(request, "shownews.html", locals())

def mynews(request):
    news = News.objects.all()
    return render(request, "mynews.html", locals())

def lotto(request):
    numbers = [i for i in range(1, 50)]   # 先產生一個 1~49 的串列
    random.shuffle(numbers)               # 打亂串列裡面各項目的順序
    numbers = numbers[:6]                 # 只取出49個項目裡面的前6個（第0個到第5個）
    return render(request, "lotto.html", locals())

def lucky(request):
    name = random.choice(["王小明", "林小華", "林書豪"])
    lucky = random.randint(1, 49)
    return render(request, "lucky.html", locals())  # locals()會打包所有區域內的變數
