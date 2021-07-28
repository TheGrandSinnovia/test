from django.contrib import admin

from .models import InventoryItem, PlayableCharacter


admin.site.register(PlayableCharacter)
admin.site.register(InventoryItem)
