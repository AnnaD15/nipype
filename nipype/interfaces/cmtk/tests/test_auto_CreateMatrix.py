from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.cmtk.cmtk import CreateMatrix

def test_CreateMatrix_inputs():
    input_map = dict(count_region_intersections=dict(usedefault=True,
    ),
    out_endpoint_array_name=dict(genfile=True,
    ),
    out_fiber_length_std_matrix_mat_file=dict(genfile=True,
    ),
    out_intersection_matrix_mat_file=dict(genfile=True,
    ),
    out_matrix_file=dict(genfile=True,
    ),
    out_matrix_mat_file=dict(usedefault=True,
    ),
    out_mean_fiber_length_matrix_mat_file=dict(genfile=True,
    ),
    out_median_fiber_length_matrix_mat_file=dict(genfile=True,
    ),
    resolution_network_file=dict(mandatory=True,
    ),
    roi_file=dict(mandatory=True,
    ),
    tract_file=dict(mandatory=True,
    ),
    )
    inputs = CreateMatrix.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_CreateMatrix_outputs():
    output_map = dict(endpoint_file=dict(),
    endpoint_file_mm=dict(),
    fiber_label_file=dict(),
    fiber_labels_noorphans=dict(),
    fiber_length_file=dict(),
    fiber_length_std_matrix_mat_file=dict(),
    filtered_tractographies=dict(),
    filtered_tractography=dict(),
    filtered_tractography_by_intersections=dict(),
    intersection_matrix_file=dict(),
    intersection_matrix_mat_file=dict(),
    matlab_matrix_files=dict(),
    matrix_file=dict(),
    matrix_files=dict(),
    matrix_mat_file=dict(),
    mean_fiber_length_matrix_mat_file=dict(),
    median_fiber_length_matrix_mat_file=dict(),
    stats_file=dict(),
    )
    outputs = CreateMatrix.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

