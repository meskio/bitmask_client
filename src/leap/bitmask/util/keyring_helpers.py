# -*- coding: utf-8 -*-
# keyring_helpers.py
# Copyright (C) 2013 LEAP
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Keyring helpers.
"""
import logging

import keyring

from keyring.backends.file import EncryptedKeyring, PlaintextKeyring

logger = logging.getLogger(__name__)


OBSOLETE_KEYRINGS = [
    EncryptedKeyring,
    PlaintextKeyring
]

canuse = lambda kr: kr is not None and kr.__class__ not in OBSOLETE_KEYRINGS


def _get_keyring_with_fallback():
    """
    Get the default keyring, and if obsolete try to pick SecretService keyring
    if available.

    This is a workaround for the cases in which the keyring module chooses
    an insecure keyring by default (ie, inside a virtualenv).
    """
    kr = keyring.get_keyring()
    if not canuse(kr):
        try:
            kr_klass = keyring.backends.SecretService
            kr = kr_klass.Keyring()
        except AttributeError:
            logger.warning("Keyring cannot find SecretService Backend")
    logger.debug("Selected keyring: %s" % (kr.__class__,))
    if not canuse(kr):
        logger.debug("Not using default keyring since it is obsolete")
    return kr


def has_keyring():
    """
    Return whether we have an useful keyring to use.

    :rtype: bool
    """
    kr = _get_keyring_with_fallback()
    return canuse(kr)


def get_keyring():
    """
    Return an usable keyring.

    :rtype: keyringBackend or None
    """
    kr = _get_keyring_with_fallback()
    return kr if canuse(kr) else None
