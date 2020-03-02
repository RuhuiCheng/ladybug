import src.plugin.email as email

def test_send():
    ls_to = ["microtaisen@163.com"]
    ls_cc = ["microtaisen@163.com"]
    ls_bcc = ["microtaisen@163.com"]
    mail_subject = "Big data demo1"
    mail_msg ='<table width="100%" border="1" cellspacing="0" bordercolor="#666666" > <tr bgcolor="#99CCFF" > <th>消费项目....</th> <th>一月</th> <th>二月</th> </tr> <tr> <td>衣服</td> <td>$241.10</td> <td>$50.20</td> </tr> </table>'
    bl = email.send(ls_to,ls_cc,ls_bcc, mail_subject, mail_msg)
    assert bl
