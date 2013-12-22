# -*- coding: utf-8 -*-
#
# This file is part of django-hashers-passlib
# (https://github.com/mathiasertl/django-hashers-passlib).
#
# django-hashers-passlib is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# django-hashers-passlib is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# django-hashers-passlib.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

import os
import sys

sys.path.insert(0, 'example')
os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings'

from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import load_hashers
from django.contrib.auth.hashers import make_password
from django.test import TestCase

import hashers_passlib

PASSWORDS = [
    'I',
    'DA',
    'RoJ',
    'THxn',
    '1uzPU',
    'oe331f',
    'qBcP47',
    'D4i19w',
    'e8qBbIA',
    'vzCXzq8',
    '7xEmLNYW',
    'HeVCzQ3I',
    'mMIJzMuAo',
    '4gjjrcCfm',
    '3Asa788x6g',
    'AGwKzVP1SC',
    'CWwYP880G4',
    'RK8SMEmv0s',
]

class TestMixin(object):
    @property
    def path(self):
        return '%s.%s' % (self.hasher.__module__, self.hasher.__class__.__name__)

    def test_check(self):
        with self.settings(PASSWORD_HASHERS=[self.path, ]):
            load_hashers(settings.PASSWORD_HASHERS)

            for password in PASSWORDS:
                encoded = make_password(password)
                self.assertTrue(check_password(password, encoded))

                # test to_orig, done here, to save a few hash-generations
                encoded_orig = self.hasher.to_orig(encoded)
                self.assertTrue(self.hasher.hasher.verify(password, encoded_orig))

    def test_from_orig(self):
        with self.settings(PASSWORD_HASHERS=[self.path, ]):
            load_hashers(settings.PASSWORD_HASHERS)

            for password in PASSWORDS:
                # create and import hash
                encoded_orig = self.hasher.hasher.encrypt(password)
                encoded = self.hasher.from_orig(encoded_orig)
                self.assertTrue(check_password(password, encoded))


class des_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.des_crypt()


class bsdi_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.bsdi_crypt()


class bigcrypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.bsdi_crypt()


class crypt16_test(TestCase, TestMixin):
    hasher = hashers_passlib.crypt16()


class md5_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.md5_crypt()


class sha1_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.sha1_crypt()


class sun_md5_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.sun_md5_crypt()


class sha256_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.sha256_crypt()


class sha512_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.sha512_crypt()


class apr_md5_crypt_test(TestCase, TestMixin):
    hasher = hashers_passlib.apr_md5_crypt()


class phpass_test(TestCase, TestMixin):
    hasher = hashers_passlib.phpass()


class cta_pbkdf2_sha1_test(TestCase, TestMixin):
    hasher = hashers_passlib.cta_pbkdf2_sha1()


class dlitz_pbkdf2_sha1_test(TestCase, TestMixin):
    hasher = hashers_passlib.dlitz_pbkdf2_sha1()


class scram_test(TestCase, TestMixin):
    hasher = hashers_passlib.scram()


class ldap_md5_test(TestCase, TestMixin):
    hasher = hashers_passlib.ldap_md5()


class ldap_sha1_test(TestCase, TestMixin):
    hasher = hashers_passlib.ldap_sha1()


class ldap_salted_md5_test(TestCase, TestMixin):
    hasher = hashers_passlib.ldap_salted_md5()


class ldap_salted_sha1_test(TestCase, TestMixin):
    hasher = hashers_passlib.ldap_salted_sha1()


class ldap_hex_md5_test(TestCase, TestMixin):
    hasher = hashers_passlib.ldap_hex_md5()


class ldap_hex_sha1_test(TestCase, TestMixin):
    hasher = hashers_passlib.ldap_hex_sha1()


class atlassian_pbkdf2_sha1_test(TestCase, TestMixin):
    hasher = hashers_passlib.atlassian_pbkdf2_sha1()


class fshp_test(TestCase, TestMixin):
    hasher = hashers_passlib.fshp()


class mssql2000_test(TestCase, TestMixin):
    hasher = hashers_passlib.mssql2000()


class mssql2005_test(TestCase, TestMixin):
    hasher = hashers_passlib.mssql2005()


class mysql323_test(TestCase, TestMixin):
    hasher = hashers_passlib.mysql323()


class mysql41_test(TestCase, TestMixin):
    hasher = hashers_passlib.mysql41()


class oracle11_test(TestCase, TestMixin):
    hasher = hashers_passlib.oracle11()


class lmhash_test(TestCase, TestMixin):
    hasher = hashers_passlib.lmhash()


class nthash_test(TestCase, TestMixin):
    hasher = hashers_passlib.nthash()


class cisco_pix_test(TestCase, TestMixin):
    hasher = hashers_passlib.cisco_pix()


class cisco_type7_test(TestCase, TestMixin):
    hasher = hashers_passlib.cisco_type7()


class grub_pbkdf2_sha512_test(TestCase, TestMixin):
    hasher = hashers_passlib.grub_pbkdf2_sha512()


class hex_md4_test(TestCase, TestMixin):
    hasher = hashers_passlib.hex_md4()


class hex_sha256_test(TestCase, TestMixin):
    hasher = hashers_passlib.hex_sha256()


class hex_sha512_test(TestCase, TestMixin):
    hasher = hashers_passlib.hex_sha512()
