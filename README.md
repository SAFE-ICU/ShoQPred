# ShoQPred - AI for Shock Prediction in ICU Validated across Continents

## Predicting Hemodynamic shock using physiological vitals time-series data
ShoQPred is Deployable Human Centric Software Suite for hemodynamic shock prediction which leverages AI and ML methods on physiological vitals time-series data to predict hemodynamic shock prediction upto 3 to 12 hours before the event.

## Requirements
1. Flask
2. Tensorflow
3. R with HilberVis
(extended requirements in requirements.txt)

or Docker for Docker deployment

## Deployment
### Docker 
Readily available installation, user can pull the docker image from docker hub, here are the instruction to use it
```bash
docker pull raptor4/shoqpred1:latest
docker run --name shoqpred-app -p 5000:5000 raptor4/shoqpred1:latest
```
App will run on localhost:5000

### Native Python
Native System Deployment Reqirements

System must have:-
1. R 3.6+ with HilberVis package
2. Tensorflow 1.15, Keras 2.35+

Install [R](https://cran.r-project.org/bin/windows/base/) 3.6+ and [HilbertVis](https://www.bioconductor.org/packages/release/bioc/html/HilbertVis.html)

Clone the repository, install requirements and run app.

 ```bash
git clone https://github.com/SAFE-ICU/ShoQPred
pip3 install -r requirements.txt
python3 app.py
```



Sample input files are available in sample data.