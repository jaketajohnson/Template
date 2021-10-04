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


if __name__ == "__main__":
    traceback_info = traceback.format_exc()
    try:
        Logging.logger.info("Script Execution Started")
        template()
        Logging.logger.info("Script Execution Finished")
    except (IOError, NameError, KeyError, IndexError, TypeError, UnboundLocalError, ValueError):
        Logging.logger.info(traceback_info)
    except NameError:
        print(traceback_info)
    except arcpy.ExecuteError:
        Logging.logger.error(arcpy.GetMessages(2))
    except:
        Logging.logger.info("An unspecified exception occurred")
