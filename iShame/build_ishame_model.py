import json
import ast

from keras.models import Sequential
from keras.layers import Input, Dense, Activation, MaxPooling2D, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, Dropout
from keras.metrics import MeanSquaredError, CategoricalAccuracy
from keras.initializers import glorot_uniform
import logging


def load_model_def(model_config_filepath):
    with open(model_config_filepath) as f:
        model_def = json.load(f) 

    conv_layers = model_def["conv_layers"]   
    conn_layers = model_def["conn_layers"]

    return conv_layers, conn_layers

def build_model(input_shape, conv_layers, conn_layers, output_classes=None):

    # create sequential model
    model = Sequential()

    # convlutional layers
    # CONV2D -> RELU -> MAXPOOL
    # number of filters, filter_size, and strides retrieved from input conv array

    init_model = True

    for idx, layer in enumerate(conv_layers):
        if init_model:
            model.add(Conv2D(input_shape=input_shape, \
                             filters=layer["num_filters"], \
                             kernel_size=conv_to_tuple(layer["filter_size"]), \
                             strides = conv_to_tuple(layer["stride_size"]), \
                             activation = layer["activation"], \
                             kernel_initializer = glorot_uniform(seed=0), \
                             name = 'conv_'+str(idx)))
        else:
            model.add(Conv2D(filters=layer["num_filters"], \
                             kernel_size=conv_to_tuple(layer["filter_size"]), \
                             strides = conv_to_tuple(layer["stride_size"]), \
                             activation = layer["activation"], \
                             kernel_initializer = glorot_uniform(seed=0), \
                             name = 'conv_'+str(idx)))

        model.add(MaxPooling2D(pool_size=conv_to_tuple(layer["pool_size"]), \
                                strides=conv_to_tuple(layer["stride_size"]), \
                                name="max_pool_"+str(idx)))            
        
        init_model = False

    # add fully connected layers
    model.add(Flatten())

    for idx, layer in enumerate(conn_layers):
        model.add(Dense(units=layer["hidden_units"], \
                        activation=layer["activation"], 
                        name="fully_connected_"+str(idx)))
        if "dropout" in layer:
            model.add(Dropout(rate=layer["dropout"]))

    # if classification, add softmax output layer
    # otherwise, add singular output layer with one unit with NO activation
    if output_classes is not None:
        model.add(Dense(units=output_classes, \
                        activation='softmax', \
                        kernel_initializer = glorot_uniform(seed=0), \
                        name='class_output_'+str(output_classes)))
    else:
        model.add(Dense(units=1, name = 'regression_output'))

    return model

def load_model_with_weights(model_config_filepath, model_weights_path, input_shape, output_classes):
    conv_layers, conn_layers = load_model_def(model_config_filepath)

    model = build_model(input_shape, conv_layers, conn_layers, output_classes)
    model.load_weights(model_weights_path)

    return model

def compile_model(model, is_regression):
    if(is_regression):
        loss="mean_squared_error"
        metrics=[MeanSquaredError()]
    else:
        loss="categorical_crossentropy"
        metrics=[CategoricalAccuracy()]
    
    model.compile(optimizer='adam', loss=loss, metrics=metrics)

def conv_to_tuple(input):
    return ast.literal_eval(input)