all_csv_files = [file
                     for path, subdir, files in os.walk(in_dir)
                     for file in glob(os.path.join(path, '*.csv'))]
