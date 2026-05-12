import itk
#import SimpleITK as sitk


def build_initial_parameter_object():
    parameter_object = itk.ParameterObject.New()
    parameter_map    = parameter_object.GetDefaultParameterMap("rigid")
    parameter_map["AutomaticTransformInitialization"]       = ["true"]
    parameter_map["MaximumNumberOfIterations"]              = ["500"]
    parameter_map["AutomaticTransformInitializationMethod"] = ["CenterOfGravity"]
    parameter_map["Metric"]                                 = ["AdvancedMeanSquares"]
    parameter_object.AddParameterMap(parameter_map)
    return parameter_object


'''def configure_initial_registration():
    parameter_map = sitk.GetDefaultParameterMap("rigid")
    parameter_map["AutomaticTransformInitialization"]       = ["true"]
    parameter_map["MaximumNumberOfIterations"]              = ["500"]
    parameter_map["AutomaticTransformInitializationMethod"] = ["CenterOfGravity"]
    parameter_map["Metric"]                                 = ["AdvancedMeanSquares"]
    return parameter_map'''