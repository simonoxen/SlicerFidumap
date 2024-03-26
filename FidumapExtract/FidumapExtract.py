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
    input_volume = sys.argv[3]
    output_volume = sys.argv[4]
    output_fiducials = sys.argv[5]

    output_prefix = os.path.join(os.path.dirname(output_volume), 'out')
    
    from fidumap.eval.extract import main
    main(n_fiducials, model_file, input_volume, output_prefix)
    
    os.rename(output_prefix + '_img.nrrd', output_volume)
    csv_to_json(output_prefix + '_fiducials.csv', output_fiducials)


