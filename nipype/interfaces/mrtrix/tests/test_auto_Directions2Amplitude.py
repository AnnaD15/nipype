from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix.tensors import Directions2Amplitude

def test_Directions2Amplitude_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    display_debug=dict(argstr='-debug',
    ),
    display_info=dict(argstr='-info',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    num_peaks=dict(argstr='-num %s',
    ),
    out_file=dict(argstr='%s',
    hash_files=False,
    keep_extension=False,
    name_source=['in_file'],
    name_template='%s_amplitudes.mif',
    position=-1,
    ),
    peak_directions=dict(argstr='-direction %s',
    sep=' ',
    ),
    peaks_image=dict(argstr='-peaks %s',
    ),
    quiet_display=dict(argstr='-quiet',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = Directions2Amplitude.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_Directions2Amplitude_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Directions2Amplitude.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

