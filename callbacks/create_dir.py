__all__ = ['createDir']

import nuke
# import scripts

def createDir():
    """
    Checks if a directory exists before rendering. 
    If not, it creates it using the os module.
    """
    import nuke, os
    tn = nuke.thisNode()
    fn = nuke.filename(tn)
    dn = os.path.dirname(fn)
    if not os.path.isdir(dn):
        os.makedirs(dn)

# nuke.addBeforeRender(scripts.createDir)