from django.shortcuts import render


def view_default_theme(request):
    return render(request, 'djit_theme/base.html')
