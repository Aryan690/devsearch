from .models import Profile, Skill
from django.db.models import Q


def searchProfiles(request):

    text = ''
    if request.GET.get('text'):
        text = request.GET.get('text')

    skills = Skill.objects.filter(name__icontains=text)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=text) | Q(short_intro=text) | Q(skill__in=skills))
        
    return profiles, text
    