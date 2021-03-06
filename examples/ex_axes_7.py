# ex_axes_7.py

import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *

N_params = {'u_min': 1.0,
            'u_max': 10.0,
            'function': lambda u: u,
            'title': 'title',
            'tick_levels': 2,
            'tick_text_levels': 1,
            'tick_side': 'left',
            'scale_type': 'manual line',
            'manual_axis_data': {1.0: 'one',
                                 2.0: 'two',
                                 3.0: 'three',
                                 3.1415: r'$\pi$',
                                 4.0: 'four',
                                 5.0: 'five',
                                 6.0: 'six',
                                 7.0: 'seven',
                                 8.0: 'eight',
                                 9.0: 'nine',
                                 10.0: 'ten'},
            'extra_params': [{'u_min': 1.0,
                              'u_max': 10.0,
                              'scale_type': 'linear',
                              'tick_levels': 3,
                              'tick_text_levels': 2,
                              'tick_side': 'right',
                              }]
            }
block_params = {'block_type': 'type_8',
                'f_params': N_params,
                'width': 5.0,
                'height': 10.0,
                }
main_params = {'filename': 'ex_axes_7.pdf',
               'paper_height': 10.0,
               'paper_width': 5.0,
               'block_params': [block_params],
               'transformations': [('scale paper',)]
               }
Nomographer(main_params)
