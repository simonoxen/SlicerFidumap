*work in progress*

# SlicerFidumap

This 3D-Slicer (Slicer) extension provides an interface to [fidumap](https://github.com/simonoxen/fidumap), an image registration framework based on detecting relevant fiducials.

## Installation

This extension is currently under development and not available from the Slicer extensions manager. It can be manually installed by downloading this repo and adding the respective folders to the modules path in the Slicer settings.

It depends on the fidumap package, which should also be manually installed. This can be done by downloading the repo and running `pip_install(path_to_fidumap)` in the Slicer python interactor.

## Modules

- FidumapRegister

This module provides the main functionality of the extension. Its inputs are a moving image, a fixed image, and a trained fidumap model. It runs inference and outputs the transformation, resampled image, and detected fiducials.

- FidumapExtract

This module only extracts relevant fiducials from an input image (the intermediate step for the registration).

## Example

The following is a screenshot before and after running FidumapRegister on the example datasets MRBrainTumor1 and MRBrainTumor2

![](resources/registration.png?raw=true)

