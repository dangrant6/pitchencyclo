from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

pitch_selections = {
    "sinker" : "sinker",
    "curveball": "curveball",
    "slider": "slider",
    "changeup": "changeup",
    "cutter": "cutter",
    "splitter": "splitter",
    "screwball": "screwball",
    "knuckleball": "knuckleball",
}
# Create your views here.
def pitch_select(request,pitch):
    try:
        temp = pitch_selections[pitch]
        return HttpResponse(temp)
    except:
        return HttpResponseNotFound("Pitch not here")

