"""
 SYNOPSIS

     Template.py

 DESCRIPTION

     * Description

 REQUIREMENTS

     Python 3
     arcpy
 """

import arcpy
import logging
import os
import traceback
import sys
sys.path.insert(0, "C:/Scripts")
import Logging


def template():
    """Create lateral lines using PACP observations"""

    # Paths

    # Environment
    arcpy.env.overwriteOutput = True

    @Logging.insert("Template logging message")
    def template_function():
        """Template description"""

        Logging.logger.info("------START Template")
        print("Template output")
        Logging.logger.info("------FINISH Template")


if __name__ == '__main__':
    template()
