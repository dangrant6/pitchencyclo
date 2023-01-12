from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

pitch_selections = {
    "sinker" : "Sinker",
    "curveball": "Curveball",
    "slider": "Slider",
    "changeup": "Changeup",
    "cutter": "Cutter",
    "splitter": "Splitter",
    "screwball": "Screwball",
    "knuckleball": "Knuckleball",
}
# Create your views here.
def index(request):
    items = ""
    pitchs = list(pitch_selections.keys())
    for pitch in pitchs:
        capital = pitch.capitalize()
        pitch_path = reverse('pitch_name', args=[pitch])
        items += f"<li><a href=\"{pitch_path}\">{capital}</a></li>"
    repsonse_data = f"<ul>{items}</ul>"
    return HttpResponse(repsonse_data)

def pitch_by_num(request, pitch):
    pitchs = list(pitch_selections.keys())
    if pitch > len(pitchs):
        return HttpResponseNotFound("Invalid Pitch")
    redirect_pitch = pitchs[pitch-1]
    reditect_path = reverse('pitch_name', args=[redirect_pitch])
    return HttpResponseRedirect(reditect_path)

def pitch_select(request,pitch):
    try:
        temp = pitch_selections[pitch]
        return render(request,'pitches/thepitch.html',{
            "text": temp,
            #"pitch_type" : pitch.capitalize()
        })

    except:
        return HttpResponseNotFound("Pitch not here")

