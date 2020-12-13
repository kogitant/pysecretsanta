# pysecretsanta
Little script to draw secret santa gifters and recipients

# Usage
```
python3 main.py --names "Antti,Katja,Aada,Helmi" --lang=fi
```

# Development
## Format sources with Black
```
black .
```

### Verify source codes mathc Black rules
```
black --check .
```

## Run unit tests and verify code coverage 
```
python -m pytest --cov=src --cov-fail-under=80 tests/*
```
