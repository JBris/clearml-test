# ClearML Testing

Testing out ClearML.

# Usage

Deploy docker compose services:

```
docker compose up -d
```

Install deps:

```
poetry install --no-root
poetry shell

clearml-init # If clearml.conf doesn't exist
python -m pipelines.pipeline_basic
python -m pipelines.dataset_basic
```

