import itk

def apply_transform_to_segmentation(
    segmentation,
    transform_parameter_object
):

    # ======================================
    # FORCE NEAREST-NEIGHBOR
    # ======================================
    parameter_map = (
        transform_parameter_object
        .GetParameterMap(0)
    )

    parameter_map["FinalBSplineInterpolationOrder"] = ["0"]
    transform_parameter_object.SetParameterMap(0, parameter_map)

    # ======================================
    # APPLY TRANSFORM
    # ======================================
    result = itk.transformix_filter(
        segmentation,
        transform_parameter_object = transform_parameter_object
    )

    return result
