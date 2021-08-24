from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from build_model import build_conv1d_model,build_conv1d_res_model

def choose_model(name_model, input_shape):
    if name_model == build_conv1d_model:
        checkpoint_cb = ModelCheckpoint("conv1d_ptb.h5", save_best_only=True)
        earlystop_cb = EarlyStopping(patience=5, restore_best_weights=True)
        model_conv1d_ptb = build_conv1d_model(input_shape)

    elif name_model == build_conv1d_res_model:
        checkpoint_cb = ModelCheckpoint("conv1d_res_ptb.h5", save_best_only=True)
        earlystop_cb = EarlyStopping(patience=5, restore_best_weights=True)
        model_conv1d_ptb = build_conv1d_res_model(input_shape)

    return model_conv1d_ptb, checkpoint_cb, earlystop_cb