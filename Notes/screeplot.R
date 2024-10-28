wssplot <- function(data, nc = 15, seed = 1234) {
  # Calculate the total sum of squares (TSS), which serves as a reference for clustering
  wss <- (nrow(data) - 1) * sum(apply(data, 2, var))
  
  # Note: To generate a scree plot, k-means clustering needs to be performed
  # as many times as there are data points (up to 'nc'). This calculates the 
  # within-cluster sum of squares (WSS) for each specified number of clusters.
  for (i in 2:nc) {
    set.seed(seed)
    wss[i] <- sum(kmeans(data, centers = i)$withinss)
  }
  
  # Plot the scree plot showing WSS by number of clusters
  plot(1:nc, wss, type = "b", xlab = "Number of Clusters",
       ylab = "Within groups sum of squares")
}

# Run the function to generate the scree plot
wssplot(BlackFriday_cluster)
