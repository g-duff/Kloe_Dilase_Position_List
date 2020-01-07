import os
import Functions.InputOutput as io
import Functions.PositionBuilder as pb
from datetime import datetime

root = os.getcwd()
position_list_dir = os.path.join(root,
                                 '..',
                                 '..',
                                 'Kloe')
io.check_dir_exists(position_list_dir)

## Firstly, what should a Kloe Dilase 650 position list look like? ##
## "ALS" "Ligne2/Laser1" ##
## "LWO" "File Name" "Modulation" "Velocity" "x-offset" "y-offset" "z-offset" ##

position_initial = {'file_name' : 'Test.lwo',
                    'laser' : 0.5,
                    'modulation' : 5,
                    'velocity' : 5,
                    'x_initial' : 0,
                    'y_initial' : 0,
                    'z_initial' : 0,
                    'repeat_patterns' : 5,
                    }

## pattern_shift = [modulation, velocity, x, y, z, repeats] ##
pattern_shift = [0, 5, 0, 1, 0, 5]
position_list = pb.position_list(pos_i=position_initial,
                                 shift_array=pattern_shift)

## pattern_repeat = [modulation, velocity, x, y, z, repeats] ##
pattern_repeat = [10, 0, 1, 1.5, 1, 2]
position_final = pb.repeat_position_list(pos_array=position_list,
                                         repeat_array=pattern_repeat)

date = datetime.date(datetime.now())
output_name = f'test_file9_{date}'
output_path = os.path.join(position_list_dir,
                           f'{output_name}.xdfl')
io.write_out_file(out_path=output_path,
                  array=position_final)
