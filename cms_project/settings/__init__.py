# Settings module
# Automatically load production settings if RENDER environment is detected
# Otherwise, load base settings for development
import os

if os.environ.get('RENDER') or os.environ.get('DJANGO_SETTINGS_MODULE', '').endswith('.production'):
    from .production import *
else:
    from .base import *

