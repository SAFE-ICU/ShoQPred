library('HilbertVis')
library('RcppCNPy')
path = "aditya/SI_safeicu_9hr/data/test/"
files = c('hr','rr','spo','sys', 'dia')
for(i in files){
    data = read.csv(paste(path,i,".csv", sep=""), header = TRUE)
    hilbert_data<-matrix(0,dim(data)[1],256)
    start.time<-Sys.time()
    for(r in 1:nrow(data)){
      print(r)
      hmat<-hilbertImage(as.double(data[r,c(1:256)]), level=4, mode="mean")
      hilbert_data[r,]<-as.vector(t(hmat))
    }
    end.time<-Sys.time()
    time.taken<-end.time-start.time
    print(time.taken)
    write.csv(hilbert_data, file = paste(path,i,"_hilbert.csv", sep=""),row.names=FALSE)
}
