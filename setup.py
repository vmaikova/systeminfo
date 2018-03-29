#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Brynja Bergmann",
      author_email="brynja.halldorsdottir@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
        'console_scripts':['systeminfo=systeminfo.main:main']
        }
      )
