### Klibs Parameter overrides ###

#########################################
# Runtime Settings
#########################################
collect_demographics = False
manual_demographics_collection = False
manual_trial_generation = False
run_practice_blocks = True
multi_user = False
view_distance = 57 # in centimeters, 57cm = 1 deg of visual angle per cm of screen

#########################################
# Available Hardware
#########################################
eye_tracker_available = False
#use -ELX for mouse if looking 
eye_tracking = False
# if this is true and E_T_A is false it will give you mouse control
labjack_available = False
labjacking = False
#labjack not working
#########################################
# Environment Aesthetic Defaults
#########################################
default_fill_color = (45, 45, 45, 255)
default_color = (255, 255, 255, 255)
default_font_size = 23
#For degrees, .5 is typically good
default_font_unit = 'px'
#define in degrees when possible (deg)
default_font_name = 'Hind-Medium'
#other is roboto medium
#########################################
# EyeLink Settings
#########################################
manual_eyelink_setup = False
manual_eyelink_recording = False

saccadic_velocity_threshold = 20
saccadic_acceleration_threshold = 5000
saccadic_motion_threshold = 0.15
#DONT MESS WITH THIS
#########################################
# Experiment Structure
#########################################
multi_session_project = False
trials_per_block = 0
blocks_per_experiment = 1
table_defaults = {} 

#ignore table defaults
#multi session means that if you put duplicate ID, it will ask you to continue
#trials per block and blocks are obvious

#########################################
# Development Mode Settings
#########################################
dm_auto_threshold = True
dm_trial_show_mouse = True
dm_ignore_local_overrides = False
dm_show_gaze_dot = True

#########################################
# Data Export Settings
#########################################
primary_table = "trials"
unique_identifier = "userhash"
default_participant_fields = [[unique_identifier, "participant"], "gender", "age", "handedness"]
default_participant_fields_sf = [[unique_identifier, "participant"], "random_seed", "gender", "age", "handedness"]

#########################################
# PROJECT-SPECIFIC VARS
#########################################
