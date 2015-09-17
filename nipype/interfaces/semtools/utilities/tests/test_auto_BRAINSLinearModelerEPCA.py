from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.utilities.brains import BRAINSLinearModelerEPCA

def test_BRAINSLinearModelerEPCA_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputTrainingList=dict(argstr='--inputTrainingList %s',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = BRAINSLinearModelerEPCA.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BRAINSLinearModelerEPCA_outputs():
    output_map = dict()
    outputs = BRAINSLinearModelerEPCA.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

