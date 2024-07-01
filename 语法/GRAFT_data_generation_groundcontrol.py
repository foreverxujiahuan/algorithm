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
from abc import ABC, abstractmethod

def flat_dict(frame):
    frame.pop("features", None)
    out = []
    for key, item in frame.items():  
        if type(item) is dict:
            out.extend(flat_dict(item))
        else:
            out.append((key,item))
    return out


class Subframe(ABC):
    #  Requires a dict of frame questions
    @staticmethod
    @abstractmethod
    def frame_questions(s):
        pass
    
    #  Requires a method to generate a random frame
    @classmethod
    @abstractmethod
    def get_random_frame(cls):
        pass


class Direction(Subframe):
    movement_list = ["go", "stop", "exit"]
    yes_no = ["yes", "no"]
    area_list = ["the CMA", "the hangar"]

    def frame_questions(s):
        return {
            "Movement": f"What kind of movement is {s} requesting?",
            "IsImmediate": f"Does the action requested in {s} need to be taken immediately?",
            "Area": f"Which area does {s} reference?",
            "Runway": Runway.frame_questions(s),
            "Taxiway": Taxiway.frame_questions(s)
        }
    
    @classmethod
    def get_random_frame(cls):
        frame = {
            "Movement": random.choice(cls.movement_list),
            "IsImmediate": random.choice(cls.yes_no),
            "Area": random.choice(cls.area_list),
            "Runway": Runway.get_random_frame(),
            "Taxiway": Taxiway.get_random_frame()
        }
        return frame


class Runway(Subframe):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "niner"]

    def frame_questions(s):
        return {
            "FirstDigit": f"What is the first digit of the runway in {s}?",
            "SecondDigit": f"What is the second digit of the runway in {s}?"
        }
    
    @classmethod
    def get_random_frame(cls):
        frame = {
            "FirstDigit": random.choice(cls.numbers),
            "SecondDigit": random.choice(cls.numbers)
        }
        return frame

    


class Taxiway(Subframe):
    phonetic_alphabet = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "x-ray", "yankee", "zulu"]

    def frame_questions(s):
        return {
            "Letter": f"What is the designation of the taxiway in {s}?"
        }
    
    @classmethod
    def get_random_frame(cls):
        frame = {
            "Letter": random.choice(cls.phonetic_alphabet)
        }
        return frame
    

class PhraseType(Subframe):
    phrasetype = ""

    def frame_questions(s):
        return {
            "": "What type of statement is this?"
        }
    @classmethod
    def get_random_frame(cls):
        cls.phrasetype = random.choice(["position", "confirmation", "direction", "direction", "direction", "direction", "direction", "direction"])
        return cls.phrasetype
    

class Addressee(Subframe):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "niner"]
    def frame_questions(s):
        return {
            "": "Who is being addressed?"
        }
    @classmethod
    def get_random_frame(cls):
        return "Sweeper " + random.choice(cls.numbers)
    

class Speaker(Subframe):
    def frame_questions(s):
        return {
            "": "Who is the speaker?"
        }
    @classmethod
    def get_random_frame(cls):
        return "Ground Control"
    

class Report(Subframe):
    yes_no = ["yes", "no"]
    def frame_questions(s):
        return {
            "": "Does the addressee need to report when the action is completed?"
        }
    @classmethod
    def get_random_frame(cls):
        return random.choice(cls.yes_no)




def generate(num_to_gen):
    # tracer.start()
    out_str = ""
    i = 0
    with tqdm(total=num_to_gen) as pbar:
        while i < num_to_gen:

            frame_subframes = {
                "PhraseType": PhraseType,
                "Addressee": Addressee,
                "Speaker": Speaker,
                "Direction1": Direction,
                "Direction2": Direction,
                "Report": Report
            }

            frame = {k : v.get_random_frame() for k, v in frame_subframes.items()}

            phrasetype = frame_subframes["PhraseType"].phrasetype

            direction1 = False
            direction2 = False
            immediate_1 = False
            immediate_2 = False
            if phrasetype == "direction":
                directions = ["Direction1", "Direction2"]
                direction1 = True
                direction2 = True
                if random.randint(0, 1):
                    frame.pop("Direction2")
                    directions.remove("Direction2")
                    direction2 = False
                elif frame["Direction1"]["IsImmediate"] == "yes":
                    frame["Direction2"]["IsImmediate"] = "no"
                elif frame["Direction2"]["IsImmediate"] == "yes":
                    immediate_2 = True
                if frame["Direction1"]["IsImmediate"] == "yes":
                    immediate_1 = True
                for d in directions:
                    current_direction = frame[d]
                    if random.randint(0, 1):
                        current_direction["Runway"].pop("FirstDigit")
                        current_direction["Runway"].pop("SecondDigit")
                    if random.randint(0, 1):
                        current_direction.pop("Taxiway")
                        if random.randint(0, 1):
                            current_direction.pop("Runway")
                        else:
                            current_direction.pop("Area")
                    else:
                        current_direction.pop("Area")
                    frame[d] = current_direction
            else:
                frame.pop("Direction2")
                frame.pop("Direction1")
                frame.pop("Report")
                
            if random.randint(0, 1):
                frame.pop("Speaker"),

            identifiers = {
                "Direction1": "the first direction",
                "Direction2": "the second direction",
                "PhraseType": "",
                "Addressee": "",
                "Speaker": "",
                "Report": ""
            }
            
            questions = {}
            for k, v in frame_subframes.items():
                frame_question = v.frame_questions(identifiers[k])
                if len(frame_question) == 1:
                    questions[k] = list(frame_question.values())[0]
                else:
                    questions[k] = frame_question

            with open('frame.json', 'w') as frame_file:
                frame_file.write(json.dumps(frame, indent=2).encode("ascii", "ignore").decode())
            
            if immediate_1:
                choice1 = random.choice(["choice1a","choice1b","choice1c"])
            elif direction1:
                choice1 = "choice1d"
            else:
                choice1 = "choice1e"
            if immediate_2:
                choice2 = random.choice(["choice2a","choice2b","choice2c"])
            elif direction2:
                choice2 = "choice2d"
            else:
                choice2 = "choice2e"
            choice3 = "choice3i"
            if "Report" in frame:
                if frame["Report"] == "no":
                    choice3 = "choice3i"
                else:
                    choice3 = "choice3"+random.choice("abcdefgh")
            if "Speaker" in frame.keys():
                choice4 = random.choice(["choice4a","choice4b","choice4c"])
            else:
                choice4 = "choice4d"
            if direction2:
                choice5 = "choice5"+random.choice("abc")
            else:
                choice5 = "choice5e"

            choices = choice1+","+choice2+","+choice3+","+choice4+","+choice5

            cmd = f'java -Xmx16G -jar sfgengine-4.7.0-shaded.jar --generate --sfg ./groundcontrol1c.json --with-frame ./frame.json  --text-only --contextual-features {choices}'
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
        
        with open('ground_control_sample_outs.json', 'a+', encoding='utf-8') as out_file:
            out_file.write(out_str)



if __name__ == '__main__':
    open('ground_control_sample_outs.json', 'w', encoding='utf-8').close()
    generate(10)
