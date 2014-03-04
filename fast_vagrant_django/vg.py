#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import sys


if __name__ == "__main__" and __package__ is None:

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(1, parent_dir)

    mod = __import__('fast_vagrant_django')
    sys.modules["fast_vagrant_django"] = mod

    __package__='fast_vagrant_django'

    from .core.projects import ProjectTemplate



    proj_name = sys.argv[1]
    path = sys.argv[2]

    proj = ProjectTemplate(project_name=proj_name, path=path)

    proj.create()
