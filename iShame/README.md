# iShame

The iShame Model Predictor is a REST API endpoint that loads a model that can be invoked to predict whether a given image depicts a full coffee pot, or should be flagged for further review of the offending culprit for summary execution. 

iShame models consists of a series of convolutional neural network layers, followed by a series of connected layers. They can be built in either of two paradigms:

    1. Classification

    Models are trained to predict a range of output classes, with images being placed in buckets - "Empty Coffee Pot", "Medium Full Coffee Pot", "Full Coffee Pot", etc..

    2. Regression

    Models are trained to predict the estimated coffee pot fullness, on a scale from 0.0 to 1.0.    

See iShame Model Definition below for more information on the model build configuration.

`preprocess_images.py` contains the helper methods used for preprocessing of images (scaling, adjusting color, etc.). It is used for both training (see the Jupyter notebook `process_label_videos.ipynb`) and by the endpoint.

`build_ishame_model.py` contains the helper methods used for building the iShame model from the configuration and loading pretrained weights. It is used for both training (see the Jupyter notebook `process_label_videos.ipynb`) and by the endpoint.

## Prerequisites

Numpy, Keras, and OpenCV are required to build / train models and run the iShame Model Predictor. The iShame Model Predictor is built using the python Flask library. 

## Usage 

### iShame Model Definition

iShame models are defined in JSON format. 

`conv_layers` is an array defining a number of convolutional neural network layers. Each CNN layer has the following hyperparameters: 

    * `num_filters`: number of filters / kernels for the layer.

    * `filter_size`: size of the filter in each dimension. Defined as a string 2D tuple.

    * `stride_size`: size of the stride in each dimension. Defined as a string 2D tuple.

    * `activation`: activation function for the CNN layer. Should be a valid keras activation function.

    * `pool_size`: size of pooling in each dimension. Currently max pooling layers are used.

No padding is defined for CNN layers at this time.

`conn_layers` is an array defining a number of flattened, fully-connected neural network layers. Each connected layer has the following hyperparameters: 

    * `hidden_units`: number of neurons for the layer.

    * `activation`: activation function for the connected layer. Should be a valid keras activation function.

    * `dropout`: percentage of neurons that would drop out for regularization. 

The sample iShame model (also included in the file `iShameModel.json`) is shown here.

```
{
"conv_layers": [
    {"num_filters": 16,
    "filter_size": "(5,5)",
    "stride_size": "(2,2)",
    "activation": "relu",
    "pool_size": "(2,2)"
    },
    {"num_filters": 32,
    "filter_size": "(5,5)",
    "stride_size": "(2,2)",
    "activation": "relu",
    "pool_size": "(2,2)"
    },
    {"num_filters": 64,
    "filter_size": "(5,5)",
    "stride_size": "(2,2)",
    "activation": "relu",
    "pool_size": "(2,2)"
    }
],    
"conn_layers": [
    {"hidden_units": 20,
    "activation": "relu",
    "dropout": 0.5
    },
    {"hidden_units": 10,
    "activation": "relu"
    }
]
}
```

### Starting the iShame Model Predictor

`iShameModelPredictor` can be invoked automatically from the command line. It loads the provided model, and starts a REST API endpoint for prediction at the `predict` route on port 5000.

*Arguments*

* `model-config`

    Filepath to trained model configuration (see above). [Required]

* `model-weights`
    
    Filepath to saved model weights, in h5 format. [Required]

* `output-classes`
    
    Number of output classes for model. If not included, assumed to be regression model [range 0.0-1.0] [Required]

*Example Usage*

```
python iShameModelPredictor.py 
--model-config /path/to/model/model_config.json
--model-weights /path/to/model/model_weights.h5
--output-classes 6
```

### Making a Prediction

An HTTP POST request should be sent with the JSON of the requested images to predict. The JSON contains an array of image paths under the heading of `image_paths`.

A sample JSON request (also included as `image_prediction.json`) is shown here.

```
{
    "image_paths": [
        "/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/frames/0_140.png",
        "/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/frames/2_160.png",
        "/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/frames/4_60.png"
    ]
}
```

The response returns the same array, with the predictions for each image attached. If it is a classifcation model, it also returns the predicted class, which is the class label with the highest probability.  

An example call of the API and response is shown here.

*Call*
```
curl -i -H "Content-Type: application/json" -X POST -d @image_prediction.json http://localhost:5000/predict
```

*Response*
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 767
Server: Werkzeug/1.0.1 Python/3.7.3
Date: Tue, 18 Aug 2020 22:49:55 GMT

{"predictions":[{"image_path":"/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/frames/0_140.png","predicted_class":3,"prediction":[0.13342617452144623,0.12521781027317047,0.19284148514270782,0.21513527631759644,0.13632124662399292,0.1970580667257309]},{"image_path":"/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/frames/2_160.png","predicted_class":3,"prediction":[0.12798205018043518,0.12305533140897751,0.19752813875675201,0.2193702757358551,0.13577957451343536,0.19628462195396423]},{"image_path":"/c/Users/rrr0901/Documents/Workspace/iShame/data/coffee_video/frames/4_60.png","predicted_class":3,"prediction":[0.13860520720481873,0.13851980865001678,0.18967372179031372,0.19793175160884857,0.1459505409002304,0.18931901454925537]}]}
```