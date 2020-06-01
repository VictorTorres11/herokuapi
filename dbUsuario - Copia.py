import mysql.connector
import time
class dbUser:
  def __init__(self,host,user,passwd,database):
      self.mydb = mysql.connector.connect(
      host=host,
      user=user,
      passwd=passwd,
      database=database,
      connect_timeout=1000
      )
      self.mycursor = self.mydb.cursor()

  def getUsuarios(self):
    sql = "SELECT * FROM USUARIO"
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    listaUsuarios = []
    for x in myresult:
      listaUsuarios.append(x)
      #print(x[1])
    return listaUsuarios

  def insertUsuario(self,nome,email,telefone,empresa,senha):
    sql = "INSERT INTO USUARIO(NOME, EMAIL, TELEFONE, EMPRESA, SENHA) values(%s,%s,%s,%s,%s)"
    val = (nome,email,telefone,empresa,senha)
    self.mycursor.execute(sql,val)
    self.mydb.commit()
    print(self.mycursor.rowcount, "Inserido com sucesso.")

  def findUsuario_by_ID(self,iD):
    sql = "SELECT * FROM USUARIO WHERE PK_USUARIO=%s;"%iD
    #print(sql)
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    print(myresult)
    return myresult

  def findUsuario_by_EMAIL(self,iD):
    email = str(iD)
    print(email)
    sql = "SELECT * FROM USUARIO WHERE EMAIL='%s';"%email
    print(sql)
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    print(myresult)
    return myresult

  def delete_by_ID(self,iD):
    sql = "DELETE FROM usuario WHERE PK_USUARIO=%s;"%iD
    self.mycursor.execute(sql)
    self.mydb.commit()
    print(self.mycursor.rowcount, "Usuário deletado")

  def updateUsuario(self,iD,nome,email,telefone,empresa,senha):
    sql = "UPDATE USUARIO SET NOME = %s, TELEFONE=%s, EMAIL=%s, EMPRESA =%s, SENHA=%s WHERE PK_USUARIO ="+str(iD)
    self.mycursor.execute(sql)
    self.mydb.commit()
    print(self.mycursor.rowcount, "Usuário Atualizado")

  def loginUsuario(self,email,senha):
    print(email, senha)
    sql = "SELECT * FROM USUARIO WHERE EMAIL='"+str(email)+"' and SENHA='"+str(senha)+"';"
    val = (email,senha)
    print(sql)
    self.mycursor.execute(sql)
    myresult = self.mycursor.fetchall()
    print(myresult)
    return myresult
