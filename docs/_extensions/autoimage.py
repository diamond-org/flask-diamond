# Pedro Kroger
# https://gist.github.com/kroger/3856821
# http://pedrokroger.net/using-sphinx-write-technical-books/

import os
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.images import Image


def find_image(path, filename):
    fname = os.path.join(path, filename)
    if os.path.exists(fname + '.pdf'):
        return fname + '.pdf'
    elif os.path.exists(fname + '.png'):
        return fname + '.png'
    else:
        return False

class Autoimage(Image):
    option_spec = {'scale-html': directives.percentage,
                   'scale-latex': directives.percentage,
                   'scale-epub2': directives.percentage,
                   'scale-mobi': directives.percentage,
                   'scale': directives.percentage,
                   }

    def run(self):
        old_filename = self.arguments[0]
        env = self.state.document.settings.env
        builder_name = env.app.builder.name

        if builder_name == 'latex':
            self.arguments[0] = find_image(env.config.image_dir, old_filename)
            if env.config.black_and_white:
                bw_image = find_image(env.config.image_dir_black_white, old_filename)
                if bw_image:
                    self.arguments[0] = bw_image
        else:
            self.arguments[0] = os.path.join(env.config.image_dir, old_filename + '.png')

        # this doesn't quite work because sphinx stores the previous
        # values and share among builds. If I do a make clean between
        # each run it works. Yuck.
        # I need to run sphinx-build with -E
        self.options['scale'] = self.options.get('scale-' + builder_name, 100)
        self.options['align'] = 'center'

        return super(Autoimage, self).run()


def setup(app):
    app.add_directive('autoimage', Autoimage)
    app.add_config_value('image_dir', 'figs', False)
    app.add_config_value('black_and_white', False, True)
    app.add_config_value('image_dir_black_white', 'figs-bw', False)
