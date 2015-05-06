#!/bin/bash
# Tunnel SSH pour POP/SMTP
ssh -L localhost:25:(IP distante):25 -L localhost:110:(IP distante):110 sysmso@serveur
