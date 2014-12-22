#======================
# LoadMenu
#======================
import os
import sys
import mari
from PythonQt.QtCore import QObject
sys.path.insert(0, "/X/tools/pythonlib/chichang/mari/")
sys.path.insert(0, "/X/tools/pythonlib/chichang/mari/xMariTools")
from textureExport import xgTextureExport
from textureExport import xgUtils as imp_utils
from styleFrameBuddy import styleFrameBuddy
reload(styleFrameBuddy)
reload(xgTextureExport)
reload(imp_utils)

#======================================================================
#	VARS
#======================================================================
debug = 0
menuName = "Mr.X"
#======================================================================
#	TEXTURE EXPORTER
#======================================================================

def showTextureExportGUI():
	#versionCheck
	if mari.app.version().major() != 2:
		mari.utils.message("Sorry. Mari 2.0 only.")
	else:

		try:
			if textureExportGUI.ui.isVisible():
				textureExportGUI.ui.reject()
		except:
			pass

		textureExportGUI = xgTextureExport.TextureExportWindow()
		textureExportGUI.showUI()


def showStyleframeBuddyGUI():
	if mari.app.version().major() != 2:
		mari.utils.message("Sorry. Mari 2.0 only.")
	else:
		try:
			if styleFrameBuddyGUI.ui.isVisible():
				styleFrameBuddyGUI.ui.reject()
		except:
			pass

		styleFrameBuddyGUI = styleFrameBuddy.styleFrameBuddyWindow()
		styleFrameBuddyGUI.showUI()

#======================================================================
#	MRI WRAP
#======================================================================
def connect_wrap(signal, response):
    """Helper function to connect a Qt or Mari signal to a Python callable.
    
    If the signal connection fails, make sure the signal and response are of the
    correct types and take compatible parameters.
    
    @param signal: A signal (event) to connect with a function call.
    @param response: A Python callable object, such as a function, to call when
                     the signal is triggered.
    @raise TypeError: Raised if one of the parameters is of the wrong type.
    @return: True or False to indicate whether the connection succeeded.
    """
    if not callable(response):
        raise TypeError(str(response) + " is not callable.")

    Result = False
    # PySide version
    if hasattr(signal, "connect"):
        Result = signal.connect(response)
    # Old PySide version
    if hasattr(signal, "__self__"):
        Result = QObject.connect(signal.__self__, signal.__name__, response)
    
    if Result==False:
        mari.app.log("Failed to connect {0}.{1} to {2}".format(signal.__self__, signal.__name__, response))
    
    return Result


#======================================================================
#  RETAIN PAINT BUFFER
#======================================================================
_retainBuffer = 0
_bufferScale = 0
_bufferRotation = 0
_bufferTranslate = 0
pBuffer = mari.canvases.paintBuffer()

def preBake():
	'''
	pre bake signal call. store paint buffer attrs.
	'''
	if _retainBuffer ==0:
		if debug: print "retain buffer is off."
		return
	elif _retainBuffer ==1:
		if debug: print "store buffer attrs"
		global _bufferScale, _bufferRotation, _bufferTranslate
		#stor buffer attrs
		_bufferScale = pBuffer.scale()
		_bufferRotation = pBuffer.rotation()
		_bufferTranslate = pBuffer.translation()

def postBake():
	'''
	post bake signal call. set paint buffer attrs.
	'''
	if _retainBuffer ==0:
		if debug: print "retain buffer is off."
		return
	elif _retainBuffer ==1:
		if debug: print "set buffer atters"
		#set buffer attrs
		pBuffer.setScale(_bufferScale)
		pBuffer.setRotation(_bufferRotation)
		pBuffer.setTranslation(_bufferTranslate)

def retainBufferSet(mode):
	'''
	set retainBuffer check variable and update Menue
	'''
	global _retainBuffer
	if mode == "on":
		_retainBuffer = 1
		if debug: print "turn on retain buffer."
		mari.menus.removeAction(retainBufferOn, "MainWindow/"+menuName)
		mari.menus.addAction(retainBufferOff, "MainWindow/"+menuName)

	elif mode == "off":
		_retainBuffer = 0
		if debug: print "turn off retain buffer."
		mari.menus.removeAction(retainBufferOff, "MainWindow/"+menuName)
		mari.menus.addAction(retainBufferOn, "MainWindow/"+menuName)

#======================================================================
#   MENU
#======================================================================

##create actions
#gotham mrx tools
textureExport = mari.actions.create("Export Textures", 'showTextureExportGUI()')
styleframeBuddy = mari.actions.create("Render Style Frames", 'showStyleframeBuddyGUI()')
loadOrtho = mari.actions.find("/Mari/Canvas/Camera/Ortho Camera")

#paint bufer callbacks
retainBufferOn = mari.actions.create("Turn On Retain Paint Buffer", 'retainBufferSet("on")')
retainBufferOff = mari.actions.create("Turn Off Retain Paint Buffer", 'retainBufferSet("off")')

def addGothamMenu():
	#gotham tools
	mari.menus.addAction(textureExport, "MainWindow/"+menuName)
	mari.menus.addAction(styleframeBuddy, "MainWindow/"+menuName)
	mari.menus.addAction(loadOrtho, "MainWindow/"+menuName)
	mari.menus.addSeparator("MainWindow/"+menuName)
	mari.menus.addAction(retainBufferOn, "MainWindow/"+menuName)

	#connect callbacks
	if mari.app.version().minor() == 6:
		connect_wrap(mari.canvases.paintBuffer().aboutToBake, preBake)
		connect_wrap(mari.canvases.paintBuffer().baked, postBake)
	elif mari.app.version().minor() == 5:
		connect(mari.canvases.paintBuffer().aboutToBake, preBake)
		connect(mari.canvases.paintBuffer().baked, postBake)

#======================================================================
#   ADD MENU
#======================================================================
if __name__=="__main__":
	addGothamMenu()
	print "-----------------------------------------"
	print "Gotham Tools Added to Menu."
	print "-----------------------------------------"
	print "\n"


