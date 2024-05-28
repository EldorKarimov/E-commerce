from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from django.core.exceptions import ValidationError

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Created time")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Updated time")
    abstract = True

class Media(BaseModel):
    class MediaType(models.TextChoices):
        IMAGE = 'image', _("Image")
        FILE = 'file', _("File")
        MUSIC = 'music', _("Music")
        VIDEO = 'video', _("Video")
    file = models.FileField(_("File"), upload_to="files/")
    type = models.CharField(_("File type"), choices=MediaType.choices, max_length=10)

    def clean(self):
        if self.type == self.MediaType.IMAGE:
            if not self.file.name.endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError("Images type must be .jpg, .jpeg, .png")
        elif self.type == self.MediaType.FILE:
            if not self.file.name.endswith(('.docx', '.pdf', '.doc')):
                raise ValidationError("Files type must be .docx, .pdf, .doc")
        elif self.type == self.MediaType.VIDEO:
            if not self.file.name.endswith('.mp4'):
                raise ValidationError("Video type must be .mp4")
        elif self.type == self.MediaType.MUSIC:
            if not self.file.name.endswith('.mp3', 'wav'):
                raise ValidationError("Video type must be .mp3, .wav")
        else:
            raise ValidationError("File type is not valid")
        return super().clean()

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Medias")

class Settings(BaseModel):
    home_image = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True, blank=True)
    home_title = models.CharField(_("Title"), max_length=120)
    home_subtitle = models.CharField(_("Subtitle"), max_length=120)

    def __str__(self):
        return self.home_title
    class Meta:

        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")
    
class Country(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Country name")
    code = models.CharField(max_length=10, verbose_name="Country code")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class Region(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Region name")
    zip_code = models.CharField(max_length=20, verbose_name="Zip code", null=True)
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="regions")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"
    
class OurInstagramStory(BaseModel):
    image = models.ForeignKey('Media', on_delete=models.CASCADE, related_name='instagram_stories')
    story_link = models.URLField(_("Story link"), validators=[
        URLValidator()
    ])

    def __str__(self):
        return str(self.story_link)

    class Meta:
        verbose_name = "Instagram story"
        verbose_name_plural = "Instagram stories"
    

class CustomerFeedback(BaseModel):
    description = models.TextField(_("Description"))
    rank = models.IntegerField(_("Rank"), validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    customer_name = models.CharField(_("Customer name"), max_length=60)
    customer_position = models.CharField(_("Customer position"), max_length=60)
    customer_image = models.ForeignKey('Media', on_delete=models.CASCADE, related_name='customer_images')

    def __str__(self):
        return self.customer_name
    
    class Meta:
        verbose_name = "Customer feedback"
        verbose_name_plural = "Customer feedbacks"