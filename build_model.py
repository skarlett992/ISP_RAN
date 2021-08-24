import tensorflow as tf
import tensorflow_addons as tfa
from tensorflow import keras
from tensorflow.keras.layers import Dense, Conv1D, \
    MaxPool1D, Flatten, Dropout, BatchNormalization, Concatenate
from tensorflow.keras.models import Model


def build_conv1d_model(input_shape):
    model = keras.models.Sequential()

    model.add(Conv1D(32, 7, padding='same', input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(MaxPool1D(5, padding='same'))

    model.add(Conv1D(64, 7, padding='same'))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(MaxPool1D(5, padding='same'))

    model.add(Conv1D(128, 7, padding='same', input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(MaxPool1D(5, padding='same'))

    model.add(Conv1D(256, 7, padding='same'))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(MaxPool1D(5, padding='same'))

    model.add(Conv1D(512, 7, padding='same', input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(tf.keras.layers.ReLU())
    model.add(MaxPool1D(5, padding='same'))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(2, activation="softmax"))
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=[tfa.metrics.F1Score(2, "micro")])
    return model

def build_conv1d_res_model(input_shape):
    model = keras.models.Sequential()

    input_ = tf.keras.layers.Input(shape=(input_shape))

    conv1_1 = Conv1D(64, 7, padding='same', input_shape=input_shape)(input_)
    conv1_1 = BatchNormalization()(conv1_1)
    conv1_1 = tf.keras.layers.ReLU()(conv1_1)

    conv1_2 = Conv1D(64, 7, padding='same')(conv1_1)
    conv1_2 = BatchNormalization()(conv1_2)
    conv1_2 = tf.keras.layers.ReLU()(conv1_2)

    conv1_3 = Conv1D(64, 7, padding='same')(conv1_2)
    conv1_3 = BatchNormalization()(conv1_3)
    conv1_3 = tf.keras.layers.ReLU()(conv1_3)

    concat_1 = Concatenate()([conv1_1, conv1_3])
    max_1 = MaxPool1D(5, padding="same")(concat_1)

    conv1_4 = Conv1D(128, 7, padding='same')(max_1)
    conv1_4 = BatchNormalization()(conv1_4)
    conv1_4 = tf.keras.layers.ReLU()(conv1_4)

    conv1_5 = Conv1D(128, 7, padding='same', input_shape=input_shape)(conv1_4)
    conv1_5 = BatchNormalization()(conv1_5)
    conv1_5 = tf.keras.layers.ReLU()(conv1_5)

    conv1_6 = Conv1D(128, 7, padding='same', input_shape=input_shape)(conv1_5)
    conv1_6 = BatchNormalization()(conv1_6)
    conv1_6 = tf.keras.layers.ReLU()(conv1_6)

    concat_2 = Concatenate()([conv1_4, conv1_6])
    max_2 = MaxPool1D(5, padding="same")(concat_2)

    flat = Flatten()(max_2)
    dense_1 = Dense(512, activation='relu')(flat)
    drop_1 = Dropout(0.5)(dense_1)
    dense_2 = Dense(256, activation='relu')(drop_1)
    drop_2 = Dropout(0.5)(dense_2)
    dense_3 = Dense(128, activation='relu')(drop_2)
    dense_4 = Dense(64, activation='relu')(dense_3)
    dense_5 = Dense(32, activation='relu')(dense_4)
    dense_6 = Dense(2, activation="softmax")(dense_5)

    model = Model(inputs=input_, outputs=dense_6)

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=[tfa.metrics.F1Score(2, "micro")])
    return model

def summary_model(model_conv1d_ptb):
    # model_conv1d_ptb = build_conv1d_model(input_shape=(12, 1))
    model_conv1d_ptb.summary()
    return model_conv1d_ptb




