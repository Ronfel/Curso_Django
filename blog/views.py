from django.shortcuts import render

def blog(request):
    return render(
        request,
        'blog/index.html',
        {
            'text': 'Estamos no blog',
            'title': 'Blog -'
        }
        )

def exemplo(request):
    return render(
        request,
        'blog/exemplo.html',
        {
            'text': 'Estamos no Exemplo',
            'title': 'Exemplo -'
        }
        )