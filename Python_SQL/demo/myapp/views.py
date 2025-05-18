from django.shortcuts import render, redirect, get_object_or_404
from .models import Contatto
from .forms import ContattoForm
from django.db.models import Q

def home(request):
    form = None
    if request.method == 'POST':
        azione = request.POST.get('azione')

        if azione == 'crea':
            form = ContattoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        
        elif azione == 'modifica':
            contatto_id = request.POST.get('contatto_id')
            contatto = get_object_or_404(Contatto, pk=contatto_id)
            form = ContattoForm(request.POST, instance=contatto)
            if form.is_valid():
                form.save()
                return redirect('home')
            
            
        elif azione == 'elimina':
            contatto_id = request.POST.get('contatto_id')
            contatto = get_object_or_404(Contatto, pk=contatto_id)
            contatto.delete()
            return redirect('home')
    else:
        form = ContattoForm()
            

    # Gestione ricerca
    query = request.GET.get('q')
    if query:
        contatti = Contatto.objects.filter(
            Q(nome__icontains=query) |
            Q(cognome__icontains=query) |
            Q(telefono__icontains=query)
        )
    else:
        contatti = Contatto.objects.all()

    return render(request, 'home.html', {
        'form': form,
        'contatti': contatti,
        'query': query
    })


