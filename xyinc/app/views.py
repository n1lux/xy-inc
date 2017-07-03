from django.http import HttpResponse


def index(request):
    return HttpResponse("""<h1>Welcome to Xy inc. POI's</h1>
                        <p>api usage:</p>
                        <p>[GET|POST]<br> http://localhost:8000/api/v0/pois/</p>
                        <p>[GET]<br> http://localhost:8000/api/v0/search/?</p>
                        """)