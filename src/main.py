import json
import math
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import dotenv_values

config = dotenv_values(".env")
DEBUG=int(config["DEBUG_LEVEL"])
ignore = ['\n', ' ', '°', '№'] # TODO move to file
char_total = 0
char_freq = {}


def main():
    process_input()
    
    dump_freq()

    print(f"Calculated entropy: {calculate_entropy()}")

    render_plot()


def process_input():
    with open(config["FILE_INPUT"], encoding='utf-8') as file:
        cur_seq_length = 0
        cur_seq = ""

        while True:
            char = file.read(1)
            if filter(char):
                if DEBUG >= 2:
                    print(f"Skipping character: {char}")
                
                continue
            if not char:
                break
            
            if DEBUG >= 3:
                print(f"Analyzing character: {char}")

            cur_seq = cur_seq + char
            cur_seq_length = cur_seq_length + 1

            if cur_seq_length >= int(config["SEQ_LENGTH"]):
                if DEBUG >= 3:
                    print(f"Analyzing sequence: {cur_seq}")
                count_sequence(str(cur_seq)) # must be converted to str explicitly
                cur_seq = ""
                cur_seq_length = 0
    pass


def filter(input) -> bool:
    if input in ignore:
        return True

    return False


def count_sequence(seq):
    global char_total

    old_value = char_freq.get(seq)

    if old_value is None:
        if DEBUG >= 2:
            print(f"Adding new key: {seq}")
        char_freq.update({seq: 1})
    else:
        char_freq[seq] = char_freq[seq] + 1

    char_total = char_total + 1


def dump_freq():
    with open(config["FILE_FREQ"], 'w') as file:
        json.dump(obj=char_freq, fp=file, ensure_ascii=False)


def calculate_entropy():
    entropy = 0

    for seq in char_freq:
        if DEBUG >= 2:
            print(f"Calculating entropy for seq: {seq}")

        char_prob = char_freq[seq]/char_total
        entropy = entropy + char_prob * math.log2(1/char_prob)

    return entropy


def render_plot():
    df = pd.DataFrame(char_freq, index=[0])

    if DEBUG >= 1:
        print(df)

    plt.figure(figsize=(int(config["HIST_SCALE_X"]),
                        int(config["HIST_SCALE_Y"])),
               dpi=int(config["HIST_DPI"]))
    
    df.sum().sort_values(ascending=False).plot.bar()
    
    plt.xticks(range(len(char_freq)), list(char_freq.keys()))
    
    if config["HIST_MODE"] == "save":
        plt.savefig(config["FILE_HIST"], dpi=int(config["HIST_DPI"]))
    elif config["HIST_MODE"] == "show":
        plt.show()
    else: 
        print("WARN: Invalid value for HIST_MODE")


if __name__ == "__main__":
    main()
