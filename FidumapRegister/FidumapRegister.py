#!/usr/bin/env python-real

import sys
import os
import csv
import json

def csv_to_json(csv_file, json_file):

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    json_data = {
        "@schema": "https://raw.githubusercontent.com/Slicer/Slicer/main/Modules/Loadable/Markups/Resources/Schema/markups-schema-v1.0.0.json#",
        "markups": [
            {
                "type": "Fiducial",
                "coordinateSystem": "RAS",
                "controlPoints": [
                    {
                        "label": f"F-{i+1}",
                        "position": [float(row[0]), float(row[1]), float(row[2])]
                    } for i, row in enumerate(data)
                ]
            }
        ]
    }

    with open(json_file, 'w') as f:
        json.dump(json_data, f, indent=4)
    
    os.remove(csv_file)

if __name__ == "__main__":

    n_fiducials = int(sys.argv[1])
    model_file = sys.argv[2] if os.path.exists(sys.argv[2]) else None
    moving_volume = sys.argv[3]
    fixed_volume = sys.argv[4]
    output_transform = sys.argv[5]
    output_volume = sys.argv[6]
    output_moving_fiducials = sys.argv[7]
    output_fixed_fiducials = sys.argv[8]

    output_prefix = os.path.join(os.path.dirname(output_volume), 'out')
    
    from fidumap.eval.register import main
    main(n_fiducials, model_file, moving_volume, fixed_volume, output_prefix)
    
    os.rename(output_prefix + '_transform.tfm', output_transform)
    os.rename(output_prefix + '_img.nrrd', output_volume)
    csv_to_json(output_prefix + '_fiducials_moving.csv', output_moving_fiducials)
    csv_to_json(output_prefix + '_fiducials_fixed.csv', output_fixed_fiducials)


