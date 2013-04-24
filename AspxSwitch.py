# coding=utf8
import sublime, sublime_plugin, os

class AspxSwitchCommand(sublime_plugin.TextCommand):

    def is_visible(self):
        return self.is_asp_view_controller()

    def description(self):
        # NOTE: Doesn't care if the file is a switchable; we just switch based on its type.

        #if self.view.file_name().endswith('aspx'):
        #   return 'Go to Implementation'

        if self.view.file_name().endswith('aspx.cs') or self.view.file_name().endswith('aspx.vb'):
            return 'Go to View'

        return 'Go to Implementation'

    def run(self, edit):
        filename = self.view.file_name()
        if filename.endswith('x'):
            self.view.window().open_file(filename + '.cs')
        else:
            self.view.window().open_file(filename.replace('.cs', ''))
        return

    def is_asp_view_controller(self):
        filename = os.path.split(self.view.file_name().lower())

        if filename[-1].split('.')[-1] in ["aspx", "ascx", "ashx", "master"] and (os.path.isfile(self.view.file_name() + '.cs') or os.path.isfile(self.view.file_name() + '.vb')):
            return True

        if filename[-1].split('.')[-1] in ["cs", "vb"] and filename[-1].split('.')[-2] in ["aspx", "ascx", "ashx", "master"]:
            return True

        return False