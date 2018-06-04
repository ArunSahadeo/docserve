from django.db import models

# Create your models here.

class Library(models.Model):
    created     = models.DateTimeField(auto_now_add=True)
    name        = models.CharField(max_length=100, blank=False, unique=True)
    language    = models.CharField(max_length=20, blank=True, default='')

    def __str__(self):
        return 'The library name is %s' % self.name

    class Meta:
        ordering = ('created',)

class Version(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=10, blank=False)
    library_id = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return 'Found version %s for the library %s' % self.version, self.name

    class Meta:
        ordering = ('created',)

class Resource(models.Model):
    version         = models.OneToOneField(
        Version,
        on_delete=models.CASCADE,
        primary_key = True
    ),
    repoREADME      = models.URLField(max_length=255, blank=True)
    websiteLanding  = models.URLField(max_length=255, blank=True)
    websiteDocs     = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return 'The version number string is %s' % self.version
