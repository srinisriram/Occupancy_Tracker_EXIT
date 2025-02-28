# This file defines the constants used in this package.

from enum import Enum

MAX_OCCUPANCY = 250
SPEECH_FILENAME = 'speech2.wav'
SERVER_PORT = 10000
MAX_NUMBER_OF_RCV_BYTES = 1024

# object detection model
MODEL_NAME = "models/MobileNetSSD_deploy.caffemodel"

# proto text file of the object detection model
PROTO_TEXT_FILE = "models/MobileNetSSD_deploy.prototxt"

# Frame width.
FRAME_WIDTH_IN_PIXELS = 400

# Maximum consecutive frames a given object is allowed to be
# marked as "disappeared" until we need to deregister the object from tracking.
MAX_NUM_OF_CONSECUTIVE_FRAMES_FOR_ACTION = 18

# Maximum distance between centroids to associate an object --
# if the distance is larger than this maximum distance we'll
# start to mark the object as "disappeared".
MAX_DISTANCE_FROM_THE_OBJECT = 100

# Column traversal
COLUMN = 1

# minimum confidence
MIN_CONFIDENCE = 0.7

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
MAX_TRACKER_LIST_SIZE = 10

OPEN_DISPLAY = True

VIDEO_DEV_ID = 0

SEND_EMAIL = True

TIMEOUT_FOR_TRACKER = 2


TEST_VIDEO_FILE_PATH_1 = 'videos/example_01.mp4'
TEST_VIDEO_FILE_PATH_2 = 'videos/example_02.mp4'

# Log file name
ENTER_LOG_FILE_NAME = "enter_file.csv"
PEER_ENTER_LOG_FILE_NAME = "peer_enter_file.csv"
EXIT_LOG_FILE_NAME = "exit_file.csv"
PEER_EXIT_LOG_FILE_NAME = "peer_exit_file.csv"
WEEKLY_LOG_FILE_NAME = "weekly_enter_file.csv"
MONTHLY_LOG_FILE_NAME = "monthly_enter_file.csv"

# Time for sending the Email
HOUR = 22
MINUTE = 0
DAY = "Saturday"
DATE = 24

USE_PI_CAMERA = True

CLEAR_FILES = False

OCCUPATION_LOG = "/home/pi/Occupation.log"

MERGE_FILES = True

class Direction(Enum):
    ENTER = 1
    EXIT = 2


USE_RASPBERRY_PI = True

MIN_DIST_TRAVELED = 25

MERGED_ENTER_CSV = "merge_file_enter.csv"

MERGED_EXIT_CSV = "merge_file_exit.csv"

# HR email send
START_TIME_HR = 8
END_TIME_HR = 22

HOURLY_CSV = "hourly.csv"
