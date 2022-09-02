def path_shortener(path: str):
    labels = path.split("/")
    dir_names = []
    filename = ""
    simple_path = ""

    for l in labels:
        label_is_file_name = "." in l

        if l:
            if not label_is_file_name:
                dir_names.append(l)
            else:
                filename = l

    if not labels[0] == dir_names[0]:
        simple_path += path[0]

    for i, d in enumerate(dir_names):
        i_is_last_directory = i == len(dir_names) - 1

        if i == 0:
            simple_path += d[0]
        elif i_is_last_directory:
            simple_path += f"/{d[0]}/"
        else:
            simple_path += f"/{d[0]}"

    simple_path += filename

    return simple_path
