#!/usr/bin/env python3

class VersionStringConverter:
    regex = '([0-9]+?[.]?)+'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return '%s' % value
