# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 19:01:05 2017

@author: VK046010
"""
# import tensorflow as tf
# import numpy as np
# from django.conf import settings
# #import json

# FOLDER_PREFIX = settings.TF_ROOT

# # Paths to files producted as part of retraining Inception.  Change these if you saved your files in
# #   a different location.
# #   Retrained graph
# MODEL_PATH = FOLDER_PREFIX+"output_graph.pb"
# #   Labels the newly retrained graph.  These would be the new classes being classified 
# #       such as "Rose, Dandillion, ..."
# LABEL_PATH = FOLDER_PREFIX+"output_labels.txt"

# # Load the retrained inception based graph
# with tf.gfile.FastGFile(MODEL_PATH, 'rb') as f:
#         # init GraphDef object
#         graph_def = tf.GraphDef()
#         # Read in the graphy from the file
#         graph_def.ParseFromString(f.read())
#         _ = tf.import_graph_def(graph_def, name='')
#     # this point the retrained graph is the default graph

# #   read the class labels in from the label file
# f = open(LABEL_PATH, 'rb')
# lines = f.readlines()
# labels = [str(w).replace("\n", "") for w in lines]

# sess = tf.Session()
# softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

# # Load the retrained graph as the default graph 
# # def load_graph(modelPath):

# #     with tf.gfile.FastGFile(modelPath, 'rb') as f:
# #         # init GraphDef object
# #         graph_def = tf.GraphDef()
# #         # Read in the graphy from the file
# #         graph_def.ParseFromString(f.read())
# #         _ = tf.import_graph_def(graph_def, name='')
# #         # this point the retrained graph is the default graph


# #   Remove ugly characters from strings
# def filter_delimiters(text):
#     filtered = text[:-3]
#     filtered = filtered.strip("b'")
#     filtered = filtered.strip("'")
#     return filtered


# def predict_image_class(image_data):
    
#     #matches = None # Default return to none

#     #if not tf.gfile.Exists(imagePath):
#     #    tf.logging.fatal('File does not exist %s', imagePath)
#     #    return matches

#     # Load the image from file
#     #image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

#     #   Get the predictions on our image by add the image data to the tensor
#     predictions = sess.run(softmax_tensor,
#                         {'DecodeJpeg/contents:0': image_data})
    
#     # Format predicted classes for display
#     #   use np.squeeze to convert the tensor to a 1-d vector of probability values
#     predictions = np.squeeze(predictions)

#     top_k = predictions.argsort()[-5:][::-1]  # Getting the indicies of the top 5 predictions

#     print("")
#     print ("Image Classification Probabilities")
#     #   Output the class probabilites in descending order
#     json_res = {}
#     for node_id in top_k:
#         human_string = filter_delimiters(labels[node_id])
#         score = predictions[node_id]
#         print('{0:s} (score = {1:.5f})'.format(human_string, score))
#         json_res[human_string] = float(score)

#         #answer = labels[top_k[0]]
#     #print(type(json_res))
#     #json_str = json.dumps( (json_res) )
#     return json_res
