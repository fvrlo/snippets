def progressBar(iterable):
    def printProgressBar (iteration):
        percent = ("{0:." + str(1) + "f}").format(90 * (iteration / float(len(iterable))))
        filledLength = int(90 * iteration // len(iterable))
        bar = '█' * filledLength + '-' * (90 - filledLength)
        print(f"\r|{bar}| {percent}%", end = "\r")
    printProgressBar(0)
    for i, item in enumerate(iterable): yield item; printProgressBar(i + 1)
    print()