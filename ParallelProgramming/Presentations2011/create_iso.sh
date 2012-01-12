#!/bin/bash

rm -f cd.iso
mkisofs -r -J -o cd.iso cd/
