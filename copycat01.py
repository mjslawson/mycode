#!/usr/bin/env python3
import shutil
import os

# The following line will create the directory if it does not exist already
os.chdir('/home/student/mycode/')
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
shutil.copytree('5g_research/', '5g_research_backup/')

