"""
GAVIP Example AVIS: Simple AVI

@req: SOW-FUN-010
@req: SOW-FUN-040
@req: SOW-FUN-046
@req: SOW-INT-001
@comp: AVI Web System

This is a simple example AVI which demonstrates usage of the GAVIP AVI framework

Here in views.py, you can define any type of functions to handle 
HTTP requests. Any of these functions can be used to create an 
AVI query from your AVI interface.
"""
import os
import time
import json
import logging

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.core import serializers
from django.utils import formats
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods

from avi.models import DemoModel

ROLES = settings.GAVIP_ROLES

logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def index(request):
    """
    This view is the first view that the user sees
    We send a dictionary called a context, which contains 
    'millis' and 'standalone' variables.
    """
    context = {
        "show_welcome": request.session.get('show_welcome', True)
    }
    request.session['show_welcome'] = False
    return render(request, 'avi/index.html', context)


