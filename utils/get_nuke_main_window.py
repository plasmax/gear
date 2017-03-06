__all__ = ['_nuke_main_window']

def _nuke_main_window():
    """Returns Nuke's main window"""
    for obj in QApplication.topLevelWidgets():
        # if obj.metaObject().className() == 'Nuke::NukeScriptEditor':
            # return obj
        if (obj.inherits('QMainWindow') and
                obj.metaObject().className() == 'Foundry::UI::DockMainWindow'):
            return obj
    else:
        raise RuntimeError('Could not find DockMainWindow instance')