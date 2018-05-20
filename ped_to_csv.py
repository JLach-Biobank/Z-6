import csv


def ped_to_csv(ped_file, map_file, final_file):
    """
    Transform source data stored in ped and map files to one easy readible csv file.
    :param ped_file: path to ped file
    :param map_file: path to map file
    :param final_file: path to save final file
    """
    with open(map_file) as f:
        map_data = f.readlines()

    with open(ped_file) as f:
        ped_data = f.readlines()

    with open(final_file, 'w') as fw:
        wr = csv.writer(fw, quoting=csv.QUOTE_ALL)

        # Process headers
        headers = ['id', 'fid', 'data1', 'data2', 'sex', 'color']
        for line in map_data:
            data = line.split()
            headers.append(data[1])
        wr.writerow(headers)

        for i in range(len(ped_data)):
            print(i)
            line = ped_data[i].strip().split(" ")
            numbers = line[:6]
            letters = line[6:]
            pairs = []
            for j in range(len(letters)//2):
                pairs.append((letters[2 * j], letters[2 * j + 1]))
            print(len(pairs))
            wr.writerow(numbers + pairs)

