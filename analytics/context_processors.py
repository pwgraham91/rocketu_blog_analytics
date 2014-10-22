__author__ = 'GoldenGate'

def location(request):
    return {
        'location': request.location
    }
