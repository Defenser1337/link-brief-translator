# link-brief-translator

Summarize and translate articles via URL.

Paste a link, get a cleaned, structured summary of the article and its translation into the
target language. Built as a small but complete software product around ready-made LLM models
(accessed via an OpenAI-compatible HTTP API), with a focus on infrastructure and engineering
quality.

## Features

- **Asynchronous scraping** with `robots.txt` compliance, including JS-rendered pages
  (Playwright fallback).
- **Text cleaning** with regex pipelines and boilerplate extraction.
- **Summarization strategies:** `single-shot` / `map-reduce` / `refine`, selectable per request.
- **Translation** into a target language via the same LLM endpoint.
- **URL-based cache** — repeated requests are served instantly.
- **FastAPI** (REST API) + **Streamlit** (web UI) + **CLI**.

## Status

Under active development — see [PROJECT.md](PROJECT.md) (local) for the full plan.

## Development

```bash
uv sync                              # install deps
uv run pre-commit install            # hooks
uv run pytest                        # tests (unit + integration, mocked)
uv run pytest -m slow                # integration tests with a real compact model
```

## License

See [LICENSE](LICENSE).
