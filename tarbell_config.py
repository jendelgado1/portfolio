# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "portfolio"

# Descriptive title of project
TITLE = "jennifer delgado&#39;s website"

# Google spreadsheet key
SPREADSHEET_KEY = "0AiiCaqIWHDnpdHF1U0g2cW9DQmNnNjRTa2VJd0Fxd2c"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
#S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
#}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'portfolio',
    'title': "jennifer delgado's website"
}