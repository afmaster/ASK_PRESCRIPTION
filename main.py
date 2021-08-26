# from flask_ngrok import run_with_ngrok # Run with this import if you need to test on your machine
from flask import Flask
from flask import request

import cgitb; cgitb.enable()     # for troubleshooting



app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR SECRET KEY HERE'

# run_with_ngrok(app) # run with this line if you need to test on your machine

@app.route('/dx', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':

        #form = cgi.FieldStorage()
        form = str(request.form)
        print(form)
        #nome = html.escape(form["nome"].value);
        #cpf = html.escape(form["cpf"].value);
        #print(nome, cpf)

    def replacing(string_para_salvar): # NTF8 - to NSCII (replace incompatible characters without excluding them).
        st = string_para_salvar.replace("é", "e")
        st = st.replace("É", "E")
        st = st.replace("é", "e")
        st = st.replace("Ã", "A")
        st = st.replace("Â", "A")
        st = st.replace("À", "A")
        st = st.replace("â", "a")
        st = st.replace("Á", "A")
        st = st.replace("á", "a")
        st = st.replace("à", "a")
        st = st.replace("ã", "a")
        st = st.replace("Õ", "O")
        st = st.replace("Ô", "O")
        st = st.replace("Ó", "O")
        st = st.replace("õ", "o")
        st = st.replace("ô", "o")
        st = st.replace("ó", "o")
        st = st.replace("ê", "e")
        st = st.replace("è", "e")
        st = st.replace("Ê", "E")
        st = st.replace("È", "E")
        st = st.replace("Í", "I")
        st = st.replace("í", "i")
        st = st.replace("ì", "i")
        st = st.replace("ç", "c")
        st = st.replace("Ç", "C")
        return st

    def sendmail(strpttable):
        try:
            msg = EmailMessage()
            msg.set_content(strpttable)

            msg['Subject'] = 'REQUISIÇÃO DE RECEITA'
            msg['From'] = 'SENDER'
            msg['To'] = "RECEIVER"

            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            sleep(3)
            server.login('SENDER', 'PASSWORD')
            sleep(3)
            server.send_message(msg)
            server.quit()
            print("email alternativo enviado")
        except:
            print("Erro no envio de email alternativo")

        msg = replacing(form)
        sendmail(msg)

        return 'Pedido enviado com sucesso.'

    else:
        return 'Falha de envio. Contate a clínica.'


if __name__ == "__main__":
  app.run()