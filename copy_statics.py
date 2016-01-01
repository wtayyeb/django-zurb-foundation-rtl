# -*- coding:utf-8 -*-
'''
Created on Jan 1, 2016

@author: Wasim
'''

from glob import glob
from pprint import pprint
import shutil, errno, os


def main():
    zf = r'zurb-foundation-sites/'
    df = r'foundation/static/foundation/'

    pathes = (
        (glob(zf + 'scss'), df + 'scss'),

        (glob(zf + 'js'), df + 'js/foundation'),
        (zf + 'dist/foundation.css', df + 'css'),
        (zf + 'dist/foundation.js', df + 'js'),
        (zf + 'dist/foundation.min.js', df + 'js'),
    )
    pprint(pathes)
    for src, dst in pathes:
        if isinstance(src, list):
            try:
                shutil.rmtree(dst)
            except OSError as e:
                if e.errno == 2:
                    pass
                else:
                    raise

            for s in src:
                cp(s, dst)
        else:
            try:
                os.makedirs(dst)
            except OSError:
                pass
            shutil.copy(src, dst)


def cp(src, dst):
    try:
        shutil.copytree(src, dst)

    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


if __name__ == '__main__':
    main()

