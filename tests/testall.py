#!/usr/bin/env python
#
# Copyright (C) 2009-2010 Wander Lairson Costa 
# 
# The following terms apply to all files associated
# with the software unless explicitly disclaimed in individual files.
# 
# The authors hereby grant permission to use, copy, modify, distribute,
# and license this software and its documentation for any purpose, provided
# that existing copyright notices are retained in all copies and that this
# notice is included verbatim in any distributions. No written agreement,
# license, or royalty fee is required for any of the authorized uses.
# Modifications to this software may be copyrighted by their authors
# and need not follow the licensing terms described here, provided that
# the new terms are clearly indicated on the first page of each file where
# they apply.
# 
# IN NO EVENT SHALL THE AUTHORS OR DISTRIBUTORS BE LIABLE TO ANY PARTY
# FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES
# ARISING OUT OF THE USE OF THIS SOFTWARE, ITS DOCUMENTATION, OR ANY
# DERIVATIVES THEREOF, EVEN IF THE AUTHORS HAVE BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# 
# THE AUTHORS AND DISTRIBUTORS SPECIFICALLY DISCLAIM ANY WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.  THIS SOFTWARE
# IS PROVIDED ON AN "AS IS" BASIS, AND THE AUTHORS AND DISTRIBUTORS HAVE
# NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR
# MODIFICATIONS.

import sys
import unittest
import glob
import os.path
import os

parent_dir = os.path.split(os.getcwd())[0]

# if we are at PyUSB source tree, add usb package to python path
if os.path.exists(os.path.join(parent_dir, 'usb')):
    sys.path.insert(0, parent_dir)

import logging
import utils

if __name__ == '__main__':

    utils.logger.setLevel(logging.INFO)
    suite = unittest.TestSuite()

    for i in glob.glob('*.py'):
        m = __import__(os.path.splitext(i)[0])
        if hasattr(m, 'get_suite'):
            suite.addTest(m.get_suite())

    runner = unittest.TextTestRunner()
    runner.run(suite)
