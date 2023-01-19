from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

import mimetypes

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
pitch_decsription = {
    "sinker": "A sinker or sinking fastball is a type of fastball which has significant downward and horizontal movement and is known for inducing ground balls.",
    "curveball": "Varieties of curveball include the 12/6 curveball, sweeping curveball, and the knuckle curve.",
    "slider": "A slider is a breaking ball pitch that tails laterally and down through the batter's hitting zone. It is thrown at a speed that is lower than a fastball, but higher than the pitcher's curveball. Variations include a sweeper, gyro, and a slurve.",
    "changeup": "Usually thrown to look like a fastball but arriving much more slowly to the plate. They tend to drop and have horizontal movement. Variations include the circle change, forkball, palmball, vulcan and split change.",
    "cutter": "A cut fastball or cutter is a type of fastball that breaks toward the pitcher's glove-hand side, as it reaches home plate.[1] This pitch is somewhere between a slider and a four-seam fastball, as it is usually thrown faster than a slider but with more movement than a typical fastball.",
    "splitter": "Looks to the batter like a fastball until it drops suddenly. Derived from the forkball, it is so named because the pitcher puts the index and middle finger on different sides of the ball.",
    "screwball": "A rare pitch that is thrown so as to break in the opposite direction of a slider or curveball. Depending on the pitcher's arm angle, the ball may also have a sinking action.",
    "knuckleball": "A knuckleball is a baseball pitch thrown to minimize the spin of the ball in flight, causing an erratic, unpredictable motion. The air flow over a seam of the ball causes the ball to change from laminar to turbulent flow. This change adds a deflecting force to the baseball, making it difficult for batters to hit but also difficult for pitchers to control and catchers to catch",
}
pitch_down = {
    "sinker": "pitches/images/Sinker",
    "curveball": "pitches/images/Curveball",
    "slider": "pitches/images/Slider",
    "changeup": "pitches/images/Changeup",
    "cutter": "pitches/images/Cutter",
    "splitter": "pitches/images/Splitter",
    "screwball": "pitches/images/Screwball",
    "knuckleball": "pitches/images/Knuckleball",
}
pitch_ex = {
    "sinker": 'pitches/images/sink.gif',
    "curveball": "pitches/images/Curveball",
    "slider": "pitches/images/Slider",
    "changeup": "pitches/images/Changeup",
    "cutter": "pitches/images/Cutter",
    "splitter": "pitches/images/Splitter",
    "screwball": "pitches/images/Screwball",
    "knuckleball": "pitches/images/Knuckleball",
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
        des = pitch_decsription[pitch]
        fl_path = pitch_down[pitch]
        #pic = Pitch.objects.get(pk=pitch)
        pic = pitch_ex[pitch]
        return render(request,'pitches/thepitch.html',{
            "text": temp,
            "des": des,
            "down": fl_path,
            "ex": pic
        })
    except:
        raise Http404()
'''
def pitch_detail(request,pitch):
    return render(request, 'pitches/thepitch.html')
'''
def download(request,pitch):
    #do = pitch_down[pitch]
    fl_path = pitch_down[pitch]
    fl_name = '.zip'
    fl = open(fl_path,'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % fl_name
    return response
