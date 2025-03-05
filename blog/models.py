# Creating our First Blog Model

from django.conf import settings    # Import Settings usch as Credentials and Keys
from django.db import models        # Import Database Models
from django.utils import timezone   # Import Timezone Module, Used for Timestamps

# Defining a new model in a class called post (it's an object)
class Post(models.Model):

    # Defining our model's properties
    
    """
        models.CharField - this is how you define text with a 
        limited number of characters.

        models.TextField - this is for long text without a limit. Sounds
        ideal for blog post content, right?

        models.DateTimeField - this is a date and time.

        models.ForeignKey - this is a link to another model.

    """

    # To create the tables for our models in our database, we add
    # our new model to our database. We just created this so we will 
    # go to the console window and type "python manage.py makemigrations blog,

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


