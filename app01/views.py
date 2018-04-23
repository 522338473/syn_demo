from django.shortcuts import render, HttpResponse
from django.db import transaction
import logging
import json
import requests
import hashlib
from io import BytesIO
import random
from PIL import Image, ImageDraw, ImageFont


logger = logging.getLogger(__name__)  # 输出日志





def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        return HttpResponse("post提交数据")





def get_validCode_img(request):
    img = Image.new(mode="RGB", size=(120, 40),
                    color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # 获取一张颜色随机的RGB格式的给定图像
    draw = ImageDraw.Draw(img, mode="RGB")
    # 定义一个画布对象，以后就在这张画布上操作
    draw.line((10, 30, 120, 20), fill="black")
    font = ImageFont.truetype("static/bootstrap-3.3.7/fonts/kumo.ttf", 25)
    # 定义画笔的字体
    valid_list = []
    for i in range(4):
        # 随机产生四个纯数字验证码，并添加到valid_list里
        randon_num = str(random.randint(0, 9))
        draw.text([5 + i * 24, 10], randon_num,
                  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), font=font)
        valid_list.append(randon_num)

    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    # data是后端处理的图片二进制图片数据
    valid_str = "".join(valid_list)
    print("此次验证码是：", valid_str)

    request.session["keepValiCode"] = valid_str
    print(request.session.get("keepValiCode"))
    request.COOKIES["keepValiCode"] = valid_str
    return HttpResponse(data)


def get_ajax(request):
    msg = request.session.get("keepValiCode")
    return HttpResponse(msg)

"""
def outter(flag):
    def wrapper(func):
        def inner(*args,**kwargs):
            if flag:
                print('执行函数之前需要执行的步骤')
            res = func(*args,**kwargs)
            if flag:
                print('执行函数之后需要执行的步骤')
            return res
        return inner
    return wrapper
"""

