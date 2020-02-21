# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse#, HttpResponseRedirect
#from django.template import RequestContext

#from io import BytesIO
from . import models
import json
import requests
from PIL import Image
import copy
import operator

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method=='POST':
        image_data = request.FILES['imgInp']
        img_bytes = image_data.file
        img_bytes_gen = copy.deepcopy(img_bytes)

        #im = Image.open(request.FILES['imgInp'])
        #width, height = im.size
        #print(width, height)

        # Generic Model
        headers_gen = {
            "Ocp-Apim-Subscription-Key": "d205fc45d1594a088b0ca92ceb1d6e41",
            "Content-Type": "application/octet-stream"
        }
        results_gen = requests.post("https://southcentralus.api.cognitive.microsoft.com/vision/v2.0/describe?maxCandidates=1&language=en", 
        data=img_bytes_gen, headers=headers_gen).text
        res_gen_j = json.loads(results_gen)
        desc = res_gen_j["description"]["captions"][0]["text"]

        headers = {
            "Prediction-Key": "a8b1a72e2caa4334a8ed8a2be688345f",
            "Content-Type": "application/octet-stream"
        }
        results = requests.post("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/402c13e3-b8ed-4d8f-8e7f-ca09addd26d0/classify/iterations/Iteration3/image", 
        data=img_bytes, headers=headers).text
        #print(results.text)
        #print(type(results))
        res_j = json.loads(results)
        ress = {"blueprint": 0, "house": 0, "others": 0}
        for i in res_j["predictions"]:
            ress[i["tagName"]] = i["probability"]
        
        key_max = max(ress.items(), key=operator.itemgetter(1))[0]
        if key_max == "others":
            ress["aux_txt"] = desc
            ress["ind"] = "yes"
        else:
            ress["ind"] = "no"

        # results = tf_dep.predict_image_class(im
        # g_bytes.getvalue())
        models.Image.objects.create(img=image_data, house=ress['house'], blueprint=ress['blueprint'], others=ress['others']) # create and save in a single step

        im = Image.open(request.FILES['imgInp'])
        width, height = im.size
        if width<100 or height<100:
            return HttpResponse(status=500)

        results_str = json.dumps(ress)
        return HttpResponse(results_str)