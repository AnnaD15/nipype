from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix3.utils import TensorMetrics

def test_TensorMetrics_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    component=dict(argstr='-num %s',
    sep=',',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    ),
    in_mask=dict(argstr='-mask %s',
    ),
    modulate=dict(argstr='-modulate %s',
    ),
    out_adc=dict(argstr='-adc %s',
    ),
    out_eval=dict(argstr='-value %s',
    ),
    out_evec=dict(argstr='-vector %s',
    ),
    out_fa=dict(argstr='-fa %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = TensorMetrics.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_TensorMetrics_outputs():
    output_map = dict(out_adc=dict(),
    out_eval=dict(),
    out_evec=dict(),
    out_fa=dict(),
    )
    outputs = TensorMetrics.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

