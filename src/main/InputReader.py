class InputReader:

    @staticmethod
    def get_data_str(file):
        with open(file) as f:
            return [x.strip() for x in f.readlines()]

    @staticmethod
    def get_data_int(file):
        with open(file) as f:
            return [int(x.strip()) for x in f.readlines()]

    @staticmethod
    def get_data_str_list(file):
        with open(file) as f:
            return [list(x.strip()) for x in f.readlines()]

    @staticmethod
    def get_data_str_split(file):
        with open(file) as f:
            data = [x.strip() for x in f.readlines()]
        split_list = []
        sub_list = []
        for item in data:
            if item != '':
                sub_list.append(item)
            else:
                split_list.append(sub_list)
                sub_list = []
        split_list.append(sub_list)
        return split_list
