# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Autobox


def test_Autobox_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(
            argstr="-input %s", copyfile=False, extensions=None, mandatory=True,
        ),
        no_clustering=dict(argstr="-noclust",),
        num_threads=dict(nohash=True, usedefault=True,),
        out_file=dict(
            argstr="-prefix %s",
            extensions=None,
            name_source="in_file",
            name_template="%s_autobox",
        ),
        outputtype=dict(),
        padding=dict(argstr="-npad %d",),
    )
    inputs = Autobox.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Autobox_outputs():
    output_map = dict(
        out_file=dict(extensions=None,),
        x_max=dict(),
        x_min=dict(),
        y_max=dict(),
        y_min=dict(),
        z_max=dict(),
        z_min=dict(),
    )
    outputs = Autobox.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
