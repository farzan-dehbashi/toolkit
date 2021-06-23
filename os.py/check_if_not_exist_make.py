def check_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
