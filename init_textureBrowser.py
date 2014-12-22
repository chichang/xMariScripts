import sys
sys.path.append("/X/tools/pythonlib/chichang/")
#todo add in mari version check
import textureBrowser.textureBrowser_mari as textureBrowser_mari
mritb = textureBrowser_mari.mariBrowser()
mari.app.addTab(mritb.title, mritb)
print '================================================='
print 'Texture Browser Loaded. '
print '================================================='
