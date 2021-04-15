# Copyright edalize contributors
# Licensed under the 2-Clause BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-2-Clause

import logging
import os.path
from edalize.edatool import Edatool

logger = logging.getLogger(__name__)

class Openlane(Edatool):

    argtypes = []

    @classmethod
    def get_doc(cls, api_ver):
        if api_ver == 0:
            return {'description' : "Open source flow for ASIC synthesis, placement and routing",
                    'members': [
                    ],
                    'lists' : []}

    def configure_main(self):
        files = []
        lefs = []
        blackboxes = []
        gds = []
        tcl_params = ""
        tcl_interactive = ""
        tcl_pdn         = ""
        pin_order = ""
        macro_placement = ""
        presynthesis = ""
        prefloorplan = ""
        preplacement = ""
        prects = ""
        prerouting = ""
        prepowered = ""
        premagic = ""
        predrc = ""
        (src_files, incdirs) = self._get_fileset_files()
        for f in src_files:
            if f.file_type == 'verilogSource':
                files.append(f.name)
            elif f.file_type == 'verilogBlackbox':
                blackboxes.append(f.name)
            elif f.file_type == 'LEF':
                lefs.append(f.name)
            elif f.file_type == 'GDS':
                gds.append(f.name)
            elif f.file_type == 'interactive':
                tcl_interactive = f.name
            elif f.file_type == 'pdn':
                tcl_pdn = f.name
            elif f.file_type == 'macroPlacement':
                macro_placement = f.name
            elif f.file_type == 'pinOrder':
                pin_order = f.name
            elif f.name.endswith('params.tcl'):
                tcl_params = f.name
            elif f.name.endswith('presynthesis.tcl'):
                presynthesis = f.name
            elif f.name.endswith('prefloorplan.tcl'):
                prefloorplan = f.name
            elif f.name.endswith('preplacement.tcl'):
                preplacement = f.name
            elif f.name.endswith('prects.tcl'):
                prects = f.name
            elif f.name.endswith('prerouting.tcl'):
                prerouting = f.name
            elif f.name.endswith('prepowered.tcl'):
                prepowered = f.name
            elif f.name.endswith('premagic.tcl'):
                premagic = f.name
            elif f.name.endswith('predrc.tcl'):
                predrc = f.name

        template_vars = {
            'top' : self.toplevel,
            'file_table' : ' '.join(files),
            'blackbox_table' : ' '.join(blackboxes),
            'lefs_table' : ' '.join(lefs),
            'gds_table' : ' '.join(gds),
            'work_root' : os.path.split(self.work_root)[1],
            'tcl_params' : tcl_params,
            'tcl_interactive' : tcl_interactive,
            'tcl_pdn' : tcl_pdn,
            'pin_order' : pin_order,
            'macro_placement' : macro_placement,
            'presynthesis' : presynthesis,
            'prefloorplan' : prefloorplan,
            'preplacement' : preplacement,
            'prects' : prects,
            'prerouting' : prerouting,
            'prepowered' : prepowered,
            'premagic' : premagic,
            'predrc' : predrc,
        }

        script_name = 'config.tcl'
        self.render_template('openlane-script-tcl.j2', script_name, template_vars)

        makefile_name = 'Makefile'
        self.render_template('openlane-makefile.j2', makefile_name, template_vars)

        if (tcl_interactive == ""):
            interactive_name = 'interactive.tcl'
            self.render_template('openlane-script-interactive-tcl.j2', interactive_name, template_vars)