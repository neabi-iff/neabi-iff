# -*- coding: utf-8 -*-

"""
Arquivo modelo do settings.py.
Aqui deve conter apenas o que há de diferente em relação ao settings_base.py,
como por exemplo senhas e outros dados sigilosos.
"""

try:
    from settings_base import *
except ImportError, e:
    pass


INSTALLED_APPS += (
)