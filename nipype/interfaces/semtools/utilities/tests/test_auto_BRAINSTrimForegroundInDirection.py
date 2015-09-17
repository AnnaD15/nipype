from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.utilities.brains import BRAINSTrimForegroundInDirection

def test_BRAINSTrimForegroundInDirection_inputs():
    input_map = dict(BackgroundFillValue=dict(argstr='--BackgroundFillValue %s',
    ),
    args=dict(argstr='%s',
    ),
    closingSize=dict(argstr='--closingSize %d',
    ),
    directionCode=dict(argstr='--directionCode %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    headSizeLimit=dict(argstr='--headSizeLimit %f',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='--inputVolume %s',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    otsuPercentileThreshold=dict(argstr='--otsuPercentileThreshold %f',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = BRAINSTrimForegroundInDirection.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BRAINSTrimForegroundInDirection_outputs():
    output_map = dict(outputVolume=dict(),
    )
    outputs = BRAINSTrimForegroundInDirection.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

