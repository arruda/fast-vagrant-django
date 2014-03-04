# -*- coding: utf-8 -*-

from __future__ import absolute_import

from ..utils import SimpleTemplateTofile
from ..models.vagrants import Vagrant

class ProjectTemplate(object):
    """
    Holds all templates from a Vagrant-puppet django project
    """

    def __init__(self, project_name="some_project", path="."):
        super(ProjectTemplate, self).__init__()
        self.path = path
        self.generator = SimpleTemplateTofile()

        self.project_name = project_name
        self.vagrant = Vagrant()

    def create_vagrant_file(self):
        self.generator.create_file(
                template_name = "manifests/Vagrant",
                file_name = "Vagrant",
                path = self.path,
                data = {
                    'vagrant': self.vagrant,
                }
            )



    def create(self):
        """
        creates a Vagrant-puppet project from the templates,
        with the current options
        """

        self.create_vagrant_file()

