from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.template import loader
from django.middleware.csrf import get_token
from .models import User
import os
import random
import string
from . import face_Identifier,filter
import json

def index(request):
    
    csrf_token = get_token(request)
    context = {'csrf_token': csrf_token}
    template = loader.get_template('index.html')
    rendered_template = template.render(context, request)
    return HttpResponse(rendered_template)

def getPic(request):
    pic=request.session.get("file")
    path="/static/"+str(pic)
    return HttpResponse(path)

def result(request):
    data = request.session.get("filtered")
    print(data)
    request.session.clear()

    transformed_data = {
        "true": [],
        "false": []
    }

    for name, value in data.items():
        if value:
            transformed_data["true"].append(name.split()[0])
        else:
            transformed_data["false"].append(name)

    return JsonResponse(transformed_data, safe=False)


def process(request):
    p = os.getcwd() + "/main/static/"
    filename=request.session.get("file")
    main_image_path = p +  str(filename)
    faces = {
        "Emma Watson": p + "emma.png",
        "Donald Trump": p + "trump.png",
        "Chris Evans": p + "chris.png",

    }
    social_distance_checker = face_Identifier.SocialDistanceChecker(main_image_path, faces)
    distances = social_distance_checker.check_social_distance()
    formatted_distances = {}
    print(distances)

    for key, value in distances.items():
        names = key.split('&')
        formatted_name = f"{names[0]}&{names[1]}"
        formatted_distances[formatted_name] = value

    social_distance_filter = filter.SocialDistanceFilter(formatted_distances)
    filtered_distances = social_distance_filter.filter_social_distance(distance_threshold=500)
    request.session["filtered"]=filtered_distances
    return  JsonResponse({"status":"ok"}, safe=False)
        

def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        
        random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        _, extension = os.path.splitext(image.name)
        new_filename = random_filename + extension
        
        upload_path = os.getcwd()+"/main/static/"+str(new_filename)
        
        with open(upload_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        request.session["file"]=new_filename
        
        return JsonResponse({'success': True, 'filename': new_filename})
    
    return JsonResponse({'success': False, 'message': 'No image file provided'})