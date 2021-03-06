# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..developer import JistLaminarProfileSampling


def test_JistLaminarProfileSampling_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inCortex=dict(argstr="--inCortex %s", extensions=None,),
        inIntensity=dict(argstr="--inIntensity %s", extensions=None,),
        inProfile=dict(argstr="--inProfile %s", extensions=None,),
        null=dict(argstr="--null %s",),
        outProfile2=dict(argstr="--outProfile2 %s", hash_files=False,),
        outProfilemapped=dict(argstr="--outProfilemapped %s", hash_files=False,),
        xDefaultMem=dict(argstr="-xDefaultMem %d",),
        xMaxProcess=dict(argstr="-xMaxProcess %d", usedefault=True,),
        xPrefExt=dict(argstr="--xPrefExt %s",),
    )
    inputs = JistLaminarProfileSampling.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_JistLaminarProfileSampling_outputs():
    output_map = dict(
        outProfile2=dict(extensions=None,), outProfilemapped=dict(extensions=None,),
    )
    outputs = JistLaminarProfileSampling.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
