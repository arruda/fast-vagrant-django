#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('./templates')
env = Environment(loader = loader)


class SimpleFileTemplate(object):
    """
        A simple file template that contains the logic
        about jinja template rendering.
    """

    template_name    = "a_template"
    output_file_name = "a_file"
    object_name      = "a_object"

    def __init__(self, **kwargs):
        super(SimpleFileTemplate, self).__init__()
        self.file = None

    def load_template(self):
        return env.get_template(self.template_name)

    def render_template(self):
        t = self.load_template()
        return t.render({
            self.object_name :self,
        })

    def save_file(self,path):
        file_text = self.render_template()

        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path,self.output_file_name), 'w') as OutPutFile:
            OutPutFile.write(file_text)

        self.file = OutPutFile
