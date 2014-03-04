#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('./templates')
env = Environment(loader = loader)

class FowardedPort(object):

    def __init__(self, guess,host):
        super(FowardedPort, self).__init__()
        self.guess = guess
        self.host = host


class Vagrant(object):
    """docstring for Vagrant"""

    def __init__(self, **kwargs):
        super(Vagrant, self).__init__()
        options = self.__default_options_dict()
        options.update(kwargs)
        for k,v in options.items():
            self.__setattr__(k,v)

        self.file = None

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

            'manifest_file' : "proj.pp",

        }
        return kwargs

    def load_template(self):
        return env.get_template('Vagrant')

    def render_template(self):
        t = self.load_template()
        return t.render({
            'vagrant':self,
        })

    def save_file(self,path):
        file_text = self.render_template()
        with open(os.path.join(path,'Vagrant'), 'w') as VagrantFile:
            VagrantFile.write(file_text)

        self.file = VagrantFile


    @classmethod
    def new_vagrant(cls,path=".", **vagrant_kwargs):


        v = Vagrant(**vagrant_kwargs)

            # vb_name=proj_name+"-vm", manifest_file=proj_name+".pp")
        v.save_file(path=path)
        return v

