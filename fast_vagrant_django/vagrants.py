#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .utils import SimpleFileTemplate

class FowardedPort(object):

    def __init__(self, guess,host):
        super(FowardedPort, self).__init__()
        self.guess = guess
        self.host = host


class Vagrant(SimpleFileTemplate):
    """docstring for Vagrant"""

    template_name    = "Vagrant"
    output_file_name = "Vagrant"
    object_name         = "vagrant"

    def __init__(self, **kwargs):
        super(Vagrant, self).__init__()
        options = self.__default_options_dict()
        options.update(kwargs)
        for k,v in options.items():
            self.__setattr__(k,v)

    def __default_options_dict(self):
        "default options for this class kwargs"

        kwargs = {
            'box' : 'precise64',
            'box_url' : "http://files.vagrantup.com/precise64.box",
            'private_network_ip' : "192.168.56.101",

            'forwarded_ports' : [
                                    FowardedPort(guess="8000",host="8000"),
                                    FowardedPort(guess="5432",host="8003"),
                                ],

            'natdnshostresolver1' : True,
            'vb_name' : "proj-vm",
            'vb_memory' : 1024,

            'vb_guess_auto_update' : False,

            'manifest_file' : "proj.pp",

        }
        return kwargs


    @classmethod
    def new_vagrant(cls,path=".", **vagrant_kwargs):


        v = Vagrant(**vagrant_kwargs)

        v.save_file(path=path)
        return v

