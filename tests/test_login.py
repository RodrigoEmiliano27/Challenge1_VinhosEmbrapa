

from controllers.login import Login


def test_login_attempts():

    login = Login()

    assert login.validade_user("admin","senha") == True

    assert login.validade_user("raquel","senha") == True

    assert login.validade_user("guilherme","senha") == True

    assert login.validade_user("gui","senha") == False
