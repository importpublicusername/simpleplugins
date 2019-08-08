
# system libraries
import configparser
import importlib
import pkgutil

# local
import localplugins

def iter_namespace(ns_pkg):
    # Specifying the second argument (prefix) to iter_modules makes the
    # returned name an absolute name instead of a relative one. This allows
    # import_module to work without having to do additional modification to
    # the name.
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

def getplugins():
    filename = r'config.txt'
    config = configparser.ConfigParser()
    config.read(filename)
    plugin_names = config._sections['plugins']
    plugin_names = [x.strip() for x in plugin_names['names'].split(',')]

    print(plugin_names)

    plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg
        in iter_namespace(localplugins)
    }

    print(plugins)

    #test the plugins calling the agreed entry point
    for plugin in plugin_names:
        plugins['localplugins.'+plugin].run('this worked')


if __name__ == "__main__":
    getplugins()
