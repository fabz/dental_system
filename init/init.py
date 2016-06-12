from base import *  # @UnusedWildImport @UnresolvedImport
from django.contrib.auth.models import User


def create_system_user():
    User.objects.create(username="system")

function_list = [create_system_user]
execute(function_list, 'deployment_schema_result3.txt')
