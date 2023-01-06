def result_to_file(all_result: [str],path):
    '''
    function:Mutation completed data storage txt file
    :param all_result: Data to be stored
    :param path:Save txt file path
    '''
    with open(path, "w", encoding="utf-8") as out:
        for _r in all_result:
            out.write(f"{hex(int(_r[:4], 2))[2:]}{hex(int(_r[4:], 2))[2:]} ")
