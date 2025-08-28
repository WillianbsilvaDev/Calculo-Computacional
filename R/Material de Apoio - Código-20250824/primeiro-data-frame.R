#Data frames, vamos usar muito!
df_teste01 <- data.frame(
  nome=c("Bob", "Mel", "Tom", "Dan"),
  idade=c(10,10,10,30),
  salario=c(1500.50, 1800.7, 5000.4,850.14)
)

#Acessando apenas uma coluna:
df_teste01$nome

#Funções uteis
mean(df_teste01$idade)  
min(df_teste01$idade)
max(df_teste01$idade)  

#Primeiro Grafico, histograma
hist(df_teste01$idade)
a <- 2
