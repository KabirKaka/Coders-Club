from django.shortcuts import render


def home(request):
    return render(request, "gallery/gallery.html", {'isGallery': True})

def selected(request):
    return render(request, "gallery/gallerySelected.html", {'isGallery': True})