# -*- coding: utf8 -*-
"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""
from __future__ import unicode_literals

from nipype.interfaces.base import CommandLine, CommandLineInputSpec, SEMLikeCommandLine, TraitedSpec, File, Directory, traits, isdefined, InputMultiPath, OutputMultiPath
import os


class BRAINSPosteriorToContinuousClassInputSpec(CommandLineInputSpec):
    inputWhiteVolume = File(desc="White Matter Posterior Volume", exists=True, argstr="--inputWhiteVolume %s")
    inputBasalGmVolume = File(desc="Basal Grey Matter Posterior Volume", exists=True, argstr="--inputBasalGmVolume %s")
    inputSurfaceGmVolume = File(desc="Surface Grey Matter Posterior Volume", exists=True, argstr="--inputSurfaceGmVolume %s")
    inputCsfVolume = File(desc="CSF Posterior Volume", exists=True, argstr="--inputCsfVolume %s")
    inputVbVolume = File(desc="Venous Blood Posterior Volume", exists=True, argstr="--inputVbVolume %s")
    inputCrblGmVolume = File(desc="Cerebellum Grey Matter Posterior Volume", exists=True, argstr="--inputCrblGmVolume %s")
    inputCrblWmVolume = File(desc="Cerebellum White Matter Posterior Volume", exists=True, argstr="--inputCrblWmVolume %s")
    outputVolume = traits.Either(traits.Bool, File(), hash_files=False, desc="Output Continuous Tissue Classified Image", argstr="--outputVolume %s")


class BRAINSPosteriorToContinuousClassOutputSpec(TraitedSpec):
    outputVolume = File(desc="Output Continuous Tissue Classified Image", exists=True)


class BRAINSPosteriorToContinuousClass(SEMLikeCommandLine):

    """title: Tissue Classification

category: BRAINS.Classify

description: This program will generate an 8-bit continuous tissue classified image based on BRAINSABC posterior images.

version: 3.0

documentation-url: http://www.nitrc.org/plugins/mwiki/index.php/brains:BRAINSClassify

license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt

contributor: Vincent A. Magnotta

acknowledgements: Funding for this work was provided by NIH/NINDS award NS050568

"""

    input_spec = BRAINSPosteriorToContinuousClassInputSpec
    output_spec = BRAINSPosteriorToContinuousClassOutputSpec
    _cmd = " BRAINSPosteriorToContinuousClass "
    _outputs_filenames = {'outputVolume': 'outputVolume'}
    _redirect_x = False
