import random
import json
import numpy as np
from tqdm import tqdm
import copy
import subprocess
from unidecode import unidecode
import random
from viztracer import VizTracer
tracer = VizTracer()
import re
import calendar

def flat_dict(frame):
    frame.pop("features", None)
    out = []
    for key, item in frame.items():  
        if type(item) is dict:
            out.extend(flat_dict(item))
        else:
            out.append((key,item))
    return out



def generate(num_to_gen):
    # tracer.start()
    out_str = ""
    i = 0
    with tqdm(total=num_to_gen) as pbar:
        while i < num_to_gen:

            speaker_list = ["Sweeper1"]
            addressee_list = ["Ground", "GC", "Ground Control"]
            phrasetype = random.choice(["ask_permission", "confirm_direction", "clarification", "confirm_off", "state_position"])
            movement_list = ["go", "stop", "exit"]
            phonetic_alphabet = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "x-ray", "yankee", "zulu"]
            numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "niner"]
            area_list = ["the CMA", "the hangar"]

            direction1_frame = {
                    "Movement": random.choice(movement_list),
                    "Area": random.choice(area_list),
                    "Runway": {
                        "FirstDigit": random.choice(numbers),
                        "SecondDigit": random.choice(numbers)
                    },
                    "Taxiway": {
                        "Letter": random.choice(phonetic_alphabet)
                    }
                }
            confirm_off_position_frame = {
                    "Movement": "exit",
                    "Area": random.choice(area_list),
                    "Runway": {
                        "FirstDigit": random.choice(numbers),
                        "SecondDigit": random.choice(numbers)
                    },
                    "Taxiway": {
                        "Letter": random.choice(phonetic_alphabet)
                    }
                }
            request_frame = {
                    "Movement": random.choice(["exit", "go"]),
                    "Area": random.choice(area_list),
                    "Runway": {
                        "FirstDigit": random.choice(numbers),
                        "SecondDigit": random.choice(numbers)
                    },
                    "Taxiway": {
                        "Letter": random.choice(phonetic_alphabet)
                    }
                }
            direction2_frame = {
                    "Movement": random.choice(movement_list),
                    "Area": random.choice(area_list),
                    "Runway": {
                        "FirstDigit": random.choice(numbers),
                        "SecondDigit": random.choice(numbers)
                    },
                    "Taxiway": {
                        "Letter": random.choice(phonetic_alphabet)
                    }
                }
            
            directions = [direction1_frame,direction2_frame,confirm_off_position_frame, request_frame]
            for d in directions:
                if random.randint(0,1):
                    d.pop("Area")
                    if random.randint(0,1):
                        d.pop(random.choice(["Runway","Taxiway"]))
                else:
                    d.pop("Runway")
                    d.pop("Taxiway")

            frame = {
                "PhraseType": phrasetype,
                "Addressee": random.choice(addressee_list),
                "Speaker": random.choice(speaker_list),
            }

            if phrasetype == "confirm_direction":
                frame.update({"Direction1":direction1_frame})
                if random.randint(0,1):
                    frame.update({"Direction2":direction2_frame})
            elif phrasetype == "ask_permission":
                frame.update({"Request":request_frame})
            elif phrasetype == "confirm_off":
                frame.update({"Position":confirm_off_position_frame})
            elif phrasetype == "state_position":
                frame.update({"Position":direction1_frame})

            if random.randint(0,1):
                frame.pop("Addressee")
                

            frame2q = {
            }
            

            with open('frame.json', 'w') as frame_file:
                frame_file.write(json.dumps(frame, indent=2).encode("ascii", "ignore").decode())



            cmd = f'java -Xmx16G -jar sfgengine-4.7.0-shaded.jar --generate --sfg ./sweeper.json --with-frame ./frame.json  --text-only'
            print(cmd)
            generated = unidecode(random.choice(subprocess.check_output(cmd).decode(
                "utf-8", errors="ignore").split('//')[:-1]).strip(), errors='ignore')
            print(generated)
            #generated = unidecode(random.choice([x.strip() for x in subprocess.check_output(cmd).decode("utf-8", errors="ignore").split('//')if x.strip() != '']), errors='ignore')
            
            if generated:
                out_json = {
                    "frame" : frame,
                    "generated_text" : generated
                }
                out_str += str(json.dumps(out_json).encode("ascii", "ignore").decode()) + '\n'
                i+=1
                # for key, value in gold_output[:1]:
                #     if value:
                #         value = str(unidecode(value, errors='ignore'))
                #         start_pos = None
                #     else:
                #         start_pos = None
                #         value = None
                #     example_dict = {'context' : generated, 'question' : f'{frame2q[key]}' , 'answers' : {'answer_start' : str(start_pos), 'text' : str(value)}}
                #     out_str += json.dumps(example_dict) + '\n'
                pbar.update(1)
        
        with open('sweeper_sample_outs.json', 'a+', encoding='utf-8') as out_file:
            out_file.write(out_str)
        


 

if __name__ == '__main__':
    open('sweeper_sample_outs.json', 'w', encoding='utf-8').close()
    generate(100)
    