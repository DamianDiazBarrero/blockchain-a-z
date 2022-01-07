# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 10:48:57 2022

@author: DamianDiazBarrero
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
        
    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain)+1, 
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]#[-1] se obtiene el primer elemento de la cadena empezando por el final
    
    def proof_of_work(self, previous_proof):
       new_proof = 1
       check_proof = False
       while check_proof is False:
           