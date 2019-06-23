from __future__ import unicode_literals, print_function, division

import torch

# from Encoder import EncoderRNN
# from AttnDecoder import AttnDecoderRNN
# from ultis import prepareData, evaluate

# use_cuda = torch.cuda.is_available()

# MAX_LENGTH = 50

# TRANSLATION = "eng-vn"
# input_lang, output_lang, pairs = prepareData(TRANSLATION.split("-")[0],
#                                              TRANSLATION.split('-')[1])

# teacher_forcing_ratio = 0.5
# hidden_size = 256
# encoder1 = EncoderRNN(input_lang.n_words, hidden_size)
# attn_decoder1 = AttnDecoderRNN(hidden_size, output_lang.n_words,
#                                1, dropout_p=0.1)
# if use_cuda:
#     encoder1 = encoder1.cuda()
#     attn_decoder1 = attn_decoder1.cuda()


# encoder1.load_state_dict(torch.load("nmt_model/%s_encoder1.pth.tar"%TRANSLATION, map_location={'cuda:0': 'cpu'}))
# encoder1.eval()

# attn_decoder1.load_state_dict(torch.load("nmt_model/%s_attn_decoder1.pth.tar"%TRANSLATION, map_location={'cuda:0': 'cpu'}))
# attn_decoder1.eval()

# class ApiTranslate:
#     @staticmethod
#     def translate(input_sentence=""):
#         output_words, attentions = evaluate(input_lang, output_lang, encoder1, attn_decoder1, input_sentence)
#         return ' '.join(output_words)

#     @staticmethod
#     def init():
#         input_sentence = "i love you"
#         print("Input Sentence: ", input_sentence)
#         output_words, attentions = evaluate(input_lang, output_lang, encoder1, attn_decoder1, input_sentence)
#         print("Output Sentence:", ' '.join(output_words))
def test(test=""):
    return "phuong oi " + test

if __name__ == '__main__':
    # ApiTranslate.init()
    # response = ApiTranslate.translate('hello')
    # print(response)
    print('hello')


 
# input1 = "i love you"
# print("Input Sentence: ", input1)
# print("Output Sentence:", translate_api(input1))

