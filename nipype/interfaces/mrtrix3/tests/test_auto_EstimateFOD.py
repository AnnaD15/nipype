from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix3.reconst import EstimateFOD

def test_EstimateFOD_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bval_scale=dict(argstr='-bvalue_scaling %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    grad_file=dict(argstr='-grad %s',
    ),
    grad_fsl=dict(argstr='-fslgrad %s %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_bval=dict(),
    in_bvec=dict(argstr='-fslgrad %s %s',
    ),
    in_dirs=dict(argstr='-directions %s',
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    in_mask=dict(argstr='-mask %s',
    ),
    max_sh=dict(argstr='-lmax %d',
    ),
    n_iter=dict(argstr='-niter %d',
    ),
    neg_lambda=dict(argstr='-neg_lambda %f',
    ),
    nthreads=dict(argstr='-nthreads %d',
    nohash=True,
    ),
    out_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    usedefault=True,
    ),
    response=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    sh_filter=dict(argstr='-filter %s',
    ),
    shell=dict(argstr='-shell %s',
    sep=',',
    ),
    terminal_output=dict(nohash=True,
    ),
    thres=dict(argstr='-threshold %f',
    ),
    )
    inputs = EstimateFOD.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_EstimateFOD_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = EstimateFOD.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

