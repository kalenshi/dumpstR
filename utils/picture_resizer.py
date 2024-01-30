"""
Utilities for the pups routes
"""

import os
import secrets
from PIL import Image

from django.conf import settings

PICTURE_WIDTH = 400
PICTURE_HEIGHT = 400


def validate_picture_format(field):
    """
    Validates the file provided for picture is in any one of the acceptable
    picture formats
    Args:
        # form (str) : the picture string to be validated
        field (str) : the picture string to be validated

    Returns:
        bool : True if valid False otherwise
    Raises:
        ValidationError : If the picture file extension is not in the allowed extensions list
    """
    picture_extensions = [".png", ".jpeg", ".jpg", ".gif", ".psd", ".tiff"]
    _, ext = os.path.splitext(field.data.filename)
    if ext.lower() not in picture_extensions:
        raise ValueError(
            f"Wrong Picture extension! Allowed extentions are: {picture_extensions}"
        )
    return True


def save_picture_by_dimensions(form_picture, dimensions=None):
    """
    Gives a picture location a random hex filename and saves it in the database

    Args:
        form_picture(str) : The representation of the picture
        dimensions (tuple) : The width and height of the picture

    Returns:
        str : the location of the photo to be added to the database
    """
    if not dimensions:
        dimensions = (PICTURE_WIDTH, PICTURE_HEIGHT)
    _, ext = os.path.splitext(form_picture.filename)
    filename = f"{secrets.token_hex(8)}{ext.lower()}"

    picture_full_path = os.path.join(settings.BASE_DIR, "static", "img", filename)

    try:
        image = Image.open(form_picture)
        image.thumbnail(size=dimensions)
        image.save(picture_full_path)

    except FileNotFoundError as e:
        filename = "default.png"
    return filename
