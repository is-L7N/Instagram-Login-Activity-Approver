
# Instagram Login Activity Approver

This Python tool automatically checks and approves the most recent login sessions on an Instagram account using a Bearer token.

## Features

- Retrieves the latest login session from your Instagram account.
- Automatically approves the session (marks it as "This was me").
- Uses advanced User-Agent spoofing to avoid detection or blocking.

## How It Works

The script sends a request to Instagram's private API to fetch recent login activities. It then selects the most recent one and confirms it.

This is particularly useful if you're getting login notifications like the one below and want to approve them programmatically:

![Login Activity](./file-210154_temp.jpg)

## Usage

1. Obtain your Instagram Bearer token.
2. Replace the placeholder in the code with your actual token:

```python
token = "Bearer IGT:2:eyJ....."
L7N = Instagram(token).agree()
print(L7N)
```

---

**Author**: [L7N](https://github.com/is-L7N)  
**Telegram**: [t.me/PyL7N](https://t.me/PyL7N)
