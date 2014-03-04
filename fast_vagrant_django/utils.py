#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from jinja2 import Environment, FileSystemLoader

class SimpleTemplateTofile(object):
    """
        A simple template to file that contains the logic
        about jinja template rendering.
    """

    loader = FileSystemLoader('./templates')
    env = Environment(loader = loader)

    def __init__(self, **kwargs):
        super(SimpleTemplateTofile, self).__init__()


    def render_template(self,template_name="a_template", **data):
        template = self.env.get_template(template_name)

        return template.render(**data)

    def create_file(self, template_name="a_template", file_name="a_file", path=".", data={}):
        template = self.render_template(template_name=template_name, **data)

        if not os.path.exists(path):
            os.makedirs(path)

        with open(os.path.join(path, file_name), 'w') as OutPutFile:
            OutPutFile.write(template)

        return OutPutFile
