from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.semtools.segmentation.specialized import BinaryMaskEditorBasedOnLandmarks

def test_BinaryMaskEditorBasedOnLandmarks_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputBinaryVolume=dict(argstr='--inputBinaryVolume %s',
    ),
    inputLandmarkNames=dict(argstr='--inputLandmarkNames %s',
    sep=',',
    ),
    inputLandmarkNamesForObliquePlane=dict(argstr='--inputLandmarkNamesForObliquePlane %s',
    sep=',',
    ),
    inputLandmarksFilename=dict(argstr='--inputLandmarksFilename %s',
    ),
    outputBinaryVolume=dict(argstr='--outputBinaryVolume %s',
    hash_files=False,
    ),
    setCutDirectionForLandmark=dict(argstr='--setCutDirectionForLandmark %s',
    sep=',',
    ),
    setCutDirectionForObliquePlane=dict(argstr='--setCutDirectionForObliquePlane %s',
    sep=',',
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = BinaryMaskEditorBasedOnLandmarks.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_BinaryMaskEditorBasedOnLandmarks_outputs():
    output_map = dict(outputBinaryVolume=dict(),
    )
    outputs = BinaryMaskEditorBasedOnLandmarks.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

