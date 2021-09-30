def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path) as f:
        lines = f.readlines()
        parsed_file = []
        for line in lines:
            line = line.replace('\n', '').split(',')
            for index in range(len(line)):
                if line[index].isdigit():
                    line[index] = int(line[index])
                else:
                    line[index] = line[index].strip('\"')
            parsed_file.append(line)

        return parsed_file;
        
