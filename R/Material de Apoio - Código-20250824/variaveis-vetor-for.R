# Criando variáveis:
a <- 10
b <- 2

#Evite atribuição com =
c = 0;

#Isso funciona, no R qualquer número diferente de 0 retorna TRUE em um condicional
if(a <- 4){
  "teste 1"
}else{
  "teste 2"
}

#Isso não funciona, no R o = é usado para passar valores em parâmetros de funções (exemplo abaixo)
if(a = 4){
  "teste 1"
}else{
  "teste 2"
}

#Usando = para passar um parametro default
somar <- function(a, b = 1){
  return(a + b)
}

#Assim podemos passar opcionalmente o valor de "b"
somar(10, 20)
somar(10)

#Combinações (vetores)
nomes <- c("Bob", "Tom", "Mel")

#No R, o índice começa em 1!!!
nomes[1]

#Exemplo de for
for(nome in nomes){
  cat(nome, "\n")
}

  