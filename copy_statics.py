# -*- coding:utf-8 -*-
"""
Created on Jan 1, 2016

@author: Wasim
"""

import errno
import glob
import os
import shutil


def main():
    zf = r'zurb-foundation-sites/'
    df = r'foundation/static/foundation/'
    zm = r'zurb-motion-ui/'
    dm = r'foundation/static/motion-ui/'

    pathes = (
        (glob.glob(zf + 'scss'), df + 'scss'),
        (glob.glob(zf + '_vendor'), df + '_vendor'),

        (glob.glob(zf + 'js'), df + 'js.es6'),
        (glob.glob(zf + 'dist/css'), df + 'css'),
        (glob.glob(zf + 'dist/js'), df + 'js'),
        (zf + 'LICENSE', df),

        (glob.glob(zm + 'src'), dm + 'scss'),
        (glob.glob(zm + 'dist/*.css'), dm + 'css', True),
        (glob.glob(zm + 'dist/*.js'), dm + 'js', True),
        (zm + 'LICENSE', dm),
    )
    for row in pathes:
        src, dst, mkdir = (row + (False,))[0:3]
        print('copy %s to %s' % (src, dst))

        if isinstance(src, list):
            try:
                shutil.rmtree(dst)
            except OSError as e:
                if e.errno not in (errno.ENOENT, errno.EINVAL):
                    raise

            if mkdir:
                try:
                    os.makedirs(dst)
                except OSError:
                    pass

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

    except OSError as exc:
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else:
            raise


if __name__ == '__main__':
    main()
