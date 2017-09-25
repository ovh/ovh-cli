# -*- coding: utf8 -*-


def humanize_size(size):
    """It shows file/disk/ram size more conveniently."""
    return '{:.1f}G'.format(size / 1000)
