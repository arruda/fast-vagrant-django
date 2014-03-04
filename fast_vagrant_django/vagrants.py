#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('./templates')
env = Environment(loader = loader)

class Vagrant(object):
    """docstring for Vagrant"""
    def __init__(self, box="precise.box", private_network_ip="192.168.56.101",
        box_url="http://files.vagrantup.com/precise64.box",
        vb_name="proj-vm", manifest_file="proj.pp"):
        super(Vagrant, self).__init__()
        self.box = box
        self.private_network_ip = private_network_ip
        self.box_url = box_url
        self.vb_name = vb_name
        self.manifest_file = manifest_file

        self.file = None

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

