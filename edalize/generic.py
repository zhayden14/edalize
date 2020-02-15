import os
import logging

from edalize.edatool import Edatool

logger = logging.getLogger(__name__)


class Generic(Edatool):

    argtypes = [
        "cmdlinearg",
        "generic",
        "plusarg",
        "vlogdefine",
        "vlogparam",
    ]

    @classmethod
    def get_doc(cls, api_ver):
        if api_ver == 0:
            return {'description' : "Generic Backend for cases where some tool external to Edalize takes over the building",
                    'members' : [
                        {'name' : 'write_flist',
                         'type' : 'bool',
                         'desc' : 'Write an flist file'},
                        {'name' : 'build_cmd',
                         'type' : 'String',
                         'desc' : 'Command used to build (leave empty if not used)'},
                        {'name' : 'run_cmd',
                         'type' : 'String',
                         'desc' : 'Command used to run (leave empty if not used)'},
                    ]}

    def _write_flist():
        pass

    def configure_main(self):

        if self.tool_options.get('write_flist'):
            self._write_flist()

        build_cmd = self.tool_options.get('build_cmd')
        run_cmd   = self.tool_options.get('run_cmd')
        with open(os.path.join(self.work_root, 'Makefile'), 'w') as f:
            f.write('build:\n')
            if build_cmd:
                f.write('\t'+build_cmd+'\n')

            f.write('run:\n')
            if run_cmd:
                f.write('\t'+run_cmd+'\n')

    def run_main(self):
        self._run_tool('make', ['run'])
