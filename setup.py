#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension
from subprocess import check_output


def pkgconfig(*packages, **kw):
    flag_map = {'-I': 'include_dirs', '-L': 'library_dirs', '-l': 'libraries'}
    extra_args = 'extra_link_args'
    for token in check_output(['pkg-config', '--cflags', '--libs'] + list(packages),
                              universal_newlines=True).strip().split():
        if token[:2] not in flag_map and token.endswith(".so"):
            kw.setdefault(extra_args, []).append(token)
        else:
            kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])
    return kw


pqtable_module = Extension('_pqtable',
                           sources=['pqtable_wrap.cxx', 'src/pq_table.cpp',
                                    'src/sparse_hashtable/sparse_hashtable.cpp',
                                    'src/sparse_hashtable/bucket_group.cpp', 'src/sparse_hashtable/array32.cpp',
                                    'src/pq_key_generator.cpp', 'src/sparse_hashtable/helper_sht.cpp', 'src/pq.cpp',
                                    'src/code_to_key.cpp', 'src/utils.cpp'],
                           extra_compile_args=['-std=c++11'],
                           **pkgconfig('opencv')
                           )

setup(name='pqtable',
      version='0.1',
      author="SWIG Docs",
      description="""PQ table module for fast spatial""",
      ext_modules=[pqtable_module],
      py_modules=["pqtable"],
      )
