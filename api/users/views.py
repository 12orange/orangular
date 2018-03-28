from django.http import HttpResponse
from pymongo import MongoClient

def index(request):
    client = MongoClient('13.125.242.38', 27017)
    db = client["12Orange"]
    collection = db["users"]

    posts = collection.find()
    result = ", ".join(posts)

    return HttpResponse(result)
