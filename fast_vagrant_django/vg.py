#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import os
import sys

#only to dev


if __name__ == "__main__" and __package__ is None:

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(1, parent_dir)

    mod = __import__('fast_vagrant_django')
    sys.modules["fast_vagrant_django"] = mod

    __package__='fast_vagrant_django'

    from .vagrants import Vagrant


    proj_name = sys.argv[1]
    path = sys.argv[2]


    v = Vagrant.new_vagrant(path=path, vb_name=proj_name+"-vm", manifest_file=proj_name+".pp")
