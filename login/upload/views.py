import io
import os
import json
import spacy
from google.cloud import vision
from google.cloud.vision import types


from django.shortcuts import render


from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

  
# Create your views here. 
def bill_image_view(request): 
  
    if request.method == 'POST': 
        form = BillForm(request.POST, request.FILES)

       
        if form.is_valid(): 
            form.save()
            
            client = vision.ImageAnnotatorClient()

            # The name of the image file to annotate
            filename="/root/Desktop/project/tez/djangobackend/login/media/images/"+str(request.FILES['bill_Main_Img'])
            file_name = os.path.abspath(filename)
           
            print("hello")
            print(request.FILES['bill_Main_Img'])
            
            # Loads the image into memory
            
            with io.open(file_name, 'rb') as image_file:
                print("done")
                content = image_file.read()
            
            #content =  request.FILES #.read()

            image = vision.types.Image(content=content)

            response = client.text_detection(image=image)
            texts = response.text_annotations
            
            
            docs= " "
            for text in texts:
                print('\n"{}"'.format(text.description))
                docs=docs+format(text.description)
                

                """
                vertices = (['({},{})'.format(vertex.x, vertex.y)
                                for vertex in text.bounding_poly.vertices])

                print('bounds: {}'.format(','.join(vertices)))
                """
            print(docs)

            nlp = spacy.load("en_core_web_sm")
            doc = nlp(docs)

            for ent in doc.ents:
                print(ent.text, ent.start_char, ent.end_char, ent.label_)

            if response.error.message:
                    raise Exception(
                        '{}\nFor more info on error messages, check: '
                        'https://cloud.google.com/apis/design/errors'.format(
                            response.error.message))
            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            print('Labels:')
            for label in labels:
                print(label.description)



            return redirect('success') 
    else: 
        form = BillForm() 
    return render(request, 'bill_image_form.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfully uploaded') 

# Create your views here.
