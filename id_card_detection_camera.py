"""
This script is used to perform real-time object detection using TensorFlow and OpenCV.
It detects objects in a webcam feed, draws bounding boxes around the detected objects, and displays the feed in a window.

Usage: Run the script in an environment with TensorFlow, OpenCV, and numpy installed.
Press 'q' to quit the video window.
"""

# Import necessary packages
import os
import sys
import cv2
import numpy as np
import tensorflow as tf

# Append the path for utility scripts
sys.path.append("..")

# Import utilities for label maps and visualization
from utils import label_map_util, visualization_utils as vis_util

# Constants
MODEL_NAME = 'model'
CWD_PATH = os.getcwd()
PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH, 'data', 'labelmap.pbtxt')
NUM_CLASSES = 1

def load_model_and_labels():
    """
    Loads the trained model and label map.

    Returns:
    tuple: (session, detection graph, category index)
    """
    # Load the label map and convert it to categories
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(
        label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Load the TensorFlow model into memory
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

    return sess, detection_graph, category_index


def object_detection_webcam(sess, detection_graph, category_index):
    """
    Perform object detection using webcam feed.

    Args:
    sess: TensorFlow Session
    detection_graph: TensorFlow graph object
    category_index: Dictionary mapping labels to category names
    """
    # Define tensors for the graph
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    # Initialize webcam
    video = cv2.VideoCapture(0)
    ret = video.set(3, 1280)
    ret = video.set(4, 720)

    try:
        while True:
            ret, frame = video.read()
            frame_expanded = np.expand_dims(frame, axis=0)

            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores, detection_classes, num_detections],
                feed_dict={image_tensor: frame_expanded})

            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8,
                min_score_thresh=0.60)

            cv2.imshow('ID CARD DETECTOR', frame)

            if cv2.waitKey(1) == ord('q'):
                break

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    session, graph, index = load_model_and_labels()
    object_detection_webcam(session, graph, index)
