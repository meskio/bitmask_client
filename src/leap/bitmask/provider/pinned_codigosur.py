# -*- coding: utf-8 -*-
# pinned_calyx.py
# Copyright (C) 2013-2014 LEAP
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
Pinned provider.json and cacert.pem for codigosur.email
"""

DOMAIN = "codigosur.email"

PROVIDER_JSON = """
{
  "api_uri": "https://api.codigosur.email:4430",
  "api_version": "1",
  "ca_cert_fingerprint": "SHA256: c2e9313a1ec605ff0952ed43fd90c80808c127b9d2e92810ad8e92d90d24e97d",
  "ca_cert_uri": "https://codigosur.email/ca.crt",
  "default_language": "es",
  "description": {
    "en": "Código Sur",
    "es": "Código Sur"
  },
  "domain": "codigosur.email",
  "enrollment_policy": "open",
  "languages": [
    "en",
    "es"
  ],
  "name": {
    "en": "CodigoSur",
    "es": "CodigoSur"
  },
  "service": {
    "allow_anonymous": false,
    "allow_free": true,
    "allow_limited_bandwidth": false,
    "allow_paid": false,
    "allow_registration": true,
    "allow_unlimited_bandwidth": true,
    "bandwidth_limit": 102400,
    "default_service_level": 1,
    "levels": {
      "1": {
        "description": "Please donate.",
        "name": "free"
      }
    }
  },
  "services": [
    "mx",
    "openvpn"
  ]
}
"""

CACERT_PEM = """-----BEGIN CERTIFICATE-----
MIIFezCCA2OgAwIBAgIBATANBgkqhkiG9w0BAQ0FADBQMRIwEAYDVQQKDAlDb2Rp
Z29TdXIxHjAcBgNVBAsMFWh0dHBzOi8vY29kaWdvc3VyLm9yZzEaMBgGA1UEAwwR
Q29kaWdvU3VyIFJvb3QgQ0EwHhcNMTUwNjE0MDAwMDAwWhcNMjUwNjE0MDAwMDAw
WjBQMRIwEAYDVQQKDAlDb2RpZ29TdXIxHjAcBgNVBAsMFWh0dHBzOi8vY29kaWdv
c3VyLm9yZzEaMBgGA1UEAwwRQ29kaWdvU3VyIFJvb3QgQ0EwggIiMA0GCSqGSIb3
DQEBAQUAA4ICDwAwggIKAoICAQDEFn86vdhWnBltc1VbyNr9pjIdtKGWyn8epm7k
F+M4kPKMeSjvBbB++52OjyEK6ADiGcnECCfA/E+5SSUbpm7eoV0w6Se71YPDwZPM
XCA90qzVyu6pf3dtZY0BT3l50lsZbEyM1wF5mzwM1He0+87Z0TMiWf3sxEnZ+o6u
ACRA+TPPzPkHyWtMsHAVafW0jnSh92irtqSYJdXvw47GyPBXkIt6wMHTggUrCX2H
lBHYfbLZVpHgDys84MKmW3n3UxALnYn3/sgg762cFMF9F2xf7uLvOJ6A5SZr6t/C
Unee29wDatNhKqSlCzKTkH1ayle82BVHO2cwtJ1gseHMyGAYC+C3Mf0fD6ySUgcY
ZcNTRxPAK5AcwqtdsWQLPiLE2I8QXLZ1Zh7yBTo5A3O5Qw0HsYQovlIFI5c5p8wT
FAxRz3xvPPNAUFnj8a9/Ls1qGIkNsM1zrhDXr7jC5HS7BcNlM2vG9GnuxXAaeNiW
Gtb5aFTA7qDupSDcmlVjQhnvP9R/yK58Pk2VQeR+PIx2XqLDgty17cpb4IZy40OV
TGqS9x706uz9As6wmgcvk72N0sxZgIL5vpIiiVKiEJu0Yqn4J/oOhBYKJOc5yO1L
Tnnbwulr0r1szbtpPWL0b12idGB32o8CVt6JZBSgvRYV50be82uePzlReEFll8vO
2qC0+QIDAQABo2AwXjAdBgNVHQ4EFgQUIzhMrgL8r92J9U2CvRhnrRQAYQwwDgYD
VR0PAQH/BAQDAgIEMAwGA1UdEwQFMAMBAf8wHwYDVR0jBBgwFoAUIzhMrgL8r92J
9U2CvRhnrRQAYQwwDQYJKoZIhvcNAQENBQADggIBABq/XV2TNItp/C5efnPO7OXA
dIVBhC818Jtc9CJkRxW0rRdZX1ClHvqdlL4GSpwTNKDto+oH6ZId5dtajdouQt5i
Twb2OTzNsvl7zu+sQIHzdVXq97FQqG+KyTlI+yc3O1JOR8jx4LR0Bl3/0A2kCTux
VXxvRIZbDIkgqVzCZTFshPzXjF2StbDe2vmlwKwE6688N26pXlQAF+2AT97KER4I
cLWKrHCDSsJQpNYkTZtGQtsHLNGaw2MHXsxN4HAU5eGtL7S3OfpGne3i8kF2treU
YC7DKtT/Q15PLnkQtnZNM81MhWyY0AQMvpwGL5N8hYBJhXAFilFeBRK15wq6/bdS
fw/V4h8m/mBLk3sg+voV/PdmFCSvWWUKNwtrqkaOphtdYqJ6t2H0ejR6M6cCuTGh
oWfTc85jKeUqCSqpT72WIEIaMBPvT7dnT0yeexi7lesZ/HOB53I9pyV6KuT9pcga
uHiz8foGpf1HEYxrwngr/Y8CcUnHA/TPiG5p02lon2mHIT8tl0+n+iuFtgeKVyuX
vv0S3meOKa5r1IORDdmIwS0GRzQ9BJ2wv6w4/nQeco0oAlC81Y3OLgQwgE4xctbf
VZDJ5s8lxogj7VQQcl/jZx0Qd0TltL6ZwZla4Kv2MvWJBuuWGyX3YtidjgUBuVKK
HuMtwKk9oKTrY/YNX1V9
-----END CERTIFICATE-----"""
