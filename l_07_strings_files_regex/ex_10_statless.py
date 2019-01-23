while True:
    state = input()
    if state == 'collapse':
        break
    fiction = input()
    is_void = False

    while fiction:
        state = state.replace(fiction, '')
        if state.strip():
            fiction = fiction[1:-1]
        else:
            print("(void)")
            is_void = True
            break

    if not is_void:
        print(state.strip())
