def createDir():
    """
    Checks if a directory exists before rendering. 
    If not, it creates it using the os module.
    To add to menu.py: nuke.addBeforeRender(create_dir.createDir)
    """
    import nuke, os
    tn = nuke.thisNode()
    fn = nuke.filename(tn)
    dn = os.path.dirname(fn)
    if not os.path.isdir(dn):
        # os.mkdir(dn)
        os.makedirs(dn)
