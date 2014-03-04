#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from vagrants import Vagrant

if __name__ == "__main__":

    proj_name = sys.argv[1]
    path = sys.argv[2]


    v = Vagrant.new_vagrant(path=path, vb_name=proj_name+"-vm", manifest_file=proj_name+".pp")
