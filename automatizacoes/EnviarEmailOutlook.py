import win32com.client as win32
outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
mail.To = 'rwmtecnologia@gmail.com'
mail.Subject = 'Email vindo do Outlook'
mail.Body = 'Texto do E-mail'
mail.HTMLBody = '<p> Teste de corpo do e-mail.<p>'

#anexos
attachment = r'C:\Users\rpiresan\Documents\projetos\python\BigQuery\automatizacoes\arquivos\Financeiro.xlsx'
mail.Attachments.Add(attachment)

mail.Send()