from utils import textprocessing


class TestTextProcessing(object):
    def test_remove_accents(self):
        text = 'áàảãạ âấầẩẫậ ăẵẳằắặ éèẻẽẹ êếềệểễ íìịỉĩ óòỏõọ ôốồổỗộ ơớờởỡợ úùủũụ ưứừửữự ýỳỵỷỹ'
        new_text = textprocessing.remove_accents(text)
        assert new_text == 'aaaaa aaaaaa aaaaaa eeeee eeeeee iiiii ooooo oooooo oooooo uuuuu uuuuuu yyyyy'

    def test_clean_text(self):
        text = 'Mỗi lít xăng sẽ chịu thuế môi trường 4.000 đồng còn dầu là 2.000 đồng, cả hai đều là mức cao nhất theo khung hiện hành'
        print(textprocessing.clean_text(text.lower()))