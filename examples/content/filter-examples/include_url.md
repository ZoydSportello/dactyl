---
parent: filters.html
desc: This file has included URL examples
categories: ["Filters"]
title: Remote includes examples
---


# Include Code Samples From Remote URLs


Sample:

The `include_url` filter provides a function that can pull in code samples from remote repositories.

Call it like so:

```py
{{ include_url("https://api.github.com/repos/ripple/dactyl/contents/tests/integration.py") }}
```

