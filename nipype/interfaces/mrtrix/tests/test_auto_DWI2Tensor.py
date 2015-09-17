from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix.preprocess import DWI2Tensor

def test_DWI2Tensor_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    debug=dict(argstr='-debug',
    position=1,
    ),
    encoding_file=dict(argstr='-grad %s',
    position=2,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    ignore_slice_by_volume=dict(argstr='-ignoreslices %s',
    position=2,
    sep=' ',
    ),
    ignore_volumes=dict(argstr='-ignorevolumes %s',
    position=2,
    sep=' ',
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    out_filename=dict(argstr='%s',
    name_source='in_file',
    name_template='%s_tensor.mif',
    output_name='tensor',
    position=-1,
    ),
    quiet=dict(argstr='-quiet',
    position=1,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = DWI2Tensor.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_DWI2Tensor_outputs():
    output_map = dict(tensor=dict(),
    )
    outputs = DWI2Tensor.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

