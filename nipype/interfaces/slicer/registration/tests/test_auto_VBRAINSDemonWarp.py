from __future__ import unicode_literals
# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.slicer.registration.specialized import VBRAINSDemonWarp

def test_VBRAINSDemonWarp_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    arrayOfPyramidLevelIterations=dict(argstr='--arrayOfPyramidLevelIterations %s',
    sep=',',
    ),
    backgroundFillValue=dict(argstr='--backgroundFillValue %d',
    ),
    checkerboardPatternSubdivisions=dict(argstr='--checkerboardPatternSubdivisions %s',
    sep=',',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fixedBinaryVolume=dict(argstr='--fixedBinaryVolume %s',
    ),
    fixedVolume=dict(argstr='--fixedVolume %s...',
    ),
    gradient_type=dict(argstr='--gradient_type %s',
    ),
    gui=dict(argstr='--gui ',
    ),
    histogramMatch=dict(argstr='--histogramMatch ',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    initializeWithDisplacementField=dict(argstr='--initializeWithDisplacementField %s',
    ),
    initializeWithTransform=dict(argstr='--initializeWithTransform %s',
    ),
    inputPixelType=dict(argstr='--inputPixelType %s',
    ),
    interpolationMode=dict(argstr='--interpolationMode %s',
    ),
    lowerThresholdForBOBF=dict(argstr='--lowerThresholdForBOBF %d',
    ),
    makeBOBF=dict(argstr='--makeBOBF ',
    ),
    max_step_length=dict(argstr='--max_step_length %f',
    ),
    medianFilterSize=dict(argstr='--medianFilterSize %s',
    sep=',',
    ),
    minimumFixedPyramid=dict(argstr='--minimumFixedPyramid %s',
    sep=',',
    ),
    minimumMovingPyramid=dict(argstr='--minimumMovingPyramid %s',
    sep=',',
    ),
    movingBinaryVolume=dict(argstr='--movingBinaryVolume %s',
    ),
    movingVolume=dict(argstr='--movingVolume %s...',
    ),
    neighborhoodForBOBF=dict(argstr='--neighborhoodForBOBF %s',
    sep=',',
    ),
    numberOfBCHApproximationTerms=dict(argstr='--numberOfBCHApproximationTerms %d',
    ),
    numberOfHistogramBins=dict(argstr='--numberOfHistogramBins %d',
    ),
    numberOfMatchPoints=dict(argstr='--numberOfMatchPoints %d',
    ),
    numberOfPyramidLevels=dict(argstr='--numberOfPyramidLevels %d',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    outputCheckerboardVolume=dict(argstr='--outputCheckerboardVolume %s',
    hash_files=False,
    ),
    outputDebug=dict(argstr='--outputDebug ',
    ),
    outputDisplacementFieldPrefix=dict(argstr='--outputDisplacementFieldPrefix %s',
    ),
    outputDisplacementFieldVolume=dict(argstr='--outputDisplacementFieldVolume %s',
    hash_files=False,
    ),
    outputNormalized=dict(argstr='--outputNormalized ',
    ),
    outputPixelType=dict(argstr='--outputPixelType %s',
    ),
    outputVolume=dict(argstr='--outputVolume %s',
    hash_files=False,
    ),
    promptUser=dict(argstr='--promptUser ',
    ),
    registrationFilterType=dict(argstr='--registrationFilterType %s',
    ),
    seedForBOBF=dict(argstr='--seedForBOBF %s',
    sep=',',
    ),
    smoothDisplacementFieldSigma=dict(argstr='--smoothDisplacementFieldSigma %f',
    ),
    terminal_output=dict(nohash=True,
    ),
    upFieldSmoothing=dict(argstr='--upFieldSmoothing %f',
    ),
    upperThresholdForBOBF=dict(argstr='--upperThresholdForBOBF %d',
    ),
    use_vanilla_dem=dict(argstr='--use_vanilla_dem ',
    ),
    weightFactors=dict(argstr='--weightFactors %s',
    sep=',',
    ),
    )
    inputs = VBRAINSDemonWarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_VBRAINSDemonWarp_outputs():
    output_map = dict(outputCheckerboardVolume=dict(),
    outputDisplacementFieldVolume=dict(),
    outputVolume=dict(),
    )
    outputs = VBRAINSDemonWarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

