#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Serveur HTTPS, avec authentification, pour formulaires.

Created on Tue Nov 16 13:22:51 2021

@author: ejetzer
"""

from http.server import ThreadingHTTPServer, CGIHTTPRequestHandler

def rouler(adresse=('', 8000), serveur=ThreadingHTTPServer, gérant=CGIHTTPRequestHandler):
    with serveur(adresse, gérant) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    rouler()
