Hackathon Model Deployment

## Build Docker image
```docker build -t image_name .```

## Run container
```docker run --name cont_name -p 8000:8000 image_name```

## Inference 
1. Web interface
    http://0.0.0.0:8000/docs
2. Python script
    ```python3 client.py```
3. curl request:
    ```curl  http://0.0.0.0:8000/predict -d "C1CCCCC1"```