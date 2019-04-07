import sys
__author__ = "Thai Thien"


def handle_doi(line):
    """
    handle a single line of doi
    remove space, left, right curly bracket
    only keep doi value
    :param line:
    :return:
    """
    line = line.strip()

    result = line[7:-2]
    return result


if __name__ == "__main__":

    doi_file = "file.bib"

    outfile = "output_doi.txt"

    out = open(outfile, "w")

    if len(sys.argv) > 1:
        doi_file = sys.argv[1]
        print(doi_file)

    for line in open(doi_file, "r"):
        if "doi = " in line:
            doi = handle_doi(line)
            out.write(doi + "\n")

    out.close()