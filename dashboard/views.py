from django.db.models.lookups import In
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import InventoryItem, PlayableCharacter

from .forms import ItemModelForm, PlayableCharacterForm


@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def playable_characters_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlayableCharacterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            name = form.cleaned_data.get('name')
            age = form.cleaned_data['age']
            description = form.cleaned_data['description']
            user = request.user
            playable_character = PlayableCharacter()
            playable_character.name = name
            playable_character.age = age
            playable_character.description = description
            playable_character.user = user
            playable_character.save()
            return redirect('dashboard:dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlayableCharacterForm()
    return render(request, 'dashboard/playable_characters.html', {'form': form})


@login_required
def pc_list_view(request):
    pc_list = PlayableCharacter.objects.filter(user=request.user)
    return render(request, 'dashboard/pc_list.html', {'pc_list': pc_list})


@login_required
def pc_delete_view(request, pk):
    playable_character = PlayableCharacter.objects.get(pk=pk)
    playable_character.delete()
    return redirect('dashboard:pc_list')


@login_required
def pc_inventory_view(request, pk):
    pc = PlayableCharacter.objects.get(pk=pk)
    item_list = InventoryItem.objects.filter(playable_character=pc)
    return render(request, 'dashboard/pc_inventory.html', {'item_list': item_list, 'pk': pk})


@login_required
def item_view(request, pk):
    pc = PlayableCharacter.objects.get(pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemModelForm(request.POST, playable_character=pc)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # name = form.cleaned_data.get('name')
            # number = form.cleaned_data['number']
            # weight = form.cleaned_data['weight']
            # description = form.cleaned_data['description']
            # playable_character = PlayableCharacter.objects.get(pk=pk)
            # item = InventoryItem()
            # item.name = name
            # item.number = number
            # item.weight = weight
            # item.description = description
            # item.playable_character = playable_character
            # item.save()
            form.save()
            return redirect('dashboard:pc_inventory', pk=pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ItemModelForm(playable_character=pc)
    return render(request, 'dashboard/item.html', {'form': form})


@login_required
def item_delete_view(request, pk, pk_item):
    item = InventoryItem.objects.get(pk=pk_item)
    item.delete()
    return redirect('dashboard:pc_inventory', pk=pk)


@login_required
def item_edit_view(request, pk, pk_item):
    pc = PlayableCharacter.objects.get(pk=pk)
    item = InventoryItem.objects.get(pk=pk_item)
    if request.method == 'POST':
        form = ItemModelForm(request.POST, instance=item,
                             playable_character=pc)
        if form.is_valid():
            form.save()
            return redirect('dashboard:pc_inventory', pk=pk)

    else:
        form = ItemModelForm(instance=item, playable_character=pc)
    return render(request, 'dashboard/item.html', {'form': form})
