

#======================
# Load xref
#======================
import os
import sys
import mari
from PythonQt.QtCore import QObject
sys.path.insert(0, "/USERS/chichang/tools/xref/xrefMari")
import xrefMariBrowser
#reload(xrefMariBrowser)
#from textureExport import xgUtils as imp_utils

#======================================================================
#	VARS
#======================================================================
debug = 0
xrefMenuName = "Gotham xref"

#======================================================================
#   MENU
#======================================================================
##create actions
#xref
xrefAbc = mari.actions.create("xref Alembic  ", "import xrefMariBrowser\nxrefMariBrowser.xDefineSelectWindow('Alembic').show()")
xrefImage = mari.actions.create("xref Image  ", "import xrefMariBrowser\nxrefMariBrowser.xDefineSelectWindow('Image').show()")
xrefImage.setEnabled(False)
xrefNew = mari.actions.create("xref New Project  ", "import xrefMariBrowser\nxrefMariBrowser.xDefineSelectWindow('New').show()")
xrefNew.setEnabled(False)

def addXrefMenu():
	#xref
	#create new project
	#mari.menus.addAction(xrefNew, "MainWindow/"+xrefMenuName)
	#mari.menus.addSeparator("MainWindow/"+xrefMenuName)
	mari.menus.addAction(xrefAbc, "MainWindow/"+xrefMenuName)
	mari.menus.addAction(xrefImage, "MainWindow/"+xrefMenuName)

#======================================================================
#   ADD XREF MENU
#======================================================================
if __name__=="__main__":
	addXrefMenu()
	print "-----------------------------------------"
	print "Gotham xref loaded."
	print "-----------------------------------------"
	print "\n"

