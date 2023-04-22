from django.shortcuts import render  # (渲染: 1.來自於瀏覽器的請求 2.HTML範本 3.要送過去的變數資料)
import random

def index(request):
    return render(request, "index.html", locals())

def lotto(request):
    numbers = [i for i in range(1, 50)]
    random.shuffle(numbers)
    numbers = numbers[:6]
    return render(request, "lotto.html", locals())

def lucky(request):
    name = random.choice(["王小明", "林小華", "林書豪"])
    lucky = random.randint(1, 49)
    return render(request, "lucky.html", locals())  # locals()會打包所有區域內的變數
