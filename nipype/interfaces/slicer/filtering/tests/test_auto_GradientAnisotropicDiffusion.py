from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.filtering.denoising import GradientAnisotropicDiffusion

def test_GradientAnisotropicDiffusion_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    conductance=dict(argstr='--conductance %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='%s',
    position=-2,
    ),
    iterations=dict(argstr='--iterations %d',
    ),
    outputVolume=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    terminal_output=dict(nohash=True,
    ),
    timeStep=dict(argstr='--timeStep %f',
    ),
    )
    inputs = GradientAnisotropicDiffusion.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_GradientAnisotropicDiffusion_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = GradientAnisotropicDiffusion.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

