def create_action_queue(action_list: list):
    print('===========================')
    print(action_list)
    queue = []

    i = 0
    # parse loop
    while i < len(action_list):
        action = action_list[i]

        if action[0] == 'loop':
            loop_times = int(action[1])
            i += 1 # next to 'loop'
            last_end = i
            loop_count = 1
            while True:
                if action_list[last_end][0] == 'loop':
                    loop_count += 1
                if action_list[last_end][0] == 'end':
                    loop_count -= 1
                    if loop_count == 0:
                        break
                last_end += 1
                print(last_end)

            action_in_loop_list = action_list[i:last_end]

            loop_queue = create_action_queue(action_in_loop_list)
            for t in range(loop_times):
                queue += loop_queue
            i = last_end + 1 # after end
        else:
            queue.append(action_list[i])
            i += 1 # next action

    return queue


def isfloat(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True


# NOTE validate negative digit
# return action queue
def action_parser(raw_action: str):
    # validation
    action_list = []
    loop_count = 0
    for line in raw_action.splitlines():
        action = line.split()

        # skip empty line
        if len(action) == 0:
            continue

        print(action)

        if action[0] == 'loop' and len(action) == 2 and action[1].isdigit():
            action_list.append(action)
            loop_count += 1
        elif action[0] == 'end' and len(action) == 1:
            action_list.append(action)
            if loop_count == 0: # 'end' before 'loop'
                raise RuntimeError('SyntaxError', line)
            loop_count -= 1
        elif action[0] == 'move' and len(action) == 3 and \
          (action[1] == 'x' or action[1] == 'y' or action[1] == 'z') and \
          isfloat(action[2]): # NOTE: add velocity?
            action_list.append(action)
        elif action[0] == 'shutter' and len(action) == 1:
            action_list.append(action)
        elif action[0] == 'sleep' and len(action) == 2 and isfloat(action[1]):
            action_list.append(action)
        else:
            raise RuntimeError('SyntaxError', line)

    if loop_count != 0:
        raise RuntimeError('SyntaxError', 'need \'end\'')

    return create_action_queue(action_list)
