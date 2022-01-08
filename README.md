# portscan

Ferramenta bem simples de ser utilizada, tem como objetivo fazer scans de portas. Quando rodar o scan e digitar o IP ou URL
o OUTPUT irá lhe retornar as portas que estão abertas de determinado alvo. 

O script é bem simples de usar o comando que deve ser utilizado, segue a dica para os comandos:
Linux: Abra o terminal vá até o diretório que se encontra o arquivo e execute o comando "python3 portscan.py"
Windows: Abra o cmd e vá até a pasta que está o arquivo e execute o comando "python3 portscan.py"

Bom, vou falar um pouco do desenvolvimento da ferramenta, primeiramente ela é para rodar um escaneamento rápido caso o Penteste,
Analista, estágiario, etc... Tenha esquecido quais portas estão abertas serve muito bem para relembrar ou até mesmo montar o script
em algum lugar onde não tem nmap ou zenmap instalado, o desenvolvimento em si foi bem simples, dificuldades que tive foi para adicionar o
INPUT pois estava dando alguns problemas, quando o IP/URL era fixo foi mais simples porém decidi ir um pouco mais além com um INPUT que pede
para quem estiver usando digitar quem será o alvo.
