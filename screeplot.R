wssplot <- function(data, nc = 15, seed = 1234) 
  {
  wss <- (nrow(data) - 1) * sum(apply(data, 2, var)) #자유도*분산=TSS : 클러스터의 중심을 찾는 기준점
  for (i in 2:nc) 
    {
    set.seed(seed)
    wss[i] <- sum(kmeans(data, centers=i)$withinss) #합(i개의 군집$중심점과의 거리)
    }
  plot(1:nc, wss, type="b", xlab = "Number of Clusters",
       ylab = "Within groups sum of squares"
       )}

wssplot(BlackFriday_cluster)  

## scree plot을 그리려면 그 점 개수만큼 kmeans clustering 을 수행해야하는 건지 수학적으로 모르고 있었다. 
