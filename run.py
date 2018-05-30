import argparse
import logging
import time
import ast

import cv2
import numpy as np
import tf_pose_estimation.common as common
from tf_pose_estimation.estimator import TfPoseEstimator
from tf_pose_estimation.networks import get_graph_path, model_wh

logger = logging.getLogger('TfPoseEstimator')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation run')

    parser.add_argument('--image', type=str, default='./images/p1.jpg')
    parser.add_argument('--model', type=str, default='cmu', help='cmu / mobilenet_thin')
    parser.add_argument('--models-dir', type=str, default='.', help='folder with \'models\' folder')
    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

    
    args = parser.parse_args()
    
    w, h = model_wh(args.resize)
    graph_path = get_graph_path(model_name=args.model, base_path=args.models_dir)
    if w == 0 or h == 0:
        e = TfPoseEstimator(graph_path, target_size=(432, 368))
    else:
        e = TfPoseEstimator(graph_path, target_size=(w, h))
    
    image = common.read_imgfile(args.image, None, None)
    for k in range(10):
        t = time.time()
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
        elapsed = time.time() - t
        logger.info('inference image: %s in %.4f seconds.' % (args.image, elapsed))

    image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
    cv2.imwrite('output.png', image)