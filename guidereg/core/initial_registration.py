from guidereg.backends.itk_elastix_backend import ITKElastixBackend
from guidereg.core.parameter_maps import build_initial_parameter_object

def run_initial_registration(
    fixed_image,
    moving_image,
    fixed_mask      = None,
    moving_mask     = None,
    output_directory= None,
    logger          = None
):

    # ======================================
    # BUILD PARAMETERS
    # ======================================
    parameter_object = build_initial_parameter_object() 

    # ======================================
    # BACKEND
    # ======================================
    backend = ITKElastixBackend(
        parameter_object = parameter_object,
        output_directory = output_directory,
        logger           = logger
    )

    # ======================================
    # RUN REGISTRATION
    # ======================================
    result_image, result_transform = (
        backend.register(
            fixed_image  = fixed_image,
            moving_image = moving_image,
            fixed_mask   = fixed_mask,
            moving_mask  = moving_mask
        )
    )
    return result_image, result_transform