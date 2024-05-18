

from enums.loginFieldsEnum import LoginFieldEnum


allowed_uses = [{LoginFieldEnum.USER : "admin", LoginFieldEnum.PASSWORD: "senha" },{LoginFieldEnum.USER : "rodrigo", LoginFieldEnum.PASSWORD: "senha" }
                ,{LoginFieldEnum.USER : "guilherme", LoginFieldEnum.PASSWORD: "senha" },{LoginFieldEnum.USER : "raquel", LoginFieldEnum.PASSWORD: "senha" },{LoginFieldEnum.USER : "lucas", LoginFieldEnum.PASSWORD: "senha" },{LoginFieldEnum.USER : "yago", LoginFieldEnum.PASSWORD: "senha" }]

class Login():

    def validade_user(self,username:str,password:str):
        for user in allowed_uses:
            if (user[LoginFieldEnum.USER] == username) and (user[LoginFieldEnum.PASSWORD] == password):
                return True
        
        return False