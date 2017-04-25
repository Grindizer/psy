from pex.commands import bdist_pex

PREAMBULE = b"""
__distribution__ = '{distro}'

"""

BOOTSTRAP_LAMBDA = b"""
import os
import sys

__entry_point__ = None
if '__file__' in locals() and __file__ is not None:
  __entry_point__ = os.path.dirname(__file__)
elif '__loader__' in locals():
  from zipimport import zipimporter
  from pkgutil import ImpLoader
  if hasattr(__loader__, 'archive'):
    __entry_point__ = __loader__.archive
  elif isinstance(__loader__, ImpLoader):
    __entry_point__ = os.path.dirname(__loader__.get_filename())

if __entry_point__ is None:
  sys.stderr.write('Could not launch python executable!\\n')
  sys.exit(2)

sys.path[0] = os.path.abspath(sys.path[0])
sys.path.insert(0, os.path.abspath(os.path.join(__entry_point__, '.bootstrap')))

from _pex.pex_bootstrapper import bootstrap_pex_env
bootstrap_pex_env(__entry_point__)

import pkg_resources
dist = pkg_resources.WorkingSet().by_key.get(__distribution__, None)
if dist:
  for name, handler in dist.get_entry_map('psy.lambda_handler').items():
    exec('{name} = handler.resolve()'.format(name=name))

"""


class bdist_lambda(bdist_pex.bdist_pex):
    description = "Generate a package to use with aws lambda"
    user_options = [
        ('bdist-dir=', None, 'the directory into which the lambda package is written'),
        ('pex-args=', None, 'additional arguments to the underlying pex tool'),
    ]

    def _write(self, pex_builder, target, script=None):
        builder = pex_builder.clone()
        if script is not None:
            builder.set_script(script)

        name = self.distribution.get_name()
        builder._chroot.write(PREAMBULE.format(distro=name) + BOOTSTRAP_LAMBDA,
                              'lambda_handler.py',
                              label='source')
        target = target[:-4] + '.zip'
        builder.build(target)
