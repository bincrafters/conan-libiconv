#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bincrafters import build_template_default, build_shared
import platform
import os

if __name__ == "__main__":

    builder = build_template_default.get_builder()

    builder.run()
