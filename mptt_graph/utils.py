import importlib


def get_model_from_path(modpath): 
    # example: modpath = mptt_graph.models.TreeNode
    modsplit = modpath.split('.')
    path = '.'.join(modsplit[:-1]) # mptt_graph.models
    modname = '.'.join(modsplit[-1:]) # TreeNode
    # getatrr() returns the value of the named attribute of an object
    module = importlib.import_module(path)
    model = getattr(module, modname)

    return model