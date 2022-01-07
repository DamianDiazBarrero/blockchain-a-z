# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 10:48:57 2022

@author: encof
"""

# Módulo 1 crear blockchain

#Importar librerías
import datetime
import hashlib
import json
from flask import Flask, jsonify 

#Crear blockchain
class Blockchain:
    
    def __init__(self):
        self.chain =[]
        self.create_block(proof = 1, previous_hash = '0')