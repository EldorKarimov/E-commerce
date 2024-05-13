from django.contrib import admin
from .models import Media, Settings, Country, Region, OurInstagramStory, CustomerFeedback

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'type', 'created', 'updated')
    search_fields = ('file', 'type')
    list_filter = ('type',)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'home_title', 'home_subtitle', 'home_image', 'created', 'updated')
    search_fields = ('home_title', 'home_subtitle')
    list_filter = ('home_image',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'created', 'updated')
    search_fields = ('name', 'code')

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'zip_code', 'country_name', 'created', 'updated')
    search_fields = ('name', 'zip_code')
    list_filter = ('country_name',)

@admin.register(OurInstagramStory)
class OurInstagramStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'story_link', 'created', 'updated')
    search_fields = ('story_link',)

@admin.register(CustomerFeedback)
class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'rank', 'customer_name', 'customer_position', 'customer_image', 'created', 'updated')
    search_fields = ('description', 'customer_name', 'customer_position')
    list_filter = ('rank', 'customer_image')
