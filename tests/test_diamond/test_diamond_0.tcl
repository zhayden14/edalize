#Generated by Edalize
prj_project new -name test_diamond_0 -dev LFE5U-85F-6BG381C -synthesis synplify
prj_impl option top top_module
prj_impl option {include path} {.}
prj_impl option HDL_PARAM {generic_bool=True;generic_int=42;generic_str=hello}
prj_impl option HDL_PARAM {vlogparam_bool=1;vlogparam_int=42;vlogparam_str="hello"}
prj_impl option VERILOG_DIRECTIVES {vlogdefine_bool=True;vlogdefine_int=42;vlogdefine_str=hello}
prj_src add -format SDC sdc_file
prj_src add -format Verilog sv_file.sv
source tcl_file.tcl
prj_src add -format Verilog vlog_file.v
prj_src add -format Verilog vlog05_file.v
prj_src add -format VHDL vhdl_file.vhd
prj_src add -format VHDL -work libx vhdl_lfile
prj_src add -format VHDL vhdl2008_file
prj_project save
exit