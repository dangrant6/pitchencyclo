from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    pitchs = list(pitch_selections.keys())
    return render(request, 'pitches/index.html',{
        "pitches": pitchs,
    })

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
        })
    except:
        raise Http404()

