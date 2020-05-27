class Evaluator:
    @staticmethod
    def zip_evaluate(coefs_list, words_list):
        if not (len(words_list) == len(coefs_list)
                or all(isinstance(x, str) for x in words_list)
                or all(isinstance(x, float) for x in coefs_list)):
            print(-1)
            return
        print(sum([len(element[0]) * element[1]
              for element in zip(words_list, coefs_list)]))
        return 0

    @staticmethod
    def enumerate_evaluate(coefs_list, words_list):
        if not (len(words_list) == len(coefs_list)
                or all(isinstance(x, str) for x in words_list)
                or all(isinstance(x, float) for x in coefs_list)):
            print(-1)
            return
        print(sum([len(words_list[i]) * coefs_list[i]
                   for i, v in enumerate(coefs_list)]))

        return 0
