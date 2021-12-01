import logging
import statistics

def analytics(data):
    logging.warn(f"Unique: {len(set(data)) == len(data)}.")
    logging.warn(f"Type: {type(data[0])}")
    logging.warn(f"Length: {len(data)}. Set length: {len(set(data))}")
    logging.warn(f"Average length: {sum([len(str(a)) for a in data])/len(data)}")
    logging.warn(f"Max length: {max([len(str(a)) for a in data])}. Min length: {min([len(str(a)) for a in data])}")

    if type(data[0]) == int or type(data[0]) == float:
        logging.warn(f"Avg: {sum(data)/len(data)}. Median: {statistics.median(data)}.")
        logging.warn(f"Max: {max(data)}. Min: {min(data)}.")


def autoparse(data, autofilestrip=True, skipsplits=False, min_splits=1, 
              autostrip=True, autofilter=True, autoparse=True, analyze=True):
    # Autostrip
    if len(data) > 1:
        if data[-1] == "\n" or data[0] == "\n":
            data = data.strip()
            logging.info("Autostripped on beg/end")
    

    # Autosplit
    if not skipsplits:
        if len(data.split("\n")) > min_splits:
            data = data.split("\n")
            logging.info("Split on newline")
        elif len(data.split(",")) > min_splits:
            data = data.split(",")
            logging.info("Split on comma")
        elif len(data.split("\t")) > min_splits:
            data = data.split("\t")
            logging.info("Split on tab")
        elif len(data.split(" ")) > min_splits:
            data = data.split(" ")
            logging.info("Split on space")
        else:
            data = [a for a in data]
            logging.info("Split on character")

    # Autostrip per item
    if autostrip:
        data = [a.strip() for a in data]
        logging.info("Autostripped")

    # Autofilter
    if autofilter:
        data = [a for a in data if len(str(a)) > 0]
        logging.info("Autofiltered")

    # Autoparse
    if autoparse:
        autoparsed = False
        for f in (int, float):
            try:
                [f(i) for i in data]
                autoparsed = True
            except ValueError:
                continue
            if autoparsed:
                data = [f(i) for i in data]
                logging.info(f"Autoparsed with f{f}")
                break

    # Analytics
    if analyze:
        analytics(data)

    return data

def multiply(arr):
    acc = arr[0]
    for i in arr[1:]:
        acc *=i

    return acc