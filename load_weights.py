from build_model import build_conv1d_model, build_conv1d_res_model

def load_weights(name_model):
    if name_model == build_conv1d_model:
        file_weight = "conv1d_ptb.h5"

    elif name_model == build_conv1d_res_model:
        file_weight = "conv1d_res_ptb.h5"

    return file_weight