import os
from django.db import models

def recipe_image_path(instance, filename):
    # Extract file extension from the original filename
    ext = filename.split('.')[-1]
    # Construct new filename using food_name and extension
    filename = f"{instance.food_name}.{ext}"
    # Return the full path where the image will be uploaded
    return os.path.join('recipe_images/', filename)
