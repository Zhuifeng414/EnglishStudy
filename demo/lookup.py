import pandas as pd
import os

class vocal_helper():
    def __init__(self):
        return

    def load_txt_data(self, my_path, txt_name):
        # read txt method one
        f = open(my_path + txt_name + '.txt')
        input_str = ''
        line = ' '
        while line:
            # print(line)
            line = f.readline()
            input_str += line
        f.close()
        return input_str

    def save_txt_file(self, my_path, txtName, context):
        filename = my_path + txtName + '.txt'
        ## 判断文件路径是否存在，如果不存在，则创建，此处是创建多级目录
        file_dir = os.path.split(filename)[0]
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))
        if not os.path.exists(filename):
            os.system(r'touch %s' % filename)
        f = open(filename, "w+")
        f.write(context)
        f.close()

    def df2dict(self, df, key, value):
        res_dict = {}
        for i in range(df.shape[0]):
            row = df.iloc[i, :]
            if row[key] not in res_dict:
                res_dict[row[key]] = row[value]
        return res_dict

    def lookup_word(self, vocal_dict, word):
        if word in vocal_dict:
            return vocal_dict[word]
        else:
            return 'Not found ! - %s'%(word)

    def lookup_list(self, vocal_dict, word_list):
        res_dict = {}
        for word in word_list:
            if word not in res_dict:
                res_dict[word] = self.lookup_word(vocal_dict, word)
        return res_dict

    def print_res(self, word_list, res_dict):
        for word in word_list:
            print('%s   %s'%(word.ljust(10), res_dict[word].rjust(20)))

    def save_res(self, word_list, res_dict, my_path, txtName):
        res_str = ''
        for word in word_list:
            res_str += '%s   %s\n'%(word.ljust(10), str(res_dict[word]).rjust(20))
        print(res_str)
        self.save_txt_file(my_path, txtName, res_str)

        return


nkey = 'word_name'
nvalue = 'note'
file_name = 'e36-4&5'
if __name__ == '__main__':
    # print('Now is your time --------- ')
    # df = pd.read_csv('../data/killer3000.csv')
    # vocal_dict = vocal_helper().df2dict(df, nkey, nvalue)
    # for i in range(1, 25):
    #     if i in [11, 12]:
    #         continue
    #     else:
    #         file_name = 'e%s'%i
    #         lookup_content = vocal_helper().load_txt_data('../data/', file_name)
    #         word_list = lookup_content.replace('\n', ' ').split(' ')
    #         word_list.sort()
    #         print(word_list)
    #         res_dict = vocal_helper().lookup_list(vocal_dict, word_list)
    #         #vocal_helper().print_res(word_list, res_dict)
    #         vocal_helper().save_res(word_list, res_dict, '../res/', file_name)
    print('Now is your time --------- ')
    df = pd.read_csv('../data/killer3000.csv')
    vocal_dict = vocal_helper().df2dict(df, nkey, nvalue)
    lookup_content = vocal_helper().load_txt_data('../data/', file_name)
    word_list = lookup_content.replace('\n', ' ').split(' ')
    word_list.sort()
    print(word_list)
    res_dict = vocal_helper().lookup_list(vocal_dict, word_list)
    # vocal_helper().print_res(word_list, res_dict)
    vocal_helper().save_res(word_list, res_dict, '../res/', file_name)





