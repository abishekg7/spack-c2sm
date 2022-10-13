#!/usr/bin/python3

# Tests that the command 'SPACK SPEC ...' work.

import subprocess
import unittest


class CosmoTest(unittest.TestCase):

    def test_org_master(self):
        subprocess.run('spack spec cosmo @org-master', check=True, shell=True)


class IconTest(unittest.TestCase):

    def test_nwp(self):
        subprocess.run('spack spec icon @nwp', check=True, shell=True)


class Int2lmTest(unittest.TestCase):

    def test_org_master(self):
        subprocess.run('spack spec int2lm @org-master', check=True, shell=True)


if __name__ == '__main__':
    unittest.main()