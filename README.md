# auto-job-bot

A PH Jobs post scraper bot which sends new jobs available every hour.

Scraped datas is based from [`queries.json`](./queries.json)

### Scheduled actions

This webhook scraper bot utilizes Deta Space's scheduled actions
https://deta.space/docs/en/basics/micros#scheduled-actions

##

- `queries.json`

```json
[
  {
    "query": "web developer",
    "location": "benguet"
  }
]
```

- Environment Variables

```
WEBHOOK=
DETA_PROJECT_KEY=
```

##

**@tbdsux | &copy; 2023**
