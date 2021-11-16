#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
"""
Test de script cgi pour gestion de base de données.

Created on Tue Nov 16 13:32:15 2021

@author: ejetzer
"""

import string
import cgi

import cgitb
cgitb.enable()

import configparser as cp

from polytechnique.outils.db import BaseDeDonnées

config = cp.ConfigParser()
config.read(fichier_config := 'référence.config', encoding='utf-8')

base_de_données = BaseDeDonnées(config['base de données']['adresse'])
base_de_données.réinitialiser(config)


with open('htbin/modèle.html') as f:
    modèle = string.Template(f.read())

print('Content-type: text/html')
print()

print(modèle.safe_substitute(titre='Test',
                             tableau=base_de_données.df('boîtes').to_html()))
print()
