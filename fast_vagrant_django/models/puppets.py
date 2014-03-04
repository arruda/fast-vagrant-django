# -*- coding: utf-8 -*-

from __future__ import absolute_import


class Manifest(object):
    """
        A simple puppet manifest object
    """
    template_name    = "manifest.pp"
    output_file_name = "manifest.pp"
    object_name         = "manifest"

    def __init__(self, **kwargs):
        super(Manifest, self).__init__()
        options = self.__default_options_dict()
        options.update(kwargs)
        for k,v in options.items():
            self.__setattr__(k,v)

    def __default_options_dict(self):
        "default options for this class kwargs"

        kwargs = {
            'project_name' : 'precise64',
            'box_url' : "http://files.vagrantup.com/precise64.box",
            'private_network_ip' : "192.168.56.101",


            'natdnshostresolver1' : True,
            'vb_name' : "proj-vm",
            'vb_memory' : 1024,

            'vb_guess_auto_update' : False,

            'manifest_file' : "proj.pp",

        }
        return kwargs

