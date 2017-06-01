from create_dir import createDir
import nuke

nuke.addBeforeRender(createDir)