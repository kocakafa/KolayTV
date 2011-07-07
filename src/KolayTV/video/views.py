from django.shortcuts import get_object_or_404,render_to_response
from models import Video

def videos_list(request,User):
    
    return render_to_response('videos/user_videos.html',
                            {'user_video_list':Video.objects.all(User)})
    
def videos_detail(request,User,year,month,day,slug):
    import datetime,time
    date_stamp = time.strptime(year+month+day,"%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    return get_object_or_404(Video,pub_date__year=pub_date.year,
                                       pub_date__month=pub_date.month,
                                       pub_date__day=pub_date.day,
                                       slug=slug)
    
    
    return render_to_response('')
